from django import forms
from cars.models import Brand

class Carform(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    value = forms.FloatField()
    plate = forms.CharField(max_length=10)
    photo = forms.ImageField()
