from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('homepage.html', views.post_list, name='post_list'),
    path('about.html', TemplateView.as_view(template_name="blog/about.html"))
    # path('cv_page.html', views.cv_page, name='CV')
]
