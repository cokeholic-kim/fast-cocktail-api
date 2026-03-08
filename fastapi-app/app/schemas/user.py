from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.enums import LoginMethod, UserRole


class UserCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    nick_name: str = Field(serialization_alias="nickName", validation_alias="nickName")
    email: EmailStr
    password: str | None = None
    role: UserRole = UserRole.ROLE_USER
    login_method: LoginMethod = LoginMethod.app


class UserResponse(UserCreate):
    id: int
    role: str
