# access-logfile : api 접속 로그 파일 경로
# bind : url ip 및 port
# workers : api process 수 (일반적으로 CPU core * 2)
# daemon : background 실행
gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log wsgi:app --bind 0.0.0.0:9999 --workers 1 --daemon