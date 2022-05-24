from django.contrib import admin

# Register your models here.
from market.models import User, SiteModel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'joined_at')
    fields = (
        'id',
        ('first_name', 'middle_name', 'last_name'),
        'joined_at',
        'mobile_number',
        'email',
    )
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
