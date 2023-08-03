from .models import New, Director, Page, Teacher
from modeltranslation.translator import TranslationOptions, register


@register(New)
class NewTranslationOption(TranslationOptions):
    fields = ('title', 'content')


@register(Director)
class DirectorTranslationOption(TranslationOptions):
    fields = ('content', 'position')


@register(Teacher)
class TeacherTranslationOption(TranslationOptions):
    fields = ('content', 'position')

@register(Page)
class PageTranslationOption(TranslationOptions):
    fields = ('title', 'content')


