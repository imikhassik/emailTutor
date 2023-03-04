from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import mail_managers
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Appointment


class AppointmentView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        return redirect('appointments:make_appointment')
