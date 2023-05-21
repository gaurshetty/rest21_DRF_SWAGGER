from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeListCreateView.as_view()),
    path('<int:id>/', views.EmployeeRetrieveUpdateDestroyView.as_view()),
]
