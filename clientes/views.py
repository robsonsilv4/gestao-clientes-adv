from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Pessoa
from produtos.models import Produto
from .forms import PessoaForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import JsonResponse
from django.forms import model_to_dict


class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Bem-vindo ao seu primeiro acesso!'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Você já acessou essa página.'

        return context


class PessoaDetail(LoginRequiredMixin, DetailView):
    model = Pessoa

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Pessoa.objects.select_related('num_doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PessoCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = [
        'first_name',
        'last_name',
        'age',
        'salary',
        'bio',
        'photo'
    ]
    success_url = '/clientes/pessoa_list/'


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = [
        'first_name',
        'last_name',
        'age',
        'salary',
        'bio',
        'photo'
    ]

    # success_url = reverse_lazy('pessoacbv_list')
    def get_success_url(self):
        return reverse_lazy('pessoacbv_list')


class PessoaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes',)
    model = Pessoa
    success_url = reverse_lazy('pessoacbv_list')


class ProdutoBulk(View):
    def get(self, request):
        produtos = [
            'Banana',
            'Maça',
            'Pera',
            'Abacaxi',
            'Laranja',
            'Maracujá',
            'Limão',
            'Acerola'
        ]

        lista_produtos = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            lista_produtos.append(p)

        Produto.objects.bulk_create(lista_produtos)

        return HttpResponse('Lista adicionada com sucesso')


@login_required
def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    # pessoas = Pessoa.objects.filter(id=100)
    return render(request, 'person.html', {'pessoas': pessoas})


@login_required
def pessoas_new(request):
    if not request.user.has_perm('clientes.add_pessoa'):
        return HttpResponse('Não autorizado!')
    elif not request.user.is_superuser:
        return HttpResponse('Não é superusuario')

    form = PessoaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list')
    return render(request, 'pessoa_form.html', {'form': form})


@login_required
def pessoas_update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(
        request.POST or None,
        request.FILES or None,
        instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('pessoa_list')

    return render(request, 'pessoa_form.html', {'form': form})


@login_required
def pessoas_delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa_list')

    return render(request, 'pessoa_delete_confirm.html', {'pessoa': pessoa})


def api(request):
    a = {'nome': 'Robson', 'idade': 22, 'profissao': 'Dev'}
    mensagem = {'mensagem': 'Erro 404'}

    produto = Produto.objects.last()
    b = model_to_dict(produto)

    produtos = Produto.objects.all()
    l = []
    for produto in produtos:
        l.append(model_to_dict(produto))

    # return JsonResponse(mensagem, status=404)
    return JsonResponse(l, safe=False)
