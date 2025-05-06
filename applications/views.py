from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationListByInternshipView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        internship_id = self.kwargs['internship_id']
        return Application.objects.filter(internship_id=internship_id)

class ApplicationListByUserView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Application.objects.filter(user_id=user_id)

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'id'
