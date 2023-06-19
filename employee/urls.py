from django.urls import path
from employee import views


urlpatterns = [
    path('', views.EmployeeView.as_view(), name='employee'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
]