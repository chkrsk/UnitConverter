from django import forms


class CalcLengthForm(forms.Form):
    units = [

        ('mm', 'milimetry'),
        ('cm', 'centymetry'),
        ('dm', 'decymetry'),
        ('m', 'metry'),
        ('km', 'kilometry')
    ]
    length = forms.FloatField(required=True, label="Długość: ")
    unit_to_convert = forms.ChoiceField(
        choices=units, required=True, initial='m', label="Przekonwertować Z: ")
    unit_from_convert = forms.ChoiceField(
        choices=units, required=True, label=" Przekonwertować NA: ")


class CalcWeightForm(forms.Form):
    units = [

        ('mg', 'miligramy'),
        ('g', 'gramy'),
        ('dag', 'dekagramy'),
        ('kg', 'kilogramy'),
        ('t', 'tonay')
    ]
    weight = forms.FloatField(required=True, label="Waga: ")
    unit_to_convert = forms.ChoiceField(
        choices=units, required=True, initial='kg', label="Przekonwertować Z: ")
    unit_from_convert = forms.ChoiceField(
        choices=units, required=True, label=" Przekonwertować NA: ")


class CalcTempForm(forms.Form):
    units = [

        ('C', 'Celsjusza'),
        ('F', 'Fahrenheita '),
        ('K', 'Kelwina'),
        ('R', 'Rankinea'),
    ]
    temperature = forms.FloatField(required=True, label="Temperatura:")
    unit_to_convert = forms.ChoiceField(
        choices=units, required=True, initial='F', label="Przekonwertować Z: ")
    unit_from_convert = forms.ChoiceField(
        choices=units, required=True, label="Przekonwertować NA: ")
