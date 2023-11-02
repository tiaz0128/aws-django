# Python 베이스 이미지 사용
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# Python 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 애플리케이션 파일 복사
COPY . .

# 기본 명령어 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]