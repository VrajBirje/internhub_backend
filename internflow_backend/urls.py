from django.contrib import admin
from django.urls import path,include
from users.views import RegisterUserView,LoginView  # make sure this import exists


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('internships/', include('internships.urls')),
    path('applications/', include('applications.urls')),
    # path('users/', views.UserListView.as_view(), name='user-list'),
    # path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
]
