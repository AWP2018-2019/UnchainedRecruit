import django.contrib
import django.views as djv
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .models import Anunt,CV,Angajat,Recruiter,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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
        import pdb; pdb.set_trace()
        '''data = form.cleaned_data'''
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