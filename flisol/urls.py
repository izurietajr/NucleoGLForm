
from django.conf.urls import url
from flisol.views import PersonView, ThankYouView

urlpatterns = [
    url(r'^registro/', PersonView.as_view(), name='registry'),
    url(r'^gracias/', ThankYouView.as_view(), name='thank_you'),
]
