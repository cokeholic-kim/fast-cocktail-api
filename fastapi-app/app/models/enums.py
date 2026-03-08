from enum import Enum


class UserRole(str, Enum):
    ROLE_ADMIN = "ROLE_ADMIN"
    ROLE_USER = "ROLE_USER"


class LoginMethod(str, Enum):
    app = "app"
    naver = "naver"
    kakao = "kakao"
    google = "google"


class IngredientStatus(str, Enum):
    DELETED = "DELETED"
    REGISTERED = "REGISTERED"
    TEMPORARILY_REGISTERED = "TEMPORARILY_REGISTERED"


class IngredientCategory(str, Enum):
    ALCOHOL_STRONG = "술(고도수)"
    ALCOHOL_WEAK = "술(저도수)"
    NON_ALCOHOL = "주스"
    FRUIT = "과일"
    ETC = "기타"


class CocktailStatus(str, Enum):
    DELETED = "DELETED"
    ADMIN_REGISTERED = "ADMIN_REGISTERED"
    USER_REGISTERED = "USER_REGISTERED"


class Glass(str, Enum):
    SHOT = "샷 글라스"
    HIGHBALL = "하이볼 글라스"
    OLDFASHIONED = "올드패션 글라스"
    COLLINS = "콜린스 글라스"
    MARTINI = "마티니 글라스"
    MAGARITA = "마가리타 글라스"
    PILSNER = "필스터 글라스"
    IRISH_COFFEE = "아이리쉬 카페 글라스"
    POUSSE = "리큐르 글래스"
    BRANDYSNIFTER = "브랜디잔"
    CORDIAL = "코디얼 글라스"
    WHITEWINE = "화이트와인 글라스"
    REDWINE = "레드와인 글라스"
    SHERRY = "쉐리 글라스"
    CHAMPAGNEFLUTE = "플루트 글라스"
    PARFAIT = "파르페 글라스"
    SOUR = "사워 글라스"
    COUPE = "쿠페 글라스"
    MARTINIGLASS = "마티니 글라스"


class Method(str, Enum):
    BUILD = "직접넣기"
    STIR = "휘젓기"
    SHAKE = "흔들기"
    FLOAT = "띄우기"
    BLEND = "블렌드"
    MUDDLE = "머들링"


class Unit(str, Enum):
    mL = "mL"
    OZ = "OZ"
    ts = "ts"
    TS = "TS"
    DASH = "DASH"


class CommentRefCategory(str, Enum):
    COCKTAIL = "COCKTAIL"
    INGREDIENT = "INGREDIENT"
