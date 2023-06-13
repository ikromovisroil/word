from django.urls import path,include
from .views import *

urlpatterns = [
    path('create_docx', create_docx, name='create_docx'),
    path('create_docx2/', create_docx2, name='create_docx2'),
    path('create_docx3/', create_docx3, name='create_docx3'),
]