from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('news/', views.news_view, name='news'),
    path('new/<int:pk>/', views.new_view, name='new'),
    path('page/<str:name>/', views.page_view, name='page'),
    path('direktors/', views.direktors_view, name='direktors'),
    path('teachers/', views.teachers_view, name='teachers'),
    # path('teacher/<int:id>/', views.teacher_view, name='teacher'),
    path('about/', views.about_view, name='about'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
]
