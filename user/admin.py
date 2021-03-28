from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CreateAccount
from .models import *


# Register your models here.
# class UserAdmin(BaseUserAdmin):
#     add_form = CreateAccount
#     form = CreateAccount
#
#     list_display = (
#         'student_id',
#         'name',
#         'email',
#         'phone'
#     )
#
#     fieldsets = (
#         (None, {'fields': ('student_id', 'password')}),
#         ('Personal info', {'fields': ('name', 'email', 'major', 'phone', 'state', 'grade', 'dues_payment')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('name', 'email', 'major', 'phone', 'state', 'grade', 'dues_payment', 'password1', 'password2')}
#          ),
#     )


admin.site.register(User)
