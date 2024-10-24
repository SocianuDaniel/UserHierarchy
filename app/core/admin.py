
"""
Django admin costumisation
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }

        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )


class OwnewAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    # readonly_fields = ['user']


class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    # readonly_fields = ['user']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Owner, OwnewAdmin)
admin.site.register(models.Supervisor, SupervisorAdmin)
admin.site.unregister(Group)
