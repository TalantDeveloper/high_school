from django.forms import ModelForm
from main.models import UserMessages


class UserMessagesForm(ModelForm):
    class Meta:
        model = UserMessages
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
