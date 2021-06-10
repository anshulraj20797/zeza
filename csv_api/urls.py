from django.urls import path
from django.urls.conf import include
from csv_api import views


urlpatterns = [
    path('csv/', views.CustomerMasterList.as_view()),
    path('csv/<int:pk>', views.CustomerMasterDetail.as_view()),
    ]