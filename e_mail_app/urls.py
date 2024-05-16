from django.urls import path

from e_mail_app.apps import EMailAppConfig
from e_mail_app.views import MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, \
    MailingDeleteView, ClientListView, ClientDetailView, CleintCreateView, \
    ClientUpdateView, ClientDeleteView

app_name = EMailAppConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='home'),
    path('mailing/new', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/view/<int:pk>', MailingDetailView.as_view(), name='create_mailing'),
    path('mailing/edit/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
    path('clients/', ClientListView.as_view(), name='client_home'),
    path('client/view/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/new/', CleintCreateView.as_view(), name='create_client'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete_client')
]
