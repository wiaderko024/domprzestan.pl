from django.urls import path
from .views import post_page

urlpatterns = [
    path('<int:id>/', post_page, name='post_page'),
]
