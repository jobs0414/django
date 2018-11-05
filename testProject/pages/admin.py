from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'bio', 'date_joined')
    list_select_related = ('profile',)

    def bio(self, instance):
        return instance.profile.bio

    def date_joined(self, instance):
        return instance.profile.date_joined

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()

        return super(ProfileAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
