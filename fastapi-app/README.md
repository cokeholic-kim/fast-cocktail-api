# FastAPI 마이그레이션 프로젝트 실행 가이드

## 프로젝트 구조
- `fastapi-app/app`: API/설정/DB/모델/스키마/서비스 코드
- `fastapi-app/alembic`: DB 마이그레이션 스크립트
- `fastapi-app/docs`: DB 마이그레이션 설계 문서
- `fastapi-app/requirements.txt`: 의존성

## 실행 준비
1. Python 3.11 기준 가상환경 생성
   - `cd fastapi-app`
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate`
2. 패키지 설치
   - `pip install -r requirements.txt`
3. 환경변수 파일 준비
   - 기본값은 `fastapi-app/.env.example` 사용
   - 로컬 DB 동작 시 `DATABASE_URL`을 `postgresql+asyncpg://postgres:postgres@localhost:5432/cocktail_db`로 설정

## 로컬 실행
- 단일 서버 실행: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8080`
- 헬스체크:
  - `GET /ready` => `{"status":"ready"}`
  - `GET /api/health` => `{"status":"ok"}`
- Swagger: `http://localhost:8080/docs`

## Docker 실행 (DB + FastAPI)
- `docker compose -f docker-compose.fastapi.yml up -d`
- 상태 확인: `docker compose -f docker-compose.fastapi.yml ps`
- 종료: `docker compose -f docker-compose.fastapi.yml down`

## DB 마이그레이션
- 현재 스키마 반영: `alembic -c alembic.ini upgrade head`
- 새 변경 반영: `alembic -c alembic.ini revision --autogenerate -m "..."` 후 `alembic upgrade head`
