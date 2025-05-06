from rest_framework import generics
from .models import Internship
from .serializers import InternshipSerializer

class InternshipCreateView(generics.CreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class InternshipListView(generics.ListAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class InternshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    lookup_field = 'id'
