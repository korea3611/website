from django.urls import path
from django.conf.urls import url
from . import views
from .views import *
from .models import Post

app_name = 'board'

urlpatterns = [
    url(r'^$', views.index),
    path('upload/', UploadView.as_view(), name='board_upload'),
    path('post/<int:pk>/',views.DetailView.as_view(), name = 'board_detail'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name = 'board_delete'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name = 'board_update'),
]