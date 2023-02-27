from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime

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

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='ilya.mikhassik@yandex.ru',
            recipient_list=['imikhassik@gmail.com']
        )

        return redirect('appointments:make_appointment')
