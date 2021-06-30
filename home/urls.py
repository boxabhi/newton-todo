from django.urls import path
from .views import *

urlpatterns = [
    path('' , home),
    path('update-todo/'  , update_todo , name="update_todo"),
    path('delete-todo/<id>/' , delete_todo , name="delete_todo")

]
