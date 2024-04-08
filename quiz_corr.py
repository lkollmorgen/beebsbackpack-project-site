from pyscript import document
from pyweb import pydom

# quiz_message = "Will calculate a corrected score after quiz/test corrections"

# pydom['div#quiz_title'].html = quiz_message


def collect_vals():
    error = False
    pydom['div#message_output'].html = ''
    input_total = document.querySelector('#total')
    input_points = document.querySelector('#points')
    total = input_total.value
    points = input_points.value

    if total=='' or points=='':
        pydom['div#message_output'].html = 'Must enter total and score'
        error = True
        return 'Please re-enter'

    total = float(input_total.value)
    points = float(input_points.value)

    if (total == 0):
        pydom['div#message_output'].html = 'Total must be above 0'
        error = True
    if points > total:
        pydom['div#message_output'].html = 'Points must not exceed total'
        error = True
    if error:
        return 'Please re-enter'
    else:
        value = calculate(total,points)
        return value

def display_calculation(event):
    value = collect_vals()
    pydom['div#calc_output'].html = value

def calculate(total,points):
    return points + 0.5*(total - points)
