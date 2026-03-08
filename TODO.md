# FastAPI + PostgreSQL 마이그레이션 TODO

## 1. 사전 조사
- [ ] `admin`, `api`, 도메인 기능의 전체 엔드포인트 목록 정리
  - 입력/출력 스키마, 에러 코드, 인증/인가 정책 동시 정리
- [ ] 기존 `db` 모듈 엔티티 목록 파악
  - User, Oauth2User, Ingredient, Banner, Like, Comment, Review 등
- [ ] OAuth, JWT, 파일 업로드, 배포(환경변수) 연계 항목 목록화
- [ ] 우선순위 정의: Phase A(인증), Phase B(핵심 도메인), Phase C(부가 기능)

## 2. PostgreSQL 설계
- [ ] MySQL 타입 매핑 규칙 수립 (`VARCHAR`, `DATETIME`, `TINYINT`, `ENUM` → PostgreSQL 타입)
- [ ] unique/foreign key/index 제약 조건 정리
- [ ] 타임스탬프는 타임존 정책을 `timezone aware`로 통일
- [ ] `cocktail_db` 기준 로컬 PostgreSQL 연결 구성 (`docker compose -f docker-compose.fastapi.yml`)

## 3. FastAPI 스캐폴딩
- [ ] 앱 구조 확정 (`app/api`, `app/core`, `app/db`, `app/models`, `app/schemas`, `app/services`)
- [ ] `requirements.txt`, `alembic`, Docker 실행 환경 정리
- [ ] `.env` 예시 작성 및 비밀값 외부 주입 표준화

## 4. 데이터 계층 이전
- [ ] SQLAlchemy 모델 1:1 대응 설계
- [ ] 리포지토리/서비스 패턴으로 CRUD 경로 분리
- [ ] Alembic 초기 마이그레이션 생성 및 실행

## 5. 인증/보안
- [ ] JWT 발급/검증 공통 모듈 구현
- [ ] 쿠키/헤더 인증 동시 지원
- [ ] OAuth2 로그인(네이버/카카오/구글) 흐름 재구성
- [ ] CORS, Role(`USER`/`ADMIN`) 정책 정합성 검증

## 6. 도메인 API 마이그레이션
- [ ] 사용자/인증 API
- [ ] 재료/배너/좋아요/댓글 API
- [ ] 관리자 API
- [ ] 파일 업로드 API
- [ ] 기존 응답 포맷 및 에러 규칙 동등성 비교

## 7. 테스트/운영 전환
- [ ] pytest + httpx 테스트 골격 구축
- [ ] 스모크 테스트로 기존 플로우 회귀 점검
- [ ] `docker-compose.fastapi.yml` 기반 배포/롤백 시나리오 정리
- [ ] README 및 운영 가이드 업데이트
