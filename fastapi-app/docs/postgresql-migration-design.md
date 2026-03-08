# PostgreSQL 전환 설계 문서 (2단계)

## 1) 대상 도메인 객체
현재 `db` 모듈에 있는 핵심 엔티티는 아래와 같다.
- `UserEntity`
- `Oauth2UserEntity`
- `IngredientEntity`
- `CocktailEntity`
- `CocktailIngredientEntity`
- `BannerEntity`
- `FileEntity`
- `CommentEntity`
- `LikeEntity`
- `BaseEntity`(공통 생성일/수정일)

`Converter`, `enum` 클래스는 PostgreSQL에서는 `VARCHAR` 또는 `SMALLINT`로 변환 후보를 검토한다.

## 2) MySQL → PostgreSQL 타입 매핑
- `VARCHAR(n)` / `TEXT` : 동일 규칙 사용
- `DATETIME`, `TIMESTAMP` : `TIMESTAMP WITH TIME ZONE`
- `BIGINT` : `BIGINT` 유지
- `TINYINT(1)`(boolean 용도) : `BOOLEAN`
- `INT AUTO_INCREMENT` : `SERIAL` 또는 `BIGSERIAL` 사용
- `ENUM` : 우선 `VARCHAR` + `CHECK` 제약 또는 `SMALLINT` + 코드값
- `LONGTEXT` : `TEXT`
- `DOUBLE`/`FLOAT` : `DOUBLE PRECISION` 또는 `NUMERIC`(금액/비율 필요 시)

## 3) 스키마 규칙
- 테이블명/컬럼명은 기존 Java 엔티티 이름 기준으로 `snake_case` 정규화.
- PK/FK/UNIQUE/INDEX를 먼저 정의하고, 이후 서비스 로직과 정렬/검색 인덱스를 추가한다.
- `created_at`, `updated_at`은 UTC 기준(`AT TIME ZONE 'UTC'`)로 저장 후 조회 시 로컬 타임존 변환.

## 4) 초기 마이그레이션 순서
1. `users`, `oauth2_users`, `ingredients` 테이블 생성
2. `cocktails`, `cocktail_ingredients`, `comments`, `likes`, `files`, `banners` 생성
3. FK/UNIQUE 제약 적용
4. 초기 인덱스(검색/정렬/필터 조건) 추가
5. 초기 데이터 적재(필요 시 seed)

## 5) 실행 체크
- 연결 URL: `postgresql+asyncpg://...`
- Alembic `autogenerate` 시 기존 테이블 생성 로그 검증
- `timezone`, `charset/collation`, `enum` 대응 방식은 PR에 명시
