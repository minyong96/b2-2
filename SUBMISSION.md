# Submission Index

## Team
- 팀명: b2-2
- 저장소: https://github.com/minyong96/b2-2
- 구성: 팀장 `minyong96`, 팀원 웅블랙(`woongblack`), 밀키정(`Hojun-lang`)
- 협업 방식: GitHub Flow (`main` + `feature/*`), 모든 변경은 Issue 생성 → PR(`Closes #이슈`) → 리뷰 → 병합

## Member PRs

### 팀장 (minyong96)
| 이슈 | PR | 내용 |
|---|---|---|
| #1 | [#12](https://github.com/minyong96/b2-2/pull/12) | 저장소 초기 구조, PR/Issue 템플릿 |
| #2 | [#13](https://github.com/minyong96/b2-2/pull/13) | `docs/CONTRIBUTING.md` |
| #3 | [#14](https://github.com/minyong96/b2-2/pull/14) | `src/file_utils.py` (유틸 함수) |
| #4 | [#15](https://github.com/minyong96/b2-2/pull/15) | `docs/troubleshooting-log.md` 틀, amend/stash 기록 |
| #5, #6 | [#21](https://github.com/minyong96/b2-2/pull/21) | 충돌 #1, #2 해결과 `docs/conflict-resolution.md` |
| #7 | [#16](https://github.com/minyong96/b2-2/pull/16) | 이 문서(SUBMISSION.md)와 증빙 |
| - | [#23](https://github.com/minyong96/b2-2/pull/23) | PR #22의 revert 기록 위치 교정 |

- 리뷰 작성: [#17](https://github.com/minyong96/b2-2/pull/17), [#18](https://github.com/minyong96/b2-2/pull/18), [#19](https://github.com/minyong96/b2-2/pull/19), [#20](https://github.com/minyong96/b2-2/pull/20)

### 웅블랙 (woongblack)
| 이슈 | PR | 내용 |
|---|---|---|
| #8 | [#17](https://github.com/minyong96/b2-2/pull/17) | `src/string_utils.py` (유틸 함수), 리뷰 반영 커밋 `a8fc47b` |
| #9 | [#18](https://github.com/minyong96/b2-2/pull/18) | troubleshooting 기록 - reset --soft |

- 리뷰 작성: [#12](https://github.com/minyong96/b2-2/pull/12), [#13](https://github.com/minyong96/b2-2/pull/13), [#14](https://github.com/minyong96/b2-2/pull/14), [#15](https://github.com/minyong96/b2-2/pull/15)

### 밀키정 (Hojun-lang)
| 이슈 | PR | 내용 |
|---|---|---|
| #10 | [#19](https://github.com/minyong96/b2-2/pull/19), [#20](https://github.com/minyong96/b2-2/pull/20) | `src/math_utils.py` (유틸 함수). #19에서 파일 위치가 잘못되어 #20으로 바로잡음 |
| #11 | [#22](https://github.com/minyong96/b2-2/pull/22) | troubleshooting 기록 - revert (위치 오류는 [#23](https://github.com/minyong96/b2-2/pull/23)에서 교정) |

- 리뷰 작성: [#14](https://github.com/minyong96/b2-2/pull/14), [#15](https://github.com/minyong96/b2-2/pull/15)

## Key Docs
- Contributing: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- Conflict log: [docs/conflict-resolution.md](docs/conflict-resolution.md)
- Troubleshooting: [docs/troubleshooting-log.md](docs/troubleshooting-log.md)

## 결과물
- 선택: (A) 유틸 함수 모음 (Python 3.10+)
- 팀원별 함수와 사용 예시(각 함수 docstring, README 함수 목록)

| 팀원 | 파일 | 함수 |
|---|---|---|
| 팀장 | `src/file_utils.py` | `read_lines(path)` |
| 웅블랙 | `src/string_utils.py` | `reverse_string(text)` |
| 밀키정 | `src/utils/math_utils.py` | `add(a, b)` |

## 충돌 해결 (2회, 비자명 포함)
| 구분 | 내용 | 기록 |
|---|---|---|
| 충돌 #1 | README 함수 목록의 같은 줄을 팀장/웅블랙이 서로 다르게 수정 | `docs/conflict-resolution.md` 충돌 기록 #1 |
| 충돌 #2 (비자명) | 팀장은 `src/math_utils.py`를 이동·수정, 밀키정은 원래 파일을 수정 (modify/delete) | `docs/conflict-resolution.md` 충돌 기록 #2 |

## Troubleshooting 4종
| 시나리오 | 참여 | 위치 |
|---|---|---|
| `git commit --amend` | 팀장 | `docs/troubleshooting-log.md` |
| `git reset --soft HEAD~1` | 팀장, 웅블랙 (PR #18) | `docs/troubleshooting-log.md` |
| `git revert` | 팀장, 밀키정 (PR #22, #23) | `docs/troubleshooting-log.md` |
| `git stash` / `git stash pop` | 팀장 | `docs/troubleshooting-log.md` |

## 참고 사항
- 충돌 해결 커밋 4개(`b9a9079`, `58c03e5`, `9054a3d`, `32d4a2f`)는 팀장이 수행했지만, 로컬 git 작성자 설정이 일시적으로 `Hojun-lang`으로 바뀌어 커밋 작성자 이름이 `Hojun-lang`으로 표시된다. PR [#21](https://github.com/minyong96/b2-2/pull/21)의 작성자는 `minyong96`이다. 공유 브랜치의 히스토리를 다시 쓰지 않는 규칙에 따라 그대로 두었다.
- 루트에 잘못 올라간 `int`, `math_utils.py`(PR #19)는 PR #21에서 삭제했다.

## Evidence
`git log --oneline --graph --all` 결과:

```txt
*   473e352 Merge remote-tracking branch 'origin/main' into feature/leader-submission
|\
| *   fe23cca Merge pull request #18 from minyong96/feature/ungblack-troubleshoot-reset
| |\
| | * 9ddd440 docs: reset --soft 트러블슈팅 기록 추가
| * |   c221b4b Merge pull request #21 from minyong96/feature/leader-conflict-1
| |\ \
| | * | 32d4a2f docs: 충돌 해결 기록(README 같은 hunk, math_utils 이동 vs 수정) 추가
| | * | 9054a3d chore: 루트에 잘못 올라온 int, math_utils.py 삭제하고 README에 add 항목 추가
| | * |   58c03e5 Merge main into feature/leader-conflict-1 (README, math_utils 충돌 해결)
| | |\ \
| | |/ /
| |/| |
| * | |   441ff73 Merge pull request #20 from minyong96/feature/milkyjung-math-utils
| |\ \ \
| | * | | 79d1119 feat: 두 수의 합을 구하는 add 함수 추가
| * | | | b94447d Merge pull request #19 from minyong96/feature/milkyjung-math-utils
| |\| | |
| | |_|/
| |/| |
| | * | 748bedf feat: 두 수의 합을 구하는 add 함수 추가
| | * | 217db8b docs: add 음수 입력 예시 추가 (리뷰 반영)
| |/ /
| * |   0f5e972 Merge pull request #15 from minyong96/feature/leader-troubleshoot
| |\ \
| | * | 5dc7f0b docs: troubleshooting 로그 틀과 amend, stash 기록 추가
| * | |   9585835 Merge pull request #14 from minyong96/feature/leader-file-utils
| |\ \ \
| | * | | 2bf0f7d feat: 파일을 줄 단위로 읽는 read_lines 함수 추가
| | |/ /
| * | |   066cdc9 Merge pull request #17 from minyong96/feature/ungblack-string-utils
| |\ \ \
| | * | | a8fc47b docs: reverse_string 빈 문자열 예시 추가 (리뷰 반영)
| | * | | e5d3918 feat: 문자열 뒤집기 함수 reverse_string 추가
| |/ / /
| * | |   de0971d Merge pull request #13 from minyong96/feature/leader-contributing
| |\ \ \
| | * | | 46cfe55 docs: CONTRIBUTING 협업 규칙 문서 추가
| | |/ /
| * | |   f184eb5 Merge pull request #12 from minyong96/feature/leader-init
| |\ \ \
| * | | | b02fba3 docs: 가이드에 전체 진행 순서와 첫 단계(리뷰) 안내 추가
| * | | | 0f4bb41 docs: 가이드 리뷰 항목을 PR 통합 기준(리뷰 3개)으로 수정
| * | | | a81c963 docs: 팀원 가이드를 저장소 루트로 이동
| * | | | 37d1576 docs: 팀원별 진행 가이드(웅블랙, 밀키정) 추가
| | |/ /
| |/| |
| | | *   b9a9079 Merge remote-tracking branch 'origin/feature/leader-conflict-2' into feature/leader-conflict-1
| | | |\
| | | | * 14624bd refactor: math_utils를 src/utils 패키지로 이동
| | | |/
| | |/|
| | | * 8cf41cb docs: README 함수 목록에 file_utils 항목 추가
| | |/
| | * ab0a301 chore: 저장소 초기 구조와 PR/Issue 템플릿 추가
| |/
* / 833b791 docs: SUBMISSION 제출물 인덱스 초안 추가
|/
* 4e1dcd8 first commit
```
