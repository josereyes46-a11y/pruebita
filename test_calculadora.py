from calculadora import Calculadora

def test_add():
        calc = Calculadora() 
        assert calc.add(2, 3) == 5

def test_quit():
        calc = Calculadora() 
        assert calc.quit(10, 7) == 3

def test_times():
        calc = Calculadora() 
        assert calc.times(5, 5) == 25       