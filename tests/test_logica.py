
import pytest
from src.calculadora.logica import sumar, restar

def test_sumar_positivos():
    
    assert sumar(2, 3) == 5

def test_restar_positivos():
    
    assert restar(10, 5) == 5

def test_sumar_negativos():
   
    assert sumar(-1, -1) == -2