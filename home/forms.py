from django import forms
from .models import booking

class DateInput(forms.DateInput):
    input_type='date'


class bookingform(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'
        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'p_name':"patient name",
            'p_phone':"phone",
            'p_email':"email",
            'doc_name':"name",
            'booking_date':"booking date"
        }

