import django.contrib.auth
import django.contrib.auth.decorators
import django.contrib.messages
import django.http
import django.shortcuts
import django.template
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView, CreateView
from accounts.forms import UserCreationForm, UserUpdateForm

from .forms import RegistrationForm


def register(request):
    context = django.template.RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            django.contrib.messages.info(request, 'Please correct errors below.')
    else:
        user_form = RegistrationForm()

    return django.shortcuts.render_to_response(
        'accounts/register.html', {'user_form': user_form, 'registered': registered}, context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = django.contrib.auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                django.contrib.auth.login(request, user)
                return django.http.HttpResponseRedirect('/')
            else:
                django.contrib.messages.info(request, 'Your account is disabled.')
        else:
            django.contrib.messages.info(request, 'Invalid Credentials.')

    return django.shortcuts.render(request, 'accounts/login.html', {})


@django.contrib.auth.decorators.login_required
def user_logout(request):
    django.contrib.auth.logout(request)
    return django.http.HttpResponseRedirect('/')


User = get_user_model()


class DetailUser(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm


class UpdateUser(UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
