from django import forms

class RangeForms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    amount = forms.IntegerField(initial=1, required=False, max_value=100)

class ListForms(forms.Form):
    list_random = forms.CharField(widget=forms.Textarea)
    repeat = forms.BooleanField(required=False)
    amount = forms.IntegerField(required=False, initial=1, max_value=100)

class RandomPassword(forms.Form):
    name= forms.CharField(required=False)
    year_birthday = forms.IntegerField(required=False, min_value=0)
    add_prefix = forms.CharField(required=False)

