# UnitConverter

A simple Django project that allows to convert units of distance, temperature and weighth.

## Features

### Conversation:
- Distance (e.g. meters to kilometers)
- Weight (e.g. kilograms to decagram)
- Temperature (e.g. Celsius to Fahrenheit)

- Html form-based interface
- No databases usage
- No models
- No users

- Interface in Polish

## Requirements

- Python 3.x
- Django 4.x or later

## Instalation
1. **Clone the repository**
```bash
git clone https://github.com/chkrsk/UnitConverter.git
```
Extract folder ```UnitConverter```

2. **Create a virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt

pip install django
# Other required packages...
pip install dotenv # to store SECRET_KEY
```

4. **Configure project**
Set ```SECRET_KEY``` in ``settings.py``

5. **Start server**
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Select the conversion type (at the top).
2. Enter the value (only the number).
3. Choose the units.
4. Click the "Konwertuj" button.
5. You see the result, to perform another conversion click the "Resetuj" button.