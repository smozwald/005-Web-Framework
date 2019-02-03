from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>/', views.article, name = 'article'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]