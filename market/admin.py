from django.contrib import admin

# Register your models here.
from market.models import User, SiteModel, DBAction


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

    empty_value_display = '-empty-'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id',)
        return self.readonly_fields


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
    empty_value_display = '-empty-'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id',)
        return self.readonly_fields


def discard(modeladmin, request, queryset):
    from market.constants.constants import ActionStatusChoices

    for action_item in queryset:

        if action_item.status not in ['IN PROGRESS', 'DISCARDED', 'DONE', 'FAILED']:
            action_item.status = ActionStatusChoices.DISCARDED.value
            action_item.save()
            print(action_item.status)


discard.short_description = 'Discard selected action items'


def populate(modeladmin, request, queryset):
    from market.constants.constants import ActionStatusChoices

    for action_item in queryset:
        if action_item.status not in ['IN PROGRESS', 'DISCARDED', 'DONE', 'FAILED']:
            action_item.status = ActionStatusChoices.PENDING.value
            action_item.save()
            try:
                _populate_users()
            except Exception as e:
                action_item.description = e.__class__
                action_item.message = f'{str(e)}'
                action_item.status = ActionStatusChoices.FAILED.value
            else:
                action_item.description = 'Populate Successfully'
                action_item.status = ActionStatusChoices.DONE.value
            action_item.save()


populate.short_description = 'Populate Data'


def _populate_users():
    from market.utils.populate.populate_users import PopulateUsers

    o = PopulateUsers()
    o.populate()


@admin.register(DBAction)
class DBActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_filter = ('status',)
    fields = ('name', 'description', 'status', 'message')
    actions = [discard, populate]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'status', 'message']
        else:
            return []
