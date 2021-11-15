from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm, forms.ModelForm):
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'grupo']
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if(User.objects.filter(email=e).exists()):
            raise ValidationError("O email digitado já está em uso!")

        return e

