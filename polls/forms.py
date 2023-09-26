from django import forms

#importar o model "User" padrão para usuários
from django.contrib.auth import get_user_model
User = get_user_model()

#criar forms django personalizado
class AccountSignupForm(forms.ModelForm):
    password = forms.CharField(
                    label="Senha", 
                    max_length=50,
                    widget=forms.PasswordInput())
    class Meta:
        model = User # conecta o form com o model padrão de usuário
        fields = ('username', 'email', 'password', ) # campos do model a exibir
