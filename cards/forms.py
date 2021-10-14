from django import forms

class CardForm(forms.Form):
    date_from = forms.DateField(label='Date from  ', widget = forms.TextInput(attrs={
        'type': 'date',
        
    }))
    date_to = forms.DateField(label='Date to  ', widget = forms.TextInput(attrs={
        'type': 'date'
    }))
    description = forms.CharField(label='Description  ', widget = forms.Textarea({
        'cols':'40',
        'rows':'5',
    }))

