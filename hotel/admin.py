from django.contrib import admin
from .models import Guest, RoomType, Room, Amenity, RoomAmenity, Reservation, Payment
# Register your models here.


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("created_at",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "room_type", "floor", "status")
    list_filter = ("status", "room_type", "floor")
    search_fields = ("room_number",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("guest", "room", "start_date", "end_date", "status")
    list_filter = ("status", "start_date", "end_date")
    search_fields = ("guest__first_name",
                     "guest__last_name", "room__room_number")


admin.site.register(RoomType)
admin.site.register(Amenity)
admin.site.register(RoomAmenity)
admin.site.register(Payment)
