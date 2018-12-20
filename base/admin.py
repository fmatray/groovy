# coding: utf-8

"""
Base admin module
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin
from simple_history.admin import SimpleHistoryAdmin
from taggit.models import Tag

# Register your models here.


admin.site.unregister(User)
admin.site.unregister(Tag)

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (('first_name', 'last_name'),
                                         'email')}),
        (_('Permissions'), {'fields': ('is_active',
                                       ('is_staff', 'is_superuser'),
                                       'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')



class BaseAdminMixin():
    FIELDSET_HEADER = [('Identification', {'fields': (('name', 'status'), 'tags', 'description')})]
    FIELDSET_FOOTER = [('Comment', {'fields': ('comment', )})]

    LIST_DISPLAY = ['name', 'status', 'tag_list']
    list_display = []
    LIST_FILTER = ['status', 'tags']
    SEARCH_FIELDS = ['description', 'comment', 'tags']
    extra = 0

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def get_queryset(self, request):
        return super(BaseAdminMixin, self).get_queryset(request).prefetch_related('tags')

    def get_fieldsets(self, request, obj=None):
        if self.fieldsets:
            fieldsets = super(BaseAdminMixin, self).get_fieldsets(request, obj)
            return BaseAdminMixin.FIELDSET_HEADER + fieldsets + BaseAdminMixin.FIELDSET_FOOTER
        return BaseAdminMixin.FIELDSET_HEADER + BaseAdminMixin.FIELDSET_FOOTER

    def get_list_display(self, request):
        if self.list_display:
            list_display = super(BaseAdminMixin, self).get_list_display(request)
            return BaseAdminMixin.LIST_DISPLAY + list(self.list_display)
        return BaseAdminMixin.LIST_DISPLAY

    def get_list_filter(self, request):
        if self.list_filter:
            list_filter = super(BaseAdminMixin, self).get_list_filter(request)
            return BaseAdminMixin.LIST_FILTER + list(list_filter)
        return BaseAdminMixin.LIST_FILTER

    def get_search_fields(self, request):
        if self.search_fields:
            search_fields = super(BaseAdminMixin, self).get_search_fields(request)
            return set(BaseAdminMixin.SEARCH_FIELDS + list(search_fields))
        return BaseAdminMixin.SEARCH_FIELDS

class BaseAdmin(BaseAdminMixin, SimpleHistoryAdmin,  admin.ModelAdmin, ImportExportMixin):
    pass

class BaseStackedInline(BaseAdminMixin, admin.StackedInline):
    pass

class BaseTabularInline(BaseAdminMixin, admin.TabularInline):
    pass

class BaseGenericStackedInline(BaseAdminMixin, GenericStackedInline):
    pass

class BaseGenericTabularInline(BaseAdminMixin, GenericTabularInline):
    pass