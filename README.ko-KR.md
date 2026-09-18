# 범용 AI 영상 제작 Skills

[中文](README.md)｜[한국어](README.ko-KR.md)

버전: **0.7.0｜공개 간소화판**

열 가지 내부 작업을 포함한 하나의 창작 협업 플러그인입니다. 아이디어 논의, 시나리오 수정, 캐릭터·장소 정리, 텍스트 스토리보드와 Midjourney／Seedance 프롬프트 작성을 돕습니다. 이론을 먼저 배우거나 Skill을 직접 고를 필요가 없습니다.

## 시작하기

[v0.7.0 압축 파일](https://github.com/pigjio/universal-ai-video-production-skills/archive/refs/tags/v0.7.0.zip)을 다운로드하고 압축을 푼 뒤 호환 Agent에 [시작 안내](START_HERE.ko-KR.md)를 읽도록 요청하세요. 예전 사본이 있다면 이 버전을 새로 받으세요. 이전 폴더를 새 패키지에 합쳐 덮어쓰면 불필요한 파일이 남을 수 있으므로 피하세요.

플러그인 설치를 지원하는 환경에서는 이 저장소의 Marketplace 목록인 `.agents/plugins/marketplace.json`을 사용할 수 있습니다. 플러그인 ID는 `universal-ai-video-production`입니다. 구체적인 설치 방법은 현재 클라이언트에 따릅니다. 열 가지 Skill을 따로 설치할 필요가 없습니다.

> 단편 영상을 만들고 싶어요. 먼저 아이디어와 시나리오를 함께 논의해 주세요. 한 번에 너무 많은 질문은 하지 말아 주세요.

## 만들 수 있는 결과

- 피드백에 따라 다듬는 개요와 상세 시나리오.
- 필요한 캐릭터·장소 목록과 선택적인 콘셉트 이미지 프롬프트.
- 얼굴 특징을 포함한 간결한 캐릭터 프롬프트. 3D 스타일은 자동으로 넣지 않습니다.
- 시나리오 키워드를 바탕으로 한 간단한 장소 프롬프트.
- 시나리오에 근거한 텍스트 스토리보드와 항목이 갖춰진 Seedance 프롬프트. 각 영상 프롬프트의 마지막 줄은 “无背景音乐”입니다.
- 실제 이미지나 영상을 제공한 뒤 구체적인 문제와 수정 방향 논의.

생성 서비스는 포함하지 않으며 생성 결과를 보장하지 않습니다. 저장, 업로드, 생성, 비용 지출, 공개, 연구 활용은 각각 해당하는 동의에 따릅니다.

## 문서 안내

- [빠른 시작](START_HERE.ko-KR.md)
- [사용 설명서](skills/ai-creative-workflow-router/references/user-guide.ko-KR.md)
- [기능 개요](00_通用AI影像制作Skills_总览.ko-KR.md)
- [처음 사용하는 분을 위한 안내](shared/novice-guidance-protocol.ko-KR.md)
- [협업 및 저장 원칙](shared/common-contract.ko-KR.md)
- [영상 프롬프트 양식 · 한국어 포함](skills/ai-prompt-execution-contract/references/video-template.md)
- [출처와 라이선스 · 한국어 포함](NOTICE.md)
- [MIT 라이선스 원문](LICENSE)

유지 관리 검사: `python evals/validate_public.py`. 패키지 구조, 링크 및 고정 출력 규칙만 확인하며 창작 품질이나 실제 생성 성공을 증명하지 않습니다.
