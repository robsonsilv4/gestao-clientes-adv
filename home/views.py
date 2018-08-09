from django.shortcuts import render, redirect, HttpResponse, render_to_response
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
        response = render_to_response('home/home4.html')
        response.set_cookie('color', 'blue', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('Verbo POST')


def home(request):
    return render(request, 'home/home.html')


def my_logout(request):
    logout(request)
    return redirect('home')
