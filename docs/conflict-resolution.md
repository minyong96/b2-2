# Conflict Resolution Log

충돌 2건을 `feature/leader-conflict-1` 브랜치에서 `main`을 병합하며 해결했다. (재현 순서: 팀장이 충돌용 브랜치 2개를 먼저 push → 팀원 PR이 main에 병합됨 → 팀장이 `git merge origin/main`)

## 충돌 기록 #1 (같은 파일의 같은 hunk)
### 참여자
- 작성자: 팀장
- 상대: 웅블랙 (PR #17)

### 상황(What happened)
- 팀장 브랜치 `feature/leader-conflict-1`에서 README 함수 목록의 `- (함수 추가 예정)` 줄을 file_utils 항목으로 바꿨다.
- 웅블랙의 `feature/ungblack-string-utils`(PR #17)가 같은 줄을 string_utils 항목으로 바꿔 먼저 main에 병합됐다.
- 같은 줄을 서로 다르게 수정해서, 팀장 브랜치에 `main`을 병합할 때 `CONFLICT (content): Merge conflict in README.md`가 발생했다.

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD
- `file_utils.read_lines(path)`: 파일을 줄 단위로 읽는다 (팀장)
=======
- `string_utils.reverse_string(text)`: 문자열을 뒤집는다 (웅블랙)
>>>>>>> origin/main
```

### 해결 과정(How)
- 선택한 전략: **keep both**. 두 줄은 서로 다른 팀원의 서로 다른 함수 설명이라 하나를 버릴 이유가 없다.
- 절차:
  1. `git merge origin/main` 으로 충돌 발생을 확인
  2. `README.md`의 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 지우고 두 줄을 모두 남김
  3. `git add README.md` 후 병합 커밋

### 결과(Outcome)
- README 함수 목록에 웅블랙(string_utils)과 팀장(file_utils) 항목이 모두 들어갔다.
- 병합 커밋: `58c03e5` (이 기록 PR에 포함)

### 배운 점(Learnings)
- 목록처럼 여러 사람이 같은 자리에 항목을 추가하는 파일은 충돌이 잦다. 한 줄씩 겹치지 않게 항목 사이에 빈 줄을 두거나, 항목마다 파일을 나누면 예방할 수 있다.

## 충돌 기록 #2 (비자명: 한쪽은 이동/삭제, 한쪽은 수정)
### 참여자
- 작성자: 팀장
- 상대: 밀키정 (PR #19, #20)

### 상황(What happened)
- 팀장 브랜치 `feature/leader-conflict-2`(`refactor: math_utils를 src/utils 패키지로 이동`)가 `src/math_utils.py`를 `src/utils/math_utils.py`로 옮기고 첫 줄 docstring도 바꿨다.
- 같은 시기에 밀키정은 원래 경로 `src/math_utils.py`에 `add` 함수를 추가해 main에 병합했다 (PR #19, 그리고 위치를 바로잡은 PR #20).
- 팀장 브랜치에서는 이 파일이 이동(원래 경로 삭제)되었고 main에서는 같은 파일이 수정되어, 병합 시 아래 충돌이 발생했다.
- 파일 이름 변경과 함께 내용도 크게 바뀌어(첫 줄 docstring 변경) git이 이름 변경으로 인식하지 못하고 "삭제 + 새 파일"로 처리했다. 그래서 자동 병합되지 않고 충돌이 됐다.

### 충돌 내용(Conflict markers)
```txt
CONFLICT (modify/delete): src/math_utils.py deleted in HEAD and modified in origin/main.
Version origin/main of src/math_utils.py left in tree.
```
충돌 마커 대신 두 버전이 따로 남는다.
```python
# HEAD (팀장): src/utils/math_utils.py
"""수학 유틸 함수 모음 (utils 패키지로 이동)."""
```
```python
# origin/main (밀키정): src/math_utils.py
"""수학 관련 유틸 함수 모음 (정수 연산)."""


def add(a: int, b: int) -> int:
    """두 수의 합을 반환한다.

    >>> add(2, 3)
    5
    """
    return a + b
```

### 해결 과정(How)
- 선택한 전략: **refactor(합치기)**. 이동한 새 위치(`src/utils/math_utils.py`)를 유지하면서 밀키정의 `add` 함수를 그대로 옮겨 합쳤다. 옛 경로 파일은 삭제한다.
- 절차:
  1. `git merge origin/main` 으로 `modify/delete` 충돌 확인
  2. `src/utils/math_utils.py`에 밀키정의 `add` 함수와 docstring을 합치고, 첫 줄은 두 설명을 합쳐 `"""수학 관련 유틸 함수 모음 (정수 연산, utils 패키지로 이동)."""` 로 정리
  3. `git rm src/math_utils.py` 로 옛 경로 파일 삭제
  4. `git add README.md src/utils/math_utils.py` 후 병합 커밋
  5. `python3 -m doctest src/utils/math_utils.py -v` 로 docstring 예시 통과 확인

### 결과(Outcome)
- `src/utils/math_utils.py`에 밀키정의 `add` 함수가 보존됐고 `src/math_utils.py`는 사라졌다.
- 병합 커밋: `58c03e5` (이 기록 PR에 포함)

### 배운 점(Learnings)
- 파일을 이동하는 사람은 먼저 팀에 알리고, 이동 PR을 짧게 먼저 병합해야 한다. 이동과 동시에 내용도 크게 바꾸면 git이 이동을 추적하지 못한다.
- 이동 전에 다른 사람이 같은 파일을 수정 중인지 `git log`나 열린 PR로 확인한다.
- 이번에는 밀키정의 PR #19가 코드를 `src/`가 아닌 저장소 루트에 `math_utils.py`와 빈 `int` 파일로 잘못 올려(명령에서 `-> int`가 셸 리다이렉션으로 해석됨) PR #20으로 위치를 바로잡았다. 루트에 남은 파일 2개는 이 PR에서 함께 삭제했다 (`9054a3d`). 코드를 붙여 넣을 때는 `cat > 파일 <<'EOF'` 형태를 지켜야 한다.
