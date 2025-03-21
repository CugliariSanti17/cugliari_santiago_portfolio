from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.render_post, name='blog'),
    path('<int:post_id>', views.post_detail, name='post_detail')
]