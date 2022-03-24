import datetime

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Customer, Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'date', 'time_slot']
        widgets = {'date': DateInput()}

    def clean(self):
        room = self.cleaned_data['room']
        date = self.cleaned_data['date']
        time_slot = self.cleaned_data['time_slot']
        if Reservation.objects.filter(date=date).filter(time_slot=time_slot).filter(room=room).exists():
            raise forms.ValidationError('Reservation already exists')
        if date <= datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past or today's date.")


class CustomerRegistrationForm(forms.ModelForm):
    # custom fields
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "address", "phone_number", "email", "username", "password", "password1"]

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError('Username already exists')
        return uname

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')

        if password != password1:
            raise forms.ValidationError("Your passwords do not match")
        return password1


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

