from django.contrib import admin
from .models import Note, UserMaster

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'content', 'name', 'note_file')

    def get_user_name(self, obj):
        return obj.user.name

    get_user_name.short_description = 'User'

@admin.register(UserMaster)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'gender']