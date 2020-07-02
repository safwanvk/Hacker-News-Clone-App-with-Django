from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Link, Vote, UserProfile, Comment


class VoteAdmin(admin.ModelAdmin):
    pass


class LinkAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'body', 'link', 'created_on')
    list_filter = ['created_on']
    search_fields = ('name', 'body')





admin.site.register(Link, LinkAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Comment, CommentAdmin)





class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
