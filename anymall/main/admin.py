from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser 모델을 관리자 사이트에 등록하고 CustomUserAdmin 클래스로 관리
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # 관리자 페이지에서 사용자 목록에 표시될 필드들
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # 관리자 페이지에서 사용자 상세 페이지를 어떻게 구성할지 결정
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('user_phone', 'zip_code', 'user_address', 'user_point', 'user_type', 'sub_date', 'grade')}),
    )

    # 검색 기능에 사용될 필드들
    search_fields = ('email', 'first_name', 'last_name', 'user_phone')
    ordering = ('email',)