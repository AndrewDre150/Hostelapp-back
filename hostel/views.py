from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HostelSerializer
from .models import Hostel

# Create your views here.

class HostelView(viewsets.ModelViewSet):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all()