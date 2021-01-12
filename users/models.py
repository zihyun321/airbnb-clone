from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# AbstractUser란
class User(AbstractUser):

    """
    Custom User Model
    - default="" 지정 or null=True 허욤
    - CharField는 한줄, 글자수 제한 없음
    - TextField는 여러줄, 글자수 제한 있음

    """

    # Gender Field 보기
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENER_OTHER, "Other"),
    )

    # Language Field 보기
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    # Currency Field 보기
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "kre"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
    