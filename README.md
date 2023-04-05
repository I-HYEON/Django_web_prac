2023.04.03(월)
게시물 crud 까지 만들어져있는 프로젝트에, custom_user 모델 설정 후 회원가입, 탈퇴, 정보수정, 비밀번호 변경 기능을 추가.

<어려웠던 점>
- django에서 제공하는 form들이 여러가지가 있는데, 요구하는 인자가 다 달라서 외우기도 힘들고, 왜 그런지 전부 알 수가 없어 이해하기 힘들었다.

<아직 모르겠는 점>
- AuthenticationForm은 request를 인자로 요구하는데 왜 그런지..
- UserCreationForm이랑 다르게 UserChangeForm은 특정 유저의 정보를 수정하는 거라서 instance를 지정해줘야 해서 함수의 인자에 instance를 지정해서 넘겨준다.
- 그런데 PasswordChangeForm은 특정 유저의 비밀번호를 수정하는 거라서 비슷하게 동작할 것 같은데, 'instance='은 사용하지 않고, 그냥 request.user라는 유저정보만 넘겨줘서 왜 그런지 이해는 안가지만 django의 규칙인 것 같다.

2023.04.05.(수)
django에서 static과 media 이란 무엇인지, 어떻게 사용할 수 있는지 연습. 서버를 실행시키면 항상 나타나는 이미지(정적파일) 로드를 가능하게 하고, 글 작성 기능에 사용자가 이미지를 업로드할 수 있는 기능 구현.

<어려웠던 점>
- django가 프레임워크라 그냥 django의 규칙대로 따라야한다는 점을 계속 간과하는 것 같다. 이렇게 하면 될 것 같은데 식으로 접근했더니 계속 이미지 경로를 읽어오는데 실패해서 블로그 여러개를 찾아보고, static 폴더에 img 폴더를 따로 추가해서 경로도 정확히 적어주니까 이미지가 업로드 되었다.

<아직 모르겠는 점>
- 어떤 경우에 앱 내부의 static 폴더를 활용하고 어떤 경우에 앱 외부에 따로 만들어둔 static 폴더를 활용하면 되는지 잘 모르겠다.
