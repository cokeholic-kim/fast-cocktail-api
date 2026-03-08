# FastAPI Migration Workspace

## 실행
- 의존성 설치: `pip install -r requirements.txt`
- 서버 실행: `uvicorn app.main:app --reload --port 8080`
- 스키마 반영: `alembic -c alembic.ini revision --autogenerate -m "init"`  
  `alembic -c alembic.ini upgrade head`

## 현재 제공 API
- `GET /api/health` : 상태 확인
- `GET /api/users` : 사용자 목록
- `POST /api/users` : 사용자 생성 (`email`, `name`)

## 폴더 구조
- `app/api`: 라우터
- `app/core`: 환경 설정
- `app/db`: DB 엔진/세션
- `app/models`: SQLAlchemy 모델
- `app/schemas`: Pydantic 스키마
- `app/services`: 비즈니스 로직
