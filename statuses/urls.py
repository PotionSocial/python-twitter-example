from django.urls import path
from . import views

urlpatterns = [
    path("", views.statuses_index, name="statuses_index"),
    path("create-status/", views.create_status, name="create_status"),
    path("delete-status/<str:status_id>",
         views.delete_status, name="delete_status"),
    path("like-status/<str:status_id>", views.like_status, name="like_status"),
    path("unlike-status/<str:status_id>",
         views.unlike_status, name="unlike_status"),
    path("select-user/", views.select_current_user, name="select_current_user"),
]
