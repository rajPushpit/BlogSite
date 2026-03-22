# User is a default user model which is created by the django in admin panel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# RegistrationForm Extends the Functionality of UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

