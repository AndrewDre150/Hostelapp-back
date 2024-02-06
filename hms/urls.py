from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hostel import views as hostel_views
from booking import views as booking_views
from users.views import CustomUserViewSet, login_user, register_user
from django.conf import settings
from django.conf.urls.static import static 

router = routers.DefaultRouter()
router.register(r'hostels', hostel_views.HostelView, 'hostels')
router.register(r'bookings', booking_views.BookingView, 'booking') 
router.register(r'custom-users', CustomUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', login_user, name='login_user'),
    path('api/register/', register_user, name='register_user'),  # Fix here: use register_user view for registration
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
