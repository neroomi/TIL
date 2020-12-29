# Git Command

> Git 명령어 정리



### 0. init

- `git init`

- `.git/` 폴더를 생성해준다.

<img src="Git Command.assets/image-20201229151435595.png" alt="image-20201229151435595" style="zoom:150%;" />

- `.git` 폴더가 생성된 경우 오른쪽에 `master` 라는 표시가 나온다.
- 최초에 한 번만 하면 된다.



### 1. add

- `git add <추가하고 싶은 파일>`
  - `git add . ` : 현재 폴더의 모든 파일과 폴더를 add(띄어쓰기에 주의)
- working diretory => staging area로 파일 이동



### 2. config

- `git config --global user.email "myemail@gmail.com"`

  - 이메일의 경우 깃헙에 올릴 때 잔디 심는 기준이므로 정확히 입력

- `git config --global user.name "myname"`

- 최초에 한 번만 하면 된다. (바꾸려면 주소만 바꿔서 다시 입력)

  

### 3. commit

- `git commit -m "message"`
- 스냅샷을 찍는 동작
- add 되어있는 파일들을 하나의 묶음으로 저장
- 메세지에 들어가는 내용은 기능 단위로 할 것
- 한 번만 해도 됨
- 만약 git commit 다음에 -m 을 통해 메세지를 안 적으면 이상한 화면에 갇힘
  - INSERT 눌러 첫째줄에 메세지 입력 -> esc 통해 최하단 줄에 :wq 입력 후 Enter -> 탈출



### 4. remote

- `git remote add origin <address>`
- 원격 저장소와 현재 로컬 저장소를 연결



### 5. push

- `git push origin master`
- 깃아 올려줘 origin으로 master을
- 원격저장소에 로컬 저장소의 데이터를 전송



### 6. status

- `git status`
- 현재 git 상태를 출력