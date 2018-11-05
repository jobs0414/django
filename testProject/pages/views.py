from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from testProject.views import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def account_edit(request, account_id=None):
    user = get_object_or_404(User, pk=account_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            image = request.FILES.get('image')
            user.profile.bio = request.POST.get('bio')
            user.profile.image = image

            user.save()
            return redirect('home')
    else:
        form = ProfileForm(
            initial={
                               'username': request.user.username,
                               'image': request.user.profile.image,
                               'email': request.user.email,
                               'bio': request.user.profile.bio,
                           }
        )
    return render(request, 'account_edit.html', {'form': form})


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    # form_class = UserCreationForm
    form_class = ProfileForm

    success_url = reverse_lazy('register_done')


# --- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
