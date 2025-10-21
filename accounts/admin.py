from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional', {'fields': ('role', 'phone', 'department')}),
    )

admin.site.site_header = "St.Martin's Hospital Administration"
admin.site.site_title = "St.Martin's Hospital Admin Portal"
admin.site.index_title = "Welcome to St.Martin's Hospital Admin"
