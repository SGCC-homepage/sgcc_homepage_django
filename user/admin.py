from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import CreateAccount
from .models import *


# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form = CreateAccount

    list_display = (
        'student_id',
        'name',
        'email',
        'phone'
    )

    list_display_links = (
        'student_id',
        'name',
        'email',
        'phone'
    )


admin.site.register(User, UserAdmin)