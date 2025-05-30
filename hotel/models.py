from django.db import models

# Create your models here.


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveIntegerField()
    rate_per_night = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
        ('out_of_service', 'Out of Service'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Room {self.room_number}"


class Amenity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    charge = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('room', 'amenity')


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled'),
    ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation #{self.id} - {self.guest}"


class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20)
    receipt_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.reservation}"

class VistaReservasCompletas(models.Model):
    guest_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False  # importante: no migrar esta vista
        db_table = 'vista_reservas_completas'
