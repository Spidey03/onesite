from django.contrib import admin

# Register your models here.
from market.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'joined_at')
    fields = (
        'id',
        ('first_name',
         'middle_name',
         'last_name'
         ),
        'joined_at',
        'mobile_number',
        'email'
    )
    empty_value_display = '-empty-'
