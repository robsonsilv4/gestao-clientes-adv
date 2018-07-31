from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.views import View


class HomePageView(TemplateView):
    template_name = 'home/home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel'] = 'Mensagem da variável'
        return context


class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home4.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Verbo POST')


def home(request):
    return render(request, 'home/home.html')


def my_logout(request):
    logout(request)
    return redirect('home')
