from pyscript import document
from pyweb import pydom


def combine_atoms(event):
    input1 = document.querySelector('#atom1')
    input2 = document.querySelector('#atom2')
    atom1 = input1.value
    atom2 = input2.value
    output_div = document.querySelector('#atom_output')
    output_div.innerText= atom1 + atom2