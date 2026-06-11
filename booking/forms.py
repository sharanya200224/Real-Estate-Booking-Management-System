from django import forms

from booking.models import Agreement


class AgreementFrom(forms.ModelForm):
    class Meta:
        model = Agreement

        fields="__all__"
