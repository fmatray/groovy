from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class PasswordChangeView(SuccessMessageMixin, views.PasswordChangeView):
    success_message = 'Success: Password was updated.'
    success_url = reverse_lazy('index')
