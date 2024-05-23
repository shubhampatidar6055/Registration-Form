from django.urls import path
from .views import *

urlpatterns = [
    path("",registration),
    path("create_user/",create_user),
    path("table/",table),
    path("delete_user/<int:pk>/", delete_user, name="delete"),
    path("update_user/<int:uid>/", update_user, name="update"),
    path("update_data/",update_data),
]
