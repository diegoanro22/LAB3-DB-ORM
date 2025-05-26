from django.urls import path, include
from rest_framework import routers
from hotel import views


router = routers.DefaultRouter()
router.register(r'guests', views.GuestViewSet)
router.register(r'room-types', views.RoomTypeViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'amenities', views.AmenityViewSet)
router.register(r'room-amenities', views.RoomAmenityViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
