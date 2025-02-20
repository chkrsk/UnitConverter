from django import forms


class CalcLengthForm(forms.Form):
    units = [
        
        ('mm', 'milimetry'), 
        ('cm', 'centymetry'), 
        ('dm', 'decymetry'), 
        ('m', 'metry'),
        ('km', 'kilometry')
    ]
    length = forms.FloatField(required=True)
    unit_to_convert = forms.ChoiceField(choices=units, required=True, initial='m')
    unit_from_convert = forms.ChoiceField(choices=units, required=True)

class CalcWeightForm(forms.Form):
    units = [
        
        ('mg', 'miligramy'), 
        ('g', 'gramy'), 
        ('dag', 'dekagramy'), 
        ('kg', 'kilogramy'),
        ('t', 'tonay')
    ]
    weight = forms.FloatField(required=True)
    unit_to_convert = forms.ChoiceField(choices=units, required=True, initial='kg')
    unit_from_convert = forms.ChoiceField(choices=units, required=True)

class CalcTempForm(forms.Form):
    units = [
        
        ('C', 'Celsjusza'), 
        ('F', 'Fahrenheita '), 
        ('K', 'Kelwina'), 
        ('R', 'Rankinea'),
    ]
    temperature = forms.FloatField(required=True)
    unit_to_convert = forms.ChoiceField(choices=units, required=True, initial='F')
    unit_from_convert = forms.ChoiceField(choices=units, required=True)
