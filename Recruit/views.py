import django.contrib
import django.views as djv
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .models import Anunt,CV,Angajat,Recruiter,User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.

class Index(djv.generic.ListView):
    template_name = 'index.html'
    model = Anunt
    context_object_name = 'anunturi'

class Show(djv.generic.DetailView):
    template_name = 'show_article.html'
    model = Anunt
    context_object_name = 'anunt'
    
    def get_object(self):
        anunt = Anunt.objects.get(pk=self.kwargs['id'])
        return anunt


class Register(djv.generic.CreateView):
    template_name= 'register.html'
    model = User
    fields = ['username','last_name','password','email']

    def form_valid(self, form):
        user = User.objects.create_user(username=form.data['username'],
                                        email=form.data['email'],
                                        last_name=form.data['last_name'],
                                        password=form.data['password'])
        if(form.data['role'] == 'Angajat'):
            Angajat.objects.create(user=user)
        else:
            Recruiter.objects.create(user=user)
        return redirect('/')

class Login(djv.generic.TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}
    
    def post(self, request, *args, **kwards):
        form =  AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form})


class Logout(djv.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

class AnuntView(LoginRequiredMixin, DetailView):
    template_name = 'anunt_detail.html'
    model = Anunt
    context_object_name = 'anunt'

    def get_object(self):
        anunt = Anunt.objects.get(id=self.kwargs['pk'])
        return anunt

class AnuntCreateView(LoginRequiredMixin, CreateView):
    model = Anunt
    fields = ['titlu','descriere']
    template_name = 'anunt_create.html'

    def form_valid(self, form):
        anunt = Anunt.objects.create(
            created_by=self.request.user.recruiter_profile,
            **form.cleaned_data
        )
        return redirect('/')



class AnuntEditView(LoginRequiredMixin, UpdateView):
    model = Anunt
    fields = ['descriere' , 'titlu']
    template_name = 'anunt_update.html'

    def form_valid(self, form):
        anunt = Anunt.objects.get(pk=self.kwargs['pk'])
        anunt.titlu = form.cleaned_data['titlu']
        anunt.descriere = form.cleaned_data['descriere']
        anunt.save()
        return redirect('/')

class AnuntDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "anunt_delete.html"
    model = Anunt

    def get_success_url(self):
        return redirect('/')

class AplicaTz(TemplateView):
    template_name = 'bullshit.html'