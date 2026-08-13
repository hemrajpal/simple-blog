from django.urls import path

from .views import register, post_list


urlpatterns = [
    path("register/", register),
    path("posts/", post_list),
]