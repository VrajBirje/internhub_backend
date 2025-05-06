from django.urls import path
from .views import (
    ApplicationCreateView,
    ApplicationListByInternshipView,
    ApplicationListByUserView,
    ApplicationDetailView,
)

urlpatterns = [
    path('create/', ApplicationCreateView.as_view(), name='create-application'),
    path('internship/<int:internship_id>/', ApplicationListByInternshipView.as_view(), name='applications-by-internship'),
    path('user/<int:user_id>/', ApplicationListByUserView.as_view(), name='applications-by-user'),
    path('<int:id>/', ApplicationDetailView.as_view(), name='application-detail'),
]
