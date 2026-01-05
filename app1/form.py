from django import forms

from app1.models import Hostel,Student,Room,Complaint,Visitor,Payment

class hostel_form(forms.ModelForm):
    class Meta:
        model=Hostel
        fields='__all__'

class student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class room_form(forms.ModelForm):
    class Meta:
        model=Room
        fields='__all__'

class complaint_form(forms.ModelForm):
    class Meta:
        model=Complaint
        fields='__all__'

class visitor_form(forms.ModelForm):
    class Meta:
        model=Visitor
        fields='__all__'

class payment_form(forms.ModelForm):
    class Meta:
        model=Payment
        fields='__all__'