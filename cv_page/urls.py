from django.urls import path, re_path

from cv_page import views

urlpatterns = [
    re_path(r'cv$', views.cv_detail, name='cv'),
    path('cv/<int:pk>/edit/', views.cv_edit, name='cv_edit'),
]
