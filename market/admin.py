from django.contrib import admin

# Register your models here.
from market.models import User, SiteModel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'date_joined', 'is_staff')
    list_filter = ('is_staff', 'date_joined')
    fields = (
        'id',
        'username',
        ('first_name', 'last_name'),
        'date_joined',
        'mobile_number',
        'email',
        (
            'is_staff',
            'is_active',
        ),
    )
    ordering = ('username', 'date_joined')
    readonly_fields = ('id',)

    empty_value_display = '-empty-'


@admin.register(SiteModel)
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'village', 'price', 'availability')
    list_filter = ('state', 'availability', 'is_private')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'id',
                    'type',
                    'price',
                    'availability',
                    'is_private',
                    'owner',
                ),
            },
        ),
        (
            'Location',
            {
                'fields': (
                    'street_name',
                    'village',
                    'city',
                    'district',
                    'state',
                    'country',
                    'location_coordinates',
                )
            },
        ),
    )
    readonly_fields = ('id',)
    empty_value_display = '-empty-'
