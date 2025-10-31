output_format = 'Décimales'

def selected_format():
    return output_format

def set_format(value: str):
    global output_format
    if value in ('Décimales', 'Fractions'):
        output_format = value

def get_format():
    return output_format
