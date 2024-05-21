from django import forms

from e_mail_app.models import MailingMessage, Client, MailingSettings

WORDS_BLACKLIST = ('казино', 'криптовалюта', 'крипта', 'биржа', 'наркотики' 'бесплатно',
                   'обман', 'полиция', 'терракт')


class MailingAddForm(forms.ModelForm):

    class Meta:
        model = MailingMessage
        fields = '__all__'

    def clean_subject(self):
        cleaned_data = self.cleaned_data.get('subject')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, тема письма в списке запрещённых товаров')

        return cleaned_data

    def clean_message(self):
        cleaned_data = self.cleaned_data.get('message')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, письмо содержит в себе слова из списка'
                                        'запрещённых слов')

        return cleaned_data


class ClientAddForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, описание клиента содержит в себе слова из списка'
                                        'запрещённых слов')

        return cleaned_data


class SettingsAddForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        exclude = ('status',)

    def clean_mailing_name(self):
        cleaned_data = self.cleaned_data.get('mailing_name')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, название рассылки в списке запрещённых товаров')

        return cleaned_data
