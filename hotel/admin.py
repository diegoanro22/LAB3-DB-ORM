from django.contrib import admin
from .models import Guest, RoomType, Room, Amenity, RoomAmenity, Reservation, Payment
# Register your models here.
admin.site.register(Guest)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(RoomAmenity)
admin.site.register(Reservation)
admin.site.register(Payment)
