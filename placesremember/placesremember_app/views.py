from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from placesremember_app.forms import AddPlaceForm, LoginUserForm, RegisterUserForm
from placesremember_app.models import Place
from placesremember_app.utils import DataMixin

menu = [
    {'title': 'Main Page', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
]


class Home(DataMixin, ListView):
    """View class to display authorized user places"""
    model = Place
    template_name = 'index.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.filter(user_id=self.request.user.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = self.get_user_context(title='Main Page', user_id=1)
        return dict(list(context.items()) + list(user_data.items()))


def about(request):
    """About site page"""
    return render(request, 'about.html', {'menu': menu, 'title': 'About'})


class AddPlace(LoginRequiredMixin, DataMixin, CreateView):
    """View class to create new place by authorized user"""
    form_class = AddPlaceForm
    template_name = 'add_place.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = self.get_user_context(title='Add Place')
        return dict(list(context.items()) + list(user_data.items()))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super(AddPlace, self).form_valid(form)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = self.get_user_context(title='Sign In')
        return dict(list(context.items()) + list(user_data.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    """View class to sign ip new user"""
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = self.get_user_context(title='Sign Up')
        return dict(list(context.items()) + list(user_data.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowPlace(DataMixin, DetailView):
    """View class that shows selected note"""
    model = Place
    template_name = 'showplace.html'
    pk_url_kwarg = 'place_id'
    context_object_name = 'place'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        place_data = self.get_user_context(title=context['place'])
        return dict(list(context.items()) + list(place_data.items()))


def logout_user(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
