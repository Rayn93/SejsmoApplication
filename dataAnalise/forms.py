from django import forms

class InputDataForAnalysis(forms.Form):
    deltaT = forms.IntegerField(label='Przedział czasu (w miesiącach)', min_value=1)
    mth = forms.FloatField(label='Magnituda teoretyczna', max_value=5, min_value=2)
