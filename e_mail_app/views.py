from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from e_mail_app.forms import MailingAddForm, ClientAddForm, SettingsAddForm
from e_mail_app.models import MailingMessage, Client, MailingSettings


# Create your views here.

class MailingListView(ListView):
    model = MailingMessage
    template_name = 'e_mail_app/e_mail_list.html'
    context_object_name = 'objects_list'


class MailingCreateView(CreateView):
    model = MailingMessage
    template_name = 'e_mail_app/e_mail_form.html'
    form_class = MailingAddForm
    success_url = reverse_lazy('e_mail_app:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        settings_form_set = inlineformset_factory(MailingMessage, MailingSettings, form=SettingsAddForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = settings_form_set(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = settings_form_set(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = MailingMessage
    template_name = 'e_mail_app/e_mail_app_detail.html'
    context_object_name = 'objects_list'


class MailingUpdateView(UpdateView):
    model = MailingMessage
    template_name = 'e_mail_app/e_mail_update_form.html'
    form_class = MailingAddForm
    success_url = reverse_lazy('e_mail_app:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        settings_form_set = inlineformset_factory(MailingMessage, MailingSettings, form=SettingsAddForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = settings_form_set(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = settings_form_set(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'e_mail_app/e_mail_app_confirm_delete.html'
    success_url = reverse_lazy('e_mail_app:home')


def settings_toggle_active(request, pk):
    mailing_item = get_object_or_404(MailingSettings, pk=pk)
    if mailing_item.is_active:
        mailing_item.is_active = False
    else:
        mailing_item.is_active = True

    return redirect(reverse('e_mail_app:home'))


class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    context_object_name = 'objects_list'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/clients_detail.html'
    context_object_name = 'objects_list'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/clients_form.html'
    form_class = ClientAddForm
    success_url = reverse_lazy('e_mail_app:client_home')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/clients_update_form.html'
    form_class = ClientAddForm
    success_url = reverse_lazy('e_mail_app:client_home')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/clients_confirm_delete.html'
    success_url = reverse_lazy('e_mail_app:client_home')


class SettingsListView(ListView):
    model = MailingSettings
    template_name = 'mail_settings/settings_list.html'
    context_object_name = 'objects_list'


class SettingsDetailView(DetailView):
    model = MailingSettings
    template_name = 'mail_settings/settings_detail.html'
    context_object_name = 'objects_list'


class SettingsCreateView(CreateView):
    model = MailingSettings
    template_name = 'mail_settings/settings_add_form.html'
    form_class = SettingsAddForm
    success_url = reverse_lazy('e_mail_app:settings_home')


class SettingsUpdateView(UpdateView):
    model = MailingSettings
    template_name = 'mail_settings/settings_update_form.html'
    form_class = SettingsAddForm
    success_url = reverse_lazy('e_mail_app:settings_home')


class SettingsDeleteView(DeleteView):
    model = MailingSettings
    template_name = 'mail_settings/settings_confirm_delete.html'
    success_url = reverse_lazy('e_mail_app:settings_home')
