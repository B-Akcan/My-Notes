from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    messages.success(request, "Logged in successfully!")