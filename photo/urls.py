from django.urls import path
from photo.views import index,upload

# App名称
# 用于Django幕后的url查询
app_name = 'photo'

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
]