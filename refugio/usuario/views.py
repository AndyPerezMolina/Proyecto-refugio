
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView,ListView
from django.urls import reverse_lazy
from usuario.forms import RegistroForm, UserPerfil,PasswordEdit, AxesCaptchaForm
from django.contrib.auth.views import PasswordChangeView
from axes.utils import reset_request

import cv2
import os
import imutils
import numpy as np

def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')
	


class RegistroUsuario( CreateView):
	model = User
	template_name = "usuario/usuarioRegistro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('registrar_rostro')

class UsuarioPerfil(ListView):
	model = User
	template_name = "usuario/usuarioPerfil.html"
	form_class = RegistroForm


class UsuarioEditPerfil(UpdateView):
	model = User
	form_class = UserPerfil
	template_name = "usuario/usuarioActualizar.html"
	success_url = reverse_lazy('usuario_perfil')

	
class UsuarioEditContraseña(PasswordChangeView):
	form_class = PasswordEdit
	template_name = "usuario/usuarioActualizarContraseña.html"
	success_url = reverse_lazy('usuario_perfil')	



def locked_out(request):
    if request.POST:
        form = AxesCaptchaForm(request.POST)
        if form.is_valid():
            reset_request(request)
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = AxesCaptchaForm()

    return render(request, 'base/bloqueo.html', {'form': form})


