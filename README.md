# RESTAPI 개발 예제 코드

1. 디렉토리 구성
    - sample : 클라이언트 샘플 코드 폴더
    - models : 분석 모델 관련 폴더
    - nginx : nginx 설치 및 설정 파일
    - utils : 기타
2. Python Packages
    - 설치
        ```
        $ pip install -r requirements.txt
        ```
3. models
    - models 폴더에 분석 모델 관련 코드 및 파일 저장
    - 모델 관련 python package 추가 설치 필요
    - models.py 코드와 연동
4. nginx
    - api.conf 수정
        - line2 server_name : local ip 또는 domain 이름으로 수정
        - line5 proxy_pass : api url 주소(ip+port)
    - 설치 (nginx 폴더에서)
        ```
        $ sh setup.sh
        ```
    - nginx configure : /etc/nginx/nginx.conf
5. 실행
    - API 실행
        ```
        $ sh run.sh
        ```
    - API 중지
        ```
        $ sh stop.sh
        ```
    - config.json에서 ip, port 수정 가능
6. 클라이언트 샘플 코드
    - 4가지 예제 코드
