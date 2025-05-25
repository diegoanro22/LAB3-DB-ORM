from rest_framework import serializers
from .models import Guest, RoomType, Room, Amenity, RoomAmenity, Reservation, Payment


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        read_only_fields = ['created_at']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)
    room_type_id = serializers.PrimaryKeyRelatedField(
        queryset=RoomType.objects.all(), source='room_type', write_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class RoomAmenitySerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), write_only=True)
    amenity = serializers.PrimaryKeyRelatedField(
        queryset=Amenity.objects.all(), write_only=True)

    class Meta:
        model = RoomAmenity
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    guest = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(), write_only=True)
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True)
    guest_details = GuestSerializer(source='guest', read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ['created_at']


class PaymentSerializer(serializers.ModelSerializer):
    reservation = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all(), write_only=True)
    reservation_details = ReservationSerializer(
        source='reservation', read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
