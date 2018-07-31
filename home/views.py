from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel'] = 'Mensagem da variável'
        return context


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')
