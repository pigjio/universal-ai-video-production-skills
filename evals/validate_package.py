#!/usr/bin/env python3
"""Read-only package checks. Usage: python evals/validate_package.py [root].
Checks authored local refs recursively, common-contract consistency and schema;
not a semantic proof, trigger benchmark, generation test or licensing audit.
"""
from pathlib import Path
import re, sys, json, hashlib
try:
    import yaml
except ImportError:
    raise SystemExit('Dependency missing: install PyYAML with python -m pip install pyyaml')
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
SKILLS = {f.parent.name:f for f in (ROOT/'skills').glob('*/SKILL.md')}
EXPECTED = {'ai-character-design','ai-creative-workflow-router','ai-generation-review','ai-prompt-execution-contract','ai-scene-design','ai-screenplay-development','ai-storyboard-design','ai-video-production-classroom','ai-visual-ideation','ai-worldbuilding'}
EXPECTED_VERSION = '0.5.0'
REQUIRED_ROOT = ['START_HERE.md','AGENTS.md','CLAUDE.md','shared/common-contract.md','shared/novice-guidance-protocol.md','templates/PROJECT_BRIEF.md','templates/PROJECT_INDEX.md','templates/SESSION_HANDOFF.md','templates/DECISIONS.md','templates/AUTHORIZATIONS.md','templates/stage-deliverable-template.md','provenance/README.md','research-extension/README.md','evals/novice-cases-0.5.0.md']
FIELDS = ['artifact_id','version','artifact_type','creative_mode','subject_type','lifecycle_status','production_status','approval_level','upstream_versions','confirmed_evidence','open_questions','recheck_trigger','next_action']
ENUMS = {'artifact_type':set('idea script world character scene storyboard prompt clip review'.split()), 'creative_mode':set('narrative perceptual conceptual'.split()),'subject_type':set('character-led environment-led object-led abstract'.split()),'lifecycle_status':set('draft candidate confirmed needs_recheck invalidated'.split()), 'production_status':set('not_applicable not_started planned awaiting_external_generation submitted generated under_review reviewed failed'.split()),'approval_level':set('none direction_approved production_approved human_confirmed'.split())}
errors=[];warnings=[];refs_count=0;records=0

# Detect personal absolute paths without embedding any real user, machine, or
# project identifiers in the validator itself. Common documentation
# placeholders remain allowed.
PLACEHOLDER_USERS = {'user','username','example','example-user','your-name','name'}
UNIX_USER_PATH = re.compile(r'(?<![\w/])/(?:home|Users)/([^/\s`"\']+)(?:/[^\s`"\']+)?')
WINDOWS_USER_PATH = re.compile(r'(?i)(?<![\w])(?:[a-z]:[\\/])Users[\\/]([^\\/\s`"\']+)(?:[\\/][^\s`"\']+)?')
MOUNTED_DRIVE_PATH = re.compile(r'(?<![\w/])/mnt/[a-z]/[^\s`"\']+')

def private_path_hits(data):
    hits=[]
    for lineno,line in enumerate(data.splitlines(),1):
        for pattern in (UNIX_USER_PATH,WINDOWS_USER_PATH):
            for match in pattern.finditer(line):
                if match.group(1).lower() not in PLACEHOLDER_USERS:
                    hits.append((lineno,match.group(0)))
        for match in MOUNTED_DRIVE_PATH.finditer(line):
            hits.append((lineno,match.group(0)))
    return hits

# Synthetic regression cases are assembled in pieces so the validator can
# safely scan its own source without treating the fixtures as package leaks.
privacy_cases = [
    ('/home/'+'example-person'+'/private-work', True),
    ('/mnt/'+'x'+'/private-knowledge-base', True),
    ('C:\\Users\\'+'example-person'+'\\drafts', True),
    ('/home/'+'user'+'/project', False),
]
for sample,expected in privacy_cases:
    if bool(private_path_hits(sample)) != expected:
        errors.append('privacy path detector regression')
if set(SKILLS)!=EXPECTED: errors.append('Unexpected skill names/count')
canonical=(ROOT/'shared/common-contract.md').read_bytes()
novice_canonical=(ROOT/'shared/novice-guidance-protocol.md').read_bytes()
for rel in REQUIRED_ROOT:
    p=ROOT/rel
    if not p.is_file() or not p.read_text(encoding='utf-8').strip():errors.append(f'missing/empty required file: {rel}')

def check_record(obj,where):
    global records
    if not isinstance(obj,dict) or 'artifact_id' not in obj:return
    records+=1
    for key in FIELDS:
        if key not in obj:errors.append(f'{where}: missing public field {key}')
    incomplete = (obj.get('lifecycle_status') in {'draft','needs_recheck'} and obj.get('approval_level')=='none' and isinstance(obj.get('payload'),dict) and obj['payload'].get('record_completeness')=='incomplete' and bool(obj.get('open_questions')))
    for key,values in ENUMS.items():
        if key in obj and obj[key] not in values:
            if not (incomplete and obj[key] is None and key not in {'lifecycle_status','approval_level'}):
                errors.append(f'{where}: invalid {key}: {obj[key]}')
    if not isinstance(obj.get('upstream_versions'),dict):errors.append(f'{where}: upstream_versions must be mapping')
    for key in ['confirmed_evidence','open_questions','recheck_trigger']:
        if not isinstance(obj.get(key),list):errors.append(f'{where}: {key} must be list')
    if obj.get('lifecycle_status')=='needs_recheck' and obj.get('approval_level')!='none':errors.append(f'{where}: recheck approval is not current')
    payload=obj.get('payload',{})
    if isinstance(payload,dict):
        if obj.get('subject_type')!='character-led' and payload.get('character') not in (None,'not_applicable'):errors.append(f'{where}: noncharacter record adds character')
        if obj.get('production_status')=='awaiting_external_generation' and payload.get('result_artifact'):errors.append(f'{where}: awaiting record fabricates result')

