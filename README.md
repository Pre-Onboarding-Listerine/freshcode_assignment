----
# :: 원티드 X 위코드 백엔드 프리온보딩 과제2 <freshcode_assignment>
----
# :: 기업과제
* 기업명: 프레시코드(Fresh Code)
* 기업사이트: https://www.freshcode.me
* 기업채용공고: https://www.wanted.co.kr/wd/34118
----
# :: 팀 :  리스테린(Listerine)

---------------------
|이름|역할|GITHUB|BLOG|
|:--:|:--:|:--:|:--:|
|`고영수`|modeling|https://github.com/kohys92|https://velog.io/@kohys92|
|`김주완`|modeling|https://github.com/joowankim|https://make-easy-anything.tistory.com/|
|`박은혜`|modeling|https://github.com/eunhye43|https://velog.io/@maja43|
|`윤수진`|modeling|https://github.com/Gouache-studio|blog|
|`주종민`|modeling|https://github.com/study-by-myself|https://gouache-studio.tistory.com/|

----
# :: 과제
* <필수 포함 사항>
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
- Swagger 대신 Postman 이용시 API 목록을 Export하여 함께 제출해 주세요
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger를 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅

* <평가 요소>
- 주어진 요구사항에 대한 설계/구현 능력
- 코드로 동료를 배려할 수 있는 구성 능력 (코드, 주석, README 등)
- 유닛 테스트 구현 능력

* <개발 요구 사항>
- Database 는 RDBMS를 이용합니다.
- 로그인 기능
    - JWT 인증 방식을 구현합니다.

* <기능 개발>
- 구현
    - JWT 인증 방식을 이용합니다.
    - 서비스 실행시 데이터베이스 또는 In Memory 상에 유저를 미리 등록해주세요.
    - Request시 Header에 Authorization 키를 체크합니다.
    - Authorization 키의 값이 없거나 인증 실패시 적절한 Error Handling을 해주세요.
    - 상품 추가/수정/삭제는 admin 권한을 가진 사용자만 이용할 수 있습니다.
- 시용자 인증 / 인가
- 상품 관리 기능
    - 아래 상품 JSON 구조를 이용하여 데이터베이스 및 API를 개발해주세요.
        - 구현
            - 서비스 실행시 데이터베이스 또는 In Memory 상에 상품 최소한 5개를 미리 생성해주세요.
            - 상품 조회는 하나 또는 전체목록을 조회할 수 있으며, 전체목록은 페이징 기능이 있습니다.
                - 한 페이지 당 아이템 수는 5개 입니다.
            - 사용자는 상품 조회만 가능합니다.
            - 관리자는 상품 추가/수정/삭제를 할 수 있습니다.
            - 상품 관리 API 개발시 적절한 Error Handling을 해주세요.
----
* <과제 해결 방안>
## ERD (모델링)
![image](https://user-images.githubusercontent.com/32446834/140312743-eda03d7f-c423-46a0-8e34-fda706d50876.png)

> `DRF`와 `PostgreSQL`을 사용해 구현하였습니다.

> freshcode project
- `members`: bulletin board라는 게시판 프로젝트의 구체적인 설정 파일 및 각 앱으로의 요청 라우팅 역할을 맡습니다.
- `menus`: 게시판의 회원에 대한 요청을 처리합니다.
- `items`: 게시글에 대한 조작 요청을 처리합니다.
- `tags`: 인증 및 인가와 관련된 요청을 처리합니다.
- 'tests': 각 app에서 함수 및 메소드들을 `tests` 디렉토리의 테스트들로 유닛테스트를 실행할 수 있습니다.

* <과제 결과물 테스트 및 확인 방법>
- POSTMAN 확인:

## 어플리케이션 실행 방법

# 개발환경 설정 방법

> `git`과 `docker`, `docker-compose`가 설치되어 있어야 합니다.

1. 레포지토리 git 클론

    ```bash
    $ git clone https://github.com/Pre-Onboarding-Listerine/freshcode_assignment.git
    ```

2. `pipenv`를 사용해 python 개발환경 설정

    ```bash
    $ cd <프로젝트 루트 디렉토리>
    $ pip install pipenv

    $ pipenv shell # pipenv 가상환경 활성화
    $ pipenv update # Pipfile.lock 빌드
    $ pipenv install --system # 의존성 패키지 설치 !Pipfile.lock 생성됐는지 확인!
    ```

3. `secret.py` 프로젝트 루트 디렉토리에 위치시키기

4. 애플리케이션 실행하기

    ```bash
    $ docker-compose up

    # 애플리케이션을 백그라운드에서 실행하고 싶다면
    $ docker-compose up -d
    
    # 어플리케이션이 실행이 되고 난 후에 데이터베이스 migration이 필요하다면
    $ docker-compose exec backend python manage.py migrate
    ```

5. 애플리케이션에 접근하기

    django의 디폴트 포트인 8000포트가 아닌 8001번 포트와 연결되어 있습니다. 따라서 아래 주소로 로컬에 실행한 애플리케이션에 접근하실 수 있습니다.
    ```
    http://localhost:8001
    ```

* <사용한 기술 스텍>

>Python = 3.8.12
>Django = 3.2
>Postgres
* <해당 리포의 디렉토리 구조, 코드 구조 및 기타 설명>


![image](https://user-images.githubusercontent.com/32446834/140312743-eda03d7f-c423-46a0-8e34-fda706d50876.png)
