from django.urls import path

from .views import Pollist, PollDetail

urlpatterns = [
    path('polls/', Pollist.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail')
]