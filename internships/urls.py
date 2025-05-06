from django.urls import path
from .views import InternshipCreateView, InternshipListView, InternshipDetailView

urlpatterns = [
    path('create/', InternshipCreateView.as_view(), name='internship-create'),
    path('', InternshipListView.as_view(), name='internship-list'),
    path('<int:id>/', InternshipDetailView.as_view(), name='internship-detail'),
]
