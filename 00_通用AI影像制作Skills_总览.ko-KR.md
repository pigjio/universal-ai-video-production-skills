# 범용 AI 영상 제작 Skills｜0.6.0 개요

[중국어 안내](00_通用AI影像制作Skills_总览.md)｜[한국어 안내](00_通用AI影像制作Skills_总览.ko-KR.md)

0.6.0은 10개의 전문 Skill, 2개의 공통 프로토콜, 6개의 프로젝트 템플릿, 3단계 사용 깊이로 구성됩니다. Agent를 처음 사용하는 일반 창작자를 기본 대상으로 하며, 복잡성은 Agent가 내부에서 처리합니다. 전문 판단, 증거 기준, 사람의 최종 판단은 낮추지 않습니다. 이번 버전은 장르·이론 선택, 구체적인 숏 언어, 모호한 피드백의 부분 수정, Seedance / Jimeng용 복사 가능한 결과물을 강화했습니다.

## 사용자에게 보이는 작업 방식

```text
사용자가 자연어로 설명
→ Agent가 현재 시작점과 단계 식별
→ 매 대화에서 작은 목표 하나 완성
→ 사용자가 비교·거절·확정
→ 단계의 전체 산출물 제시
→ 사용자가 단계 완료를 명확히 확정
→ 유효한 권한에 따라 새로운 전체 Markdown 버전 저장
→ 다시 읽기 + PROJECT_INDEX와 SESSION_HANDOFF 업데이트
→ 다음 단계로 진행하거나 새 세션에서 복구
```

“좋아요”, “계속해 주세요”, “방향이 괜찮아요”는 단계 완료를 뜻하지 않습니다. 작품 저장도 업로드, 생성, 게시, 연구 사용 동의를 뜻하지 않습니다.

## 10개의 Skill

| Skill | 사용자 관점의 역할 | 단계 주 파일 |
|---|---|---|
| [ai-creative-workflow-router](skills/ai-creative-workflow-router/SKILL.md) | 유일한 초보자 진입점, 단계 간 라우팅, 복구, 권한, 최소 범위 되돌리기 | `项目简报_vNNN.md` |
| [ai-visual-ideation](skills/ai-visual-ideation/SKILL.md) | 막연한 아이디어를 비교 가능한 창작 방향으로 발전 | `创意核心_vNNN.md` |
| [ai-screenplay-development](skills/ai-screenplay-development/SKILL.md) | 시나리오, 동작 구성, 장면 연결, 대사, 진단, 수정 | `剧本_vNNN.md` |
| [ai-worldbuilding](skills/ai-worldbuilding/SKILL.md) | 세계 규칙, 소재 메커니즘, 시공간, 일관성 | `世界观设定_vNNN.md` |
| [ai-character-design](skills/ai-character-design/SKILL.md) | 캐릭터 콘셉트, 외형, 연기, 제작 자산 | `角色设计_名称_vNNN.md` |
| [ai-scene-design](skills/ai-scene-design/SKILL.md) | 장면 토폴로지, 구도, 빛과 색, 재질, 상태 파생 | `场景设计_名称_vNNN.md` |
| [ai-storyboard-design](skills/ai-storyboard-design/SKILL.md) | Beat, 관람 순서, 블로킹, 리듬, 연속성 | `分镜_场次_vNNN.md` |
| [ai-prompt-execution-contract](skills/ai-prompt-execution-contract/SKILL.md) | 정지 이미지·영상 생성 계약과 Seedance 정식 요청 | `生成请求_对象_vNNN.md` |
| [ai-video-production-classroom](skills/ai-video-production-classroom/SKILL.md) | 제작 그룹, 플랫폼 요청, 이어 만들기, 실제 상태, 편집 납품 | `视频生产计划_vNNN.md` |
| [ai-generation-review](skills/ai-generation-review/SKILL.md) | 실제 미디어 증거, 10차원 리뷰, 진단, 수정, 회귀 검증 | `生成评审_对象_vNNN.md` |

## 세 가지 대화 모드

- **초보자**: 기본값이며 쉬운 말로 한 번에 작은 목표 하나를 진행합니다.
- **협업**: 대안을 함께 비교하고 필요한 선택 이유를 설명합니다.
- **전문가**: 전체 필드, 상태, 의존성, 제작 인계 내용을 표시합니다.

대화 모드는 작업 깊이와 다릅니다. 논의, 탐색 초안, 정식 원고, 제작 인계·검증은 각각 별도로 관리합니다.

## 3단계 사용 깊이

- **production**: 기본값이며 실제 창작과 제작을 수행합니다.
- **provenance**: 필요할 때 방법의 출처, 증거 수준, 적용 범위를 확인합니다.
- **research**: 명확한 연구 동의를 받은 경우에만 활성화합니다. 연구 계층은 제작 스냅샷을 읽기 전용으로 참조할 수 있지만 production의 확정 상태를 다시 써서는 안 됩니다.

## 전문 제작 흐름

```text
확정된 storyboard shots
→ production_group / Clip / DO
→ generation_request
→ 실제 플랫폼 제출과 원본 output
→ 10차원 review
→ edit_unit
→ 사람의 최종 판단과 납품
```

계획, 원고 작성, 저장, 제출, 결과 반환, 기계 리뷰, 사람의 최종 승인은 서로 다른 상태입니다.

학생에게 보이는 간단한 출구는 **만족한 시나리오 → 시나리오 근거가 있는 스토리보드 → 바로 복사할 수 있는 숏별 Seedance 프롬프트**입니다. 이론은 내부 판단에만 사용하며 사용자가 근거를 물을 때 적용 이유와 범위를 설명합니다.

## 파일과 복구

프로젝트 템플릿은 `templates/`에 있습니다. 완전한 저장은 매번 새 버전을 만들고 주 파일을 다시 읽은 뒤, `PROJECT_INDEX.md`와 `SESSION_HANDOFF.md`를 업데이트하고 재확인해야 합니다. 새 세션에서는 `AUTHORIZATIONS.md`, 인덱스, 인계 문서, 실제 산출물을 먼저 읽으며 기억만으로 최신 버전을 추측하지 않습니다.

## 검증 범위

정적 검증은 구조와 규칙이 닫혀 있다는 점만 증명합니다. Agent 텍스트·파일 테스트는 시험한 경로의 동작만 증명합니다. 실제 생성, 예술적 품질, 외부 초보자 사용성은 각각 별도로 검증해야 합니다.
