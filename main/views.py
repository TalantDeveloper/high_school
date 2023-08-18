from django.shortcuts import render, redirect
from .models import New, Director, Page, Teacher, UserMessages
from .forms import UserMessagesForm
from django.contrib import messages


def welcome_view(request):
    news = New.objects.all()[:3]
    directors = Director.objects.all()
    teachers = Teacher.objects.all()[:4]
    content = {
        'news': news,
        'directors': directors,
        'teachers': teachers,
    }
    return render(request, 'main/welcome.html', content)


def news_view(request):  # tamom  # pagination qilish kerak
    news = New.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search')
        news_orders = New.objects.filter(title__icontains=search)[:12]
    else:
        news_orders = New.objects.all()[:12]
    content = {
        'news': news,
        'news_orders': news_orders,
    }
    return render(request, 'main/news.html', content)


def new_view(request, pk):  # tamom
    all_news = New.objects.all()[:6]
    new = New.objects.get(pk=pk)
    new.sees_add()
    new.likes_add()
    content = {
        'new': new,
        'news': all_news
    }
    return render(request, 'main/new.html', content)


def page_view(request, name):
    page = Page.objects.get(page_name=name)
    content = {
        'page': page,
    }
    return render(request, 'main/page.html', content)


def direktors_view(request):
    director = Director.objects.get(position_uz='Ijrochi Direktor')
    zamdirectors = Director.objects.all()

    content = {
        'director': director,
        'zamdirectors': zamdirectors[1:]
    }
    return render(request, 'main/direktor_zam.html', content)


def teachers_view(request):
    teachers = Teacher.objects.all()
    content = {
        'teachers': teachers,
    }
    return render(request, 'main/teachers.html', content)


def about_view(request):

    return render(request, 'main/about.html')


def contact_us_view(request):
    if request.method == "POST":
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.first_name} {form.last_name} your message sending :)')
            return redirect('/')
        else:
            return render(request, 'main/contact_us.html', {'form': form})
    return render(request, 'main/contact_us.html')


def teacher_view(request, id):
    pass
