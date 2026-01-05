from django.db import models
from django.utils import timezone

class Hostel(models.Model):
    HOSTEL_TYPE = (
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
    )
    name = models.CharField(max_length=100)
    hostel_type = models.CharField(max_length=10, choices=HOSTEL_TYPE)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPE = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
    )
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE)
    bed_capacity = models.IntegerField()
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    join_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[('pending','Pending'),('resolved','Resolved')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Visitor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)

