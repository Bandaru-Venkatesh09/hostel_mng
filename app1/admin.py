from django.contrib import admin
from app1.models import Room,Hostel,Student,Complaint,Visitor,Payment

class hostel_admin(admin.ModelAdmin):
    list_display=['HOSTEL_TYPE','name']
admin.site.register(Hostel,hostel_admin)

class room_admin(admin.ModelAdmin):
    list_display=['ROOM_TYPE','hostel','room_number','room_type','bed_capacity','rent','is_available']
admin.site.register(Room,room_admin)

class student_admin(admin.ModelAdmin):
    list_display=['name','roll_number','room','join_date']
admin.site.register(Student,student_admin)

class complaint_admin(admin.ModelAdmin):
    list_display=['student','subject','message','status','created_at']
admin.site.register(Complaint,complaint_admin)

class visitor_admin(admin.ModelAdmin):
    list_display=['student','visitor_name','relation','entry_time','exit_time','approved']
admin.site.register(Visitor,visitor_admin)

class payment_admin(admin.ModelAdmin):
    list_display=['student','amount','month','paid','paid_date']
admin.site.register(Payment,payment_admin)