# 저장소 가이드라인

## 기본 응답 정책
- 이 저장소에서 생성되는 응답은 반드시 **한국어**로 작성한다.

## 프로젝트 구조 및 모듈
- 현재 레포는 멀티 모듈 Gradle 기반 구조를 갖는다.
  - `cocktail-app-api`: 기존 API 진입점
  - `common`: 예외 처리, 공통 유틸
  - `db`: 엔티티/Repository/모델 계층
- `admin/`은 별도 Spring 구조로 존재하며, 기본 Gradle include 대상이 아니다.

## 현재 작업 원칙 (FastAPI + PostgreSQL 전환)
- 최종 목표는 Spring Boot 의존을 제거하고 Python FastAPI + PostgreSQL로 전환한다.
- 1단계: 도메인/엔드포인트/스키마 목록화
- 2단계: DB 스키마 설계 및 마이그레이션
- 3단계: FastAPI 라우팅/서비스/영속성 계층 구현
- 4단계: 인증/권한/OAuth/업로드 통합
- 5단계: 테스트와 운영 전환 자동화

## 빌드/개발 명령
- `./gradlew test` : 기존 Java 모듈 테스트(참고용)
- `./gradlew :cocktail-app-api:bootRun` : 기존 API 실행(참고용)
- `docker compose up --build` : 기존 Spring 기반 실행(기존 스택)
- `docker compose -f docker-compose.fastapi.yml up --build` : FastAPI + PostgreSQL 실행
- `uvicorn app.main:app --reload --port 8080` : FastAPI 로컬 실행(`fastapi-app` 기준)

## 커밋 규칙
- 커밋 메시지는 한국어로 작성한다.
- 형식 권장: `타입: 작업 요약`
  - 예: `feat: 사용자 라우터 초기 스켈레톤 추가`
- 작업 단위는 작고 독립적으로 커밋한다.

## 보안/설정
- 비밀번호·비밀키·토큰은 코드에 하드코딩하지 않는다.
- `.env` 또는 배포 환경 변수로 관리한다.
- PostgreSQL 연결 문자열, OAuth 키, JWT Secret은 마스킹 처리한다.
