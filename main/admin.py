from django.contrib import admin
from .models import New, Director, Page, Teacher, UserMessages
from modeltranslation.admin import TranslationAdmin


@admin.register(New)
class NewAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'image', 'create_at')
    list_display_links = ('id', 'title', 'image', 'create_at')
    search_fields = ('id', 'title')
    filter = ('id', 'title')


@admin.register(Director)
class DirectorAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'position', 'phone_number', 'email', 'image')
    list_display_links = ('id', 'name', 'position')
    search_fields = ('id', 'name', 'position', 'phone_number')
    filter = ('id', 'position')


@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'position', 'phone_number', 'email', 'image')
    list_display_links = ('id', 'name', 'position')
    search_fields = ('id', 'name', 'position', 'phone_number')
    filter = ('id', 'position')


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display = ('id', 'title_uz', 'title_en', 'title_ru')
    list_display_links = ('id', 'title_uz', 'title_en', 'title_ru')
    search_fields = ('id', 'title_uz', 'title_en', 'title_ru')
    filter = ('id', 'title_uz', 'title_en', 'title_ru')


@admin.register(UserMessages)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'subject')
    list_display_link = ('id', 'first_name', 'last_name', 'email', 'subject')
    search_fields = ('id', 'first_name', 'last_name')
