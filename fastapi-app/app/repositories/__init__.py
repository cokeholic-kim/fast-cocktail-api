from app.repositories.banner import BannerRepository
from app.repositories.comment import CommentRepository
from app.repositories.cocktail import CocktailRepository
from app.repositories.cocktail_ingredient import CocktailIngredientRepository
from app.repositories.file import FileRepository
from app.repositories.ingredient import IngredientRepository
from app.repositories.like import LikeRepository
from app.repositories.oauth2_user import Oauth2UserRepository
from app.repositories.user import UserRepository

__all__ = [
    "BannerRepository",
    "CommentRepository",
    "CocktailRepository",
    "CocktailIngredientRepository",
    "FileRepository",
    "IngredientRepository",
    "LikeRepository",
    "Oauth2UserRepository",
    "UserRepository",
]
