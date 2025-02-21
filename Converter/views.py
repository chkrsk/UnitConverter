from django.shortcuts import render
from .forms import CalcLengthForm, CalcWeightForm, CalcTempForm
from .services import UnitConverter

# Create your views here.


def length_calc(request):

    if request.method == "POST":
        form = CalcLengthForm(request.POST)
        if form.is_valid():

            length = form.cleaned_data['length']
            unit_a = form.cleaned_data['unit_to_convert']
            unit_b = form.cleaned_data['unit_from_convert']

            res = UnitConverter.convert_length(length, unit_a, unit_b)

    else:
        res = None
        length = None
        unit_a = None
        form = CalcLengthForm()

    context = {
        'form': form,
        'length': length,
        'unit_a': unit_a,
        'res': res
    }
    return render(request, 'Converter/length_calc.html', context)


def weight_calc(request):

    if request.method == "POST":
        form = CalcWeightForm(request.POST)
        if form.is_valid():

            weight = form.cleaned_data['weight']
            unit_a = form.cleaned_data['unit_to_convert']
            unit_b = form.cleaned_data['unit_from_convert']

            res = UnitConverter.convert_weight(weight, unit_a, unit_b)

    else:
        res = None
        weight = None
        unit_a = None
        form = CalcWeightForm()

    context = {
        'form': form,
        'weight': weight,
        'unit_a': unit_a,
        'res': res
    }
    return render(request, 'Converter/weight_calc.html', context)


def temperatur_calc(request):

    if request.method == "POST":
        form = CalcTempForm(request.POST)
        if form.is_valid():

            # add constant dict with conversion
            CONVERSIONS = {
                ('C', 'F'): lambda x: (x*(9/5)) + 32,
                ('C', 'K'): lambda x: x + 273.15,
                ('C', 'R'): lambda x: (x*(9/5)) + 491,

                ('F', 'C'): lambda x: (x - 32) / 1.8,
                ('F', 'K'): lambda x: (x+495) * (5/9),
                ('C', 'R'): lambda x: x + 459.67,

                ('K', 'C'): lambda x: x - 273.15,
                ('K', 'F'): lambda x: (x * 1.8) - 459.67,
                ('K', 'R'): lambda x: (x - 273.15) + 1.8,

                ('R', 'C'): lambda x: x / 1.8,
                ('R', 'F'): lambda x: x - 459.67,
                ('R', 'K'): lambda x: x * 5/9,

            }

            temp = form.cleaned_data['temperature']
            unit_a = form.cleaned_data['unit_to_convert']
            unit_b = form.cleaned_data['unit_from_convert']

            res = temp if unit_a == unit_b else CONVERSIONS[unit_a,
                                                            unit_b](temp)

    else:
        res = None
        temp = None
        unit_a = None
        unit_b = None
        form = CalcTempForm()

    context = {
        'form': form,
        'temp': temp,
        'unit_a': unit_a,
        'unit_b': unit_b,
        'res': res
    }
    return render(request, 'Converter/temperatur_calc.html', context)
