# message-controller

디스코드 서버에서 스터디를 진행할 때 활용하기 위한 프로그램입니다.<br>
디스코드 서버에 Bot을 참가시키는 것이 불가능한 경우를 생각해 discord의 자체 API나 Bot 기능을 사용하지 않고 윈도우의 핸들 값을 따와 물리적으로 채팅을 입력하는 방식을 취했습니다. <br>


스터디 진행 인원의 매일 Commit 상황을 확인하기 위해 만들어졌으며, 부가기능으로 사다리타기 기능이 있습니다.<br>
pystray 모듈을 통해 별다른 UI 없이 작업표시줄의 빠른실행 아이콘으로 프로그램을 관리합니다.
data.py에서 스터디 멤버의 인원과 디스코드 서버의 이름을 관리합니다.

Github: https://github.com/jmkim648/message-controller


## <목차>
[1. 주요 기능](#주요-기능)
  - 스터디 구성원의 당일 GitHub 커밋 여부 확인, 알림
  - 스터디 구성원들을 두 팀으로 나눌 때 쓰기 위한 사다리 게임

[2. 개발 이슈](#개발-이슈)
  - GitHub에서 정보를 가져올 때 인식이 안됐던 문제
  - Discord에서 구성원을 호출할 때 '@이름' 호출 기능이 작동되지 않던 문제
  - pystray와 scheduler 기능 충돌 문제

[3. 기타](#기타)
  - Discord 규정과 Bot 문제

## <주요 기능>

#### <폴더 구조>
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

### <구동 화면 및 설명>
![아이콘](https://github.com/jmkim648/variable-recommander/assets/22714585/2fdbc6d5-76ac-4293-b977-361373df3032)  
\- 작업표시줄 빠른 실행 아이콘

![아이콘-메뉴](https://github.com/jmkim648/variable-recommander/assets/22714585/5f933301-9091-4711-a62d-233e0e0f0dad)  
\- 아이콘 우클릭 메뉴 호출

 - pystray 모듈을 사용하여 프로그램을 실행 시 작업표시줄의 빠른 실행 아이콘이 생성됩니다. 아이콘을 우클릭 시 GitHub의 Commit 여부 확인, 사다리 게임, 프로그램 종료 3가지 메뉴가 표시 됩니다. 종료하기 전까지는 백그라운드에서 계속 실행되고 있으며 이외 별도의 UI는 없습니다.
<br>
<br>

![디스코드-채팅-입력](https://github.com/jmkim648/variable-recommander/assets/22714585/dc4f6104-6caa-4e7e-bc46-d075cd1d810b)  
\- 디스코드 채팅 입력

 - 채팅 입력은 다음과 같은 형태로 진행됩니다.
 ```
 1. 디스코드의 핸들 값을 찾아 활성화
 2. 'tab'을 눌러 채팅창으로 포커스 이동
 3. 필요한 문구를 입력, 인원 호출이 필요한 경우 '@이름' 후 'tab'으로 호출 활성화
 4. enter 입력
 ```
  - 디스코드 내부의 핸들이나 기능에 접근하는 것은 보안적 문제가 있을 것이라 생각되어 키보드로 물리적으로 입력 가능한 범위에서 해결하였습니다. 키보드 입력은 keyboard 모듈을 사용하였습니다.
<br>
<br>

![잔디확인](https://github.com/jmkim648/variable-recommander/assets/22714585/e5e821ab-2d40-4f45-9fa4-ee4cc6946022)  
\- Plant grass 기능 (GitHub Commit 여부 확인)
 - BeautifulSoup4 모듈을 사용하여 GitHub의 Overview 메뉴에서 필요한 데이터를 가져옵니다.<br>Overview의 DOM구조를 파악하여 데이터가 저장된 위치를 특정하였으며, 날짜에 관련된 태그를 이용해 당일 commit이 되었는지의 여부를 파악합니다.
<br>
<br>

![사다리](https://github.com/jmkim648/variable-recommander/assets/22714585/7df30a79-df46-47ed-88b5-2d67c93f6dcc)  
\- Play ladder 기능 (구성원 팀 나누기 위한 사다리게임)
 - 구성원들의 이름을 shuffle 후 두 팀에 나누어 출력합니다.
<br>
<br>

## <개발 이슈>
1. Discord에서 구성원을 호출할 때 '@이름' 호출 기능이 작동되지 않던 문제
   
  ![호출오류](https://github.com/jmkim648/variable-recommander/assets/22714585/a96b6e17-6338-479a-b655-aca34b0f8c6a)
  - 구성원의 호출은 '@이름' 입력 후 'tab'을 입력해 설정합니다. 호출할 구성원의 수가 적을 경우 '@이름' 입력, 0.1초 대기, 'tab'으로 문제없이 호출이 가능하였으나 인원이 많아질 경우 상단과 같이 호출 기능이 먹히지 않았습니다. 코드에 문제가 있을 것이라 생각되어 계속해 디버그, 테스트를 해봤지만 해결하지 못하고, 마지막에서야 디스코드의 인식 시간에 문제가 있을 수 있다는 생각이 들어 테스트, 해결할 수 있었습니다. 대기시간을 0.3초로 늘려 해결하였습니다.
<br>
<br>
  2. pystray와 scheduler 기능 충돌 문제
  
  - 처음에는 schedul 모듈을 사용해 일정 시간마다 자동으로 commit 확인을 해주는 프로그램으로 기획했습니다. 하지만 배포와 실행의 편의성을 위해 pystray를 사용하면서 schedule의 기능과 충돌이 났습니다.
  충돌 원인은 schedule과 pystray 모듈 둘 다 `while True:` 구문을 사용하면서 생긴 문제로, 한쪽의 반복문 때문에 다른쪽으로 진입할 수가 없었습니다.<br><br>
  threading 모듈을 사용하여 쓰레드에서 별개로 scheduler를 돌리는 것도 고려하였지만, 간단한 기능에 비해 쓸 데 없이 반복 연산을 여러개 동작하는 것은 과하다는 생각이 들어 scheduler 기능을 제거하였습니다.


## <기타>
![문의](https://github.com/jmkim648/variable-recommander/assets/22714585/f6fbfc8d-65b4-4cb7-b62b-62a0b711dafc)
- Discord의 API를 사용하지 않고 자동화 기능을 적용하는 것이 괜찮을 지 찾아보았습니다.
현재 프로그램의 기능은 텍스트 정리 후 클립보드에 저장/디스코드 입력창에 붙여넣기 후 엔터를 누르는 수준으로 규정에서 뜻하는 bot과는 다른 것이 아닐까 생각되었습니다. <br><br>
다만, 문구를 적용하는 방법, 메시지 발송 함수를 적용하는 방법에 따라 스캠, 피싱 봇의 형태가 될 수 있단 것을 고려하여 추가 수정, 사용을 자제하기로 결정하였습니다.
