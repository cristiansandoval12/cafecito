from django.shortcuts import render
from .forms import CustomPasswordResetForm

def password_reset_view(request):
    form = CustomPasswordResetForm()
    # Otras lógicas de la vista...
    context = {
        'protocol': 'https',  # Cambia esto con el protocolo real que deseas usar (http o https).
        # 'domain': 'example.com',   # Cambia esto con el dominio real de tu sitio web.
        'uidb64': 'ABC123',  # Cambia esto con el valor real que obtienes al generar el token.
        'token': 'xyz789',   # Cambia esto con el valor real que obtienes al generar el token.
    }
    return render(request, 'auten/password-reset.html', context)
