from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note

class TaskForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']