# Troubleshooting Log

팀 전체가 아래 4가지 시나리오를 연습하고 기록한다.
모든 명령은 실습용 저장소(로컬 bare 저장소를 origin으로 둔 연습 저장소)에서 재현했고, 출력은 실제 결과이다. (커밋 해시는 실행할 때마다 달라진다.)

## 시나리오: reset --soft
<!-- reset-entry -->

## 시나리오: amend
### 참여자
- 팀장 (시나리오 수행, 기록 작성)

### 상황
- 로컬에서 커밋했는데 메시지에 오타(`mesage`)가 있다. 아직 push하지 않았다.

### 시도한 명령/절차
```bash
git commit -qam "feat: 인사말 추가 (오타 mesage)"
git log --oneline          # 4cfbb42 feat: 인사말 추가 (오타 mesage)
git commit --amend -m "feat: 인사말 한 줄 추가"
git log --oneline          # 214797b feat: 인사말 한 줄 추가
```

### 결과
- 최근 커밋 메시지만 바뀌었고 커밋 해시가 `4cfbb42`에서 `214797b`로 달라졌다. 커밋 개수는 그대로다.
- 주의: amend는 커밋을 새로 만드는 것과 같아서 이미 push한 커밋에 쓰면 원격 히스토리와 어긋난다. 강제 push가 필요해지므로 push 전에만 쓴다.

### 왜 이 방법을 선택했는가(Why)
- 메시지만 고치면 되는 마지막 커밋이고 push 전이라, 새 커밋을 쌓지 않고 amend로 깔끔하게 정리했다.

## 시나리오: revert
<!-- revert-entry -->

## 시나리오: stash
### 참여자
- 팀장 (시나리오 수행, 기록 작성)

### 상황
- 파일을 수정하는 중인데(커밋하기엔 이르다) 다른 브랜치로 전환해 확인할 일이 생겼다.

### 시도한 명령/절차
```bash
git status --short         #  M a.txt
git stash                  # Saved working directory and index state WIP on main: ...
git status --short         # (변경 없음)
git switch feature/other   # 다른 브랜치에서 작업/확인
git switch main
git stash list             # stash@{0}: WIP on main: ...
git stash pop              # Dropped refs/stash@{0}, a.txt 변경이 돌아옴
git status --short         #  M a.txt
```

### 결과
- stash로 작업 중인 변경을 잠시 치워 브랜치를 전환했고, pop으로 그대로 복원했다.
- 주의: pop은 stash 목록에서 항목을 지운다. 충돌이 나면 항목이 남을 수 있으니 `git stash list`로 확인한다. 새 파일(untracked)은 기본으로 stash되지 않는다.

### 왜 이 방법을 선택했는가(Why)
- 미완성 작업을 의미 없는 커밋(`wip` 등)으로 남기지 않고 임시로 보관하기 위해 stash를 썼다.
