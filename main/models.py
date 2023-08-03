from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')  # translation
    image = models.ImageField(upload_to='./news/', default='/news/news.png')
    content = RichTextUploadingField(verbose_name='Content')  # translation

    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=200, verbose_name='F.I.O')
    image = models.ImageField(null=True, blank=True, upload_to='./director/', default='/director/default.png')

    email = models.EmailField(verbose_name='Email', null=True)
    phone_number = models.CharField(max_length=50)

    content = RichTextUploadingField(null=True, blank=True, verbose_name='Malumot')  # translation

    position = models.CharField(max_length=250, verbose_name='Lavozimi')  # translation

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name='F.I.O')
    image = models.ImageField(null=True, blank=True, upload_to='./director/', default='/director/default.png')

    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    content = RichTextUploadingField(null=True, blank=True, verbose_name='Malumot')  # translation
    position = models.CharField(max_length=250, verbose_name='Lavozimi', blank=True, null=True)  # translation


class Page(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')  # translation
    content = RichTextUploadingField(verbose_name='Malumot')
    page_name = models.CharField(max_length=300, verbose_name='Page Name')

    def __str__(self):
        return self.title


class UserMessages(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Ismi')
    last_name = models.CharField(max_length=100, verbose_name='Familyasi')
    email = models.EmailField(max_length=100, verbose_name='Email')
    subject = models.CharField(max_length=250, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.subject


