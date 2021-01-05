from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.
# Custom User 등록.
@admin.register(models.User)  # decorator라고 부름
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )


"""
    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "currency")
"""

"""
Admin Panel에 model 나타나게 하는 방법 2가지
== Admin Panel에서 User를 보고싶어
1) @admin.register(models.User)
2) admin.site.register(models.User, CustomUserAdmin)
"""