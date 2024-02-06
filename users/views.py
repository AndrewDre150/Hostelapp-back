from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import CustomUserSerializer



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('username')  # assuming 'username' is the key for email
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Remove the automatic login after registration
            # login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


