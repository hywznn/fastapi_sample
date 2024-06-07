# 베이스 이미지 설정
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 가상 환경 생성 및 활성화
RUN python -m venv hywznn

# 애플리케이션 소스 코드 복사
COPY . .

# 가상 환경 활성화 및 종속성 설치
RUN . hywznn/bin/activate && pip install -r requirements.txt

# 애플리케이션 실행 명령어
CMD ["/app/hywznn/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
