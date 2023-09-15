# message-controller

디스코드 서버에서 스터디를 진행할 때 활용하기 위한 프로그램입니다.<br>
디스코드 서버에 Bot을 참가시키기 불가능한 경우를 생각해 discord의 자체 API나 Bot 기능을 사용하지 않고 윈도우의 핸들 값을 따와 물리적으로 채팅을 입력하는 방식을 취했습니다.<br>
스터디 진행 인원의 매일 Commit 상황을 확인하기 위해 만들어졌으며, 부가기능으로 사다리타기 기능이 있습니다.<br>
pystray 모듈을 통해 별다른 UI 없이 작업표시줄의 빠른실행 아이콘으로 프로그램을 관리합니다.
data.py에서 스터디 멤버의 인원과 디스코드 서버의 이름을 관리합니다.

Github: https://github.com/jmkim648/message-controller


## <목차>
[1. 주요 기능](#주요-기능)
  - 스터디 구성원의 당일 GitHub 커밋 여부 확인, 알림
  - 스터디 구성원들을 두 팀으로 나눌 때 쓰기 위한 사다리 게임

[2. 기능 설명](#기능-설명)
  - 구현 화면 및 설명

[3. 개발 이슈](#개발-이슈)
  - GitHub에서 정보를 가져올 때 인식이 안됐던 문제
  - Discord에서 구성원을 호출할 때 '@이름' 호출 기능이 작동되지 않던 문제

## <주요 기능>
```
root
├─data
│  └─data.py
├─img
│  └─icon.ico
├─main.py
├─check_github.py
├─find_app_handle.py
├─play_ladder.py
├─requirements.txt
└─README.md
```

## <기능 설명>


## <개발 이슈>