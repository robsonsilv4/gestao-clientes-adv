from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm


@login_required
def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})


@login_required
def pessoas_new(request):
    form = PessoaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list')
    return render(request, 'pessoa_form.html', {'form': form})


@login_required
def pessoas_update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

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