for name,body in sorted(SKILLS.items()):
    text=body.read_text(encoding='utf-8')
    try:fm=yaml.safe_load(text.split('---',2)[1])
    except Exception as e:errors.append(f'{name}: frontmatter {e}');continue
    if fm.get('name')!=name or fm.get('version')!=EXPECTED_VERSION:errors.append(f'{name}: wrong name/version')
    if len(fm.get('description',''))>1024:errors.append(f'{name}: description too long')
    for dep in fm.get('metadata',{}).get('hermes',{}).get('related_skills',[]):
        if dep not in SKILLS:errors.append(f'{name}: external related skill {dep}')
    common=body.parent/'references/common-contract.md'
    if not common.exists() or common.read_bytes()!=canonical:errors.append(f'{name}: common contract mismatch')
    novice=body.parent/'references/novice-guidance-protocol.md'
    if not novice.exists() or novice.read_bytes()!=novice_canonical:errors.append(f'{name}: novice protocol mismatch')
    if 'references/novice-guidance-protocol.md' not in text:errors.append(f'{name}: novice protocol is not routed')
    for marker in ['PROJECT_INDEX.md','SESSION_HANDOFF.md','完整正文']:
        if marker not in text:errors.append(f'{name}: missing stage persistence marker {marker}')
    for ref in (body.parent/'references').glob('*.md'):
        refs_count+=1
        if f'references/{ref.name}' not in text:errors.append(f'{name}: unrouted reference {ref.name}')
    for field in FIELDS:
        if not re.search(r'^\s*'+field+r':',text,re.M):errors.append(f'{name}: body lacks public template field {field}')
    for f in body.parent.rglob('*.md'):
        data=f.read_text(encoding='utf-8');where=str(f.relative_to(ROOT))
        if '\ufffd' in data:errors.append(f'{where}: replacement character')
        if '\\n' in data and not re.search(r'```(?:python|bash)',data):warnings.append(f'{where}: possible literal escaped newline')
        for lineno,_hit in private_path_hits(data):
            errors.append(f'{where}:{lineno}: personal absolute path detected')
        if re.search(r'^\s*status:\s',data,re.M):errors.append(f'{where}: legacy generic status field')
        for block in re.findall(r'```ya?ml\s*\n(.*?)```',data,re.S):
            try:
                obj=yaml.safe_load(block);check_record(obj,where)
            except Exception as e:errors.append(f'{where}: invalid YAML example: {e}')
        # All inline-code authored paths into bundled resource dirs, including references inside references.
        for token in re.findall(r'`([^`\n]+)`',data):
            for m in re.finditer(r'(?<![\w/])((?:\.\./)*(?:references|scripts|templates|assets)/[\w./-]+\.(?:md|py|json|yaml|yml|txt))',token):
                rel=m.group(1); candidates=[body.parent/rel,f.parent/rel]
                if not any(x.is_file() for x in candidates):errors.append(f'{where}: missing nested resource {rel}')
            # Bare same-directory references, not code placeholders or descriptive source attribution.
            if re.fullmatch(r'[\w\u4e00-\u9fff-]+\.md',token) and not (f.parent/token).exists():
                project_names={'SKILL.md','PROJECT_BRIEF.md','PROJECT_INDEX.md','SESSION_HANDOFF.md','AUTHORIZATIONS.md','DECISIONS.md'}
                if token not in project_names and '_vNNN.md' not in token and f.name not in {'common-contract.md','novice-guidance-protocol.md'}:
                    warnings.append(f'{where}: bare filename requires scope review: {token}')
        for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',data):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            if target and not (f.parent/target).exists():errors.append(f'{where}: missing markdown link {target}')

fixture=ROOT/'evals/fixtures/handoff.json'
if fixture.exists():
    for obj in json.loads(fixture.read_text(encoding='utf-8')):check_record(obj,'fixture:'+str(obj.get('artifact_id')))

# Package-wide release leakage and onboarding assertions.
for f in ROOT.rglob('*'):
    if '.git' in f.parts:continue
    if not f.is_file() or f.suffix.lower() not in {'.md','.py','.json','.yaml','.yml','.txt'}:continue
    data=f.read_text(encoding='utf-8',errors='replace');where=str(f.relative_to(ROOT))
    for lineno,_hit in private_path_hits(data):
        errors.append(f'{where}:{lineno}: personal absolute path detected')
auth=(ROOT/'templates/AUTHORIZATIONS.md').read_text(encoding='utf-8') if (ROOT/'templates/AUTHORIZATIONS.md').exists() else ''
if not re.search(r'research',auth,re.I) or not re.search(r'(denied|not_granted|未授权|不允许)',auth,re.I):
    errors.append('AUTHORIZATIONS template must keep research unauthorized by default')
for marker in ['首次保存自动初始化','确认但暂不保存','不得要求新手复制模板']:
    if marker not in novice_canonical.decode('utf-8'):
        errors.append(f'novice protocol missing onboarding marker: {marker}')
for name, body in sorted(SKILLS.items()):
    skill_text = body.read_text(encoding='utf-8')
    if '自动创建缺失的项目基础记录文件' not in skill_text and '自动从模板创建缺失的项目基础记录文件' not in skill_text:
        errors.append(f'{name}: missing first-save initialization behavior')
    if '确认但暂不保存' not in skill_text:
        errors.append(f'{name}: missing combined closeout choice')
print(json.dumps({'skills':len(SKILLS),'references':refs_count,'schema_records_checked':records,'errors':errors,'warnings':warnings,'scope':'static recursive resources + schema only'},ensure_ascii=False,indent=2))
sys.exit(bool(errors))
