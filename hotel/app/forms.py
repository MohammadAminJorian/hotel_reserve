from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import *

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ('start_date', 'finish_date', 'room', 'name', 'family', 'city','address','state','email','total_price')


    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        super().__init__()
        self.fields['start_date'] = JalaliDateField(label=_('start_date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        self.fields['finish_date'] = SplitJalaliDateTimeField(label=_('finish_date'),
            widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )




class LoginPhoneForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['phone']


class CodePhoneForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['verify_code']
