from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm, AgendaForm
from core.models import Agenda

def login(request):
    if request.user.id is not None:
        return redirect("home")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        return render(request, 'login.html', {'form': form, 'acesso_negado': True})

    return render(request, 'login.html', {'form': LoginForm()})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    contatos = Agenda.objects.filter(user=request.user)
    return render(request, 'index.html', {'contatos': contatos})


@login_required
def listar_contatos(request):
    contatos = Agenda.objects.filter(user=request.user)
    return render(request, 'listar_contatos.html', {'contatos': contatos})


@login_required
def adicionar_contato(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.user = request.user  # associa ao usuário logado
            contato.save()
            return redirect('listar_contatos')
    else:
        form = AgendaForm()
    return render(request, 'adicionar_contato.html', {'form': form})


@login_required
def editar_contato(request, id):
    contato = get_object_or_404(Agenda, id=id, user=request.user)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')
    else:
        form = AgendaForm(instance=contato)
    return render(request, 'editar_contato.html', {'form': form, 'contato': contato})


@login_required
def excluir_contato(request, id):
    contato = get_object_or_404(Agenda, id=id, user=request.user)
    if request.method == 'POST':
        contato.delete()
        return redirect('listar_contatos')
    return render(request, 'excluir_contato.html', {'contato': contato})
