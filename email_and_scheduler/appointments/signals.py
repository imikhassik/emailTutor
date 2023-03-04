from django.db.models.signals import post_save, post_delete
from django.core.mail import mail_managers
from django.dispatch import receiver

from .models import Appointment


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )


@receiver(post_delete, sender=Appointment)
def notify_managers_delete(sender, instance, **kwargs):
    mail_managers(
        subject=f'Appointment for {instance.client_name} on {instance.date.strftime("%d %m %Y")} has been deleted',
        message=instance.message
    )
