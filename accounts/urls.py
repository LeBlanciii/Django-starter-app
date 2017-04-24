from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
import accounts.views


urlpatterns = (
    url(r'^register', accounts.views.register, name='register'),
    url(r'^login', accounts.views.user_login, name='user_login'),
    url(r'^logout', accounts.views.user_logout, name='user_logout'),
    # url(r'^$', login_required(RedirectView.as_view(url=reverse_lazy('account_detail'), permanent=False))),
    url(r'^create/$', accounts.views.CreateUser.as_view(), name='account_create'),
    url(r'^detail/$', login_required(accounts.views.DetailUser.as_view()), name='account_detail'),
    url(r'^update/$', login_required(accounts.views.UpdateUser.as_view()), name='account_update'),
)
