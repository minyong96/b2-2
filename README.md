# b2-2

Git 협업 워크플로우(브랜치, PR, 코드 리뷰, 이슈, 충돌 해결, 기록)를 연습하는 팀 저장소입니다.

## 팀원
| 역할 | 이름 | GitHub |
|---|---|---|
| 팀장 | 팀장 | [@minyong96](https://github.com/minyong96) |
| 팀원 | 웅블랙 | [@woongblack](https://github.com/woongblack) |
| 팀원 | 밀키정 | [@Hojun-lang](https://github.com/Hojun-lang) |

## 폴더 구조
```
.
├── README.md
├── SUBMISSION.md      # 제출물 인덱스 (팀원별 PR/문서/증빙 링크)
├── docs/              # 협업 문서 (CONTRIBUTING, conflict-resolution, troubleshooting-log)
├── src/               # 팀원별 유틸 함수
└── .github/           # Issue / PR 템플릿
```

## 유틸 함수 모음
팀원별로 함수를 1개 이상 추가하고, 아래 목록에 사용 예시를 남깁니다.

<!-- 유틸 함수 목록 시작 -->
- `string_utils.reverse_string(text)`: 문자열을 뒤집는다 (웅블랙)
- `file_utils.read_lines(path)`: 파일을 줄 단위로 읽는다 (팀장)
- `utils/math_utils.add(a, b)`: 두 수의 합을 구한다 (밀키정)
<!-- 유틸 함수 목록 끝 -->

## 협업 규칙
GitHub Flow를 따릅니다. 상세 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 참고하세요.

## 문서
- [SUBMISSION.md](SUBMISSION.md): 팀원별 PR/Issue와 증빙 모음
- [docs/conflict-resolution.md](docs/conflict-resolution.md): 충돌 해결 기록
- [docs/troubleshooting-log.md](docs/troubleshooting-log.md): amend, reset, revert, stash 기록
