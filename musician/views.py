from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .import forms
from .import models
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class home(ListView):
    model=models.Album
    template_name='home.html'
    context_object_name='albums'
    

#User registrations
class register_user(CreateView):
    model=User
    form_class=forms.register_form
    template_name='register.html'
    success_url=reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Registration"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Registration Successfully")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)
    
#user login
class login_user(LoginView):
    template_name='register.html'
    success_url=reverse_lazy('home')
    def get_success_url(self):
        return self.success_url
    
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context 
    
    def form_valid(self,form):
        messages.success(self.request,"Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)

#User Logout
def logout(request):
    auth.logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('login')

#Add Musicians
class add_musician(LoginRequiredMixin,CreateView):
    model=models.Musicians
    form_class=forms.musician_form
    template_name='register.html'
    success_url=reverse_lazy('home')
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] ="Add Musician" 
        return context
    def form_valid(self,form):
        messages.success(self.request,"Musician Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)
    
#add Album
class add_album(LoginRequiredMixin,CreateView):
    model=models.Album
    form_class=forms.album_form
    template_name='register.html'
    success_url=reverse_lazy('home')
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] ="Add Album" 
        return context
    def form_valid(self,form):
        messages.success(self.request,"Album Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)
    
#edit album
class edit_album(LoginRequiredMixin,UpdateView):
    model = models.Album
    class_form=forms.album_form
    fields='__all__'
    template_name = "register.html"
    pk_url_kwarg='pk'
    success_url=reverse_lazy('home')
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] ="Album Edit" 
        return context
    def form_valid(self,form):
        messages.success(self.request,"Album Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)

class delete_album(DeleteView):
    model=models.Album
    template_name='delete.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        messages.success(self.request,"Album Delete Successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Something went wrong. Please Try Again")
        return super().form_invalid(form)