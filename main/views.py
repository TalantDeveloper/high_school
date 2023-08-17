from django.shortcuts import render, redirect
from .models import New, Director, Page, Teacher, UserMessages


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
    news_orders = New.objects.all()
    content = {
        'news': news,
        'news_orders': news_orders,
    }
    return render(request, 'main/news.html', content)


def new_view(request, pk):  # tamom
    all_news = New.objects.all()[:6]
    new = New.objects.get(pk=pk)
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
    director = Director.objects.get(position='Ijrochi Direktor')
    zamdirectors = Director.objects.all()
    content = {
        'director': director,
        'zamdirectors': zamdirectors
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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user_message = UserMessages.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message,
        )
        user_message.save()
        return redirect('/')
    return render(request, 'main/contact_us.html')


def teacher_view(request, id):
    pass
