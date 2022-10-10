from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import Collect_data, UserListView, MainPageView

urlpatterns = [
    path("main_page/", MainPageView.as_view(), name="main_page"),
    path("collect_data/", staff_member_required(Collect_data.as_view()), name="collect_data"),
    path("userlist/", staff_member_required(UserListView.as_view()), name="userlist"),
    path("login/", LoginView.as_view())
]
