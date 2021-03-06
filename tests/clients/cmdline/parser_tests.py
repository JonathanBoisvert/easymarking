# import nose
# from clients.cmdline.parser import is_integer_or_float

# def test_is_integer_or_float_returns_true_for_integers():
# 	assert True == is_integer_or_float(0)
# 	assert True == is_integer_or_float(1)
# 	assert True == is_integer_or_float(2)
# 	assert True == is_integer_or_float(10)
# 	assert True == is_integer_or_float(50)
# 	assert True == is_integer_or_float(50L)
# 	assert True == is_integer_or_float(1000)
# 	assert True == is_integer_or_float(91289199)
# 	assert True == is_integer_or_float(98172817381731827817219378189121312)
# 	assert True == is_integer_or_float(-1)
# 	assert True == is_integer_or_float(-2)
# 	assert True == is_integer_or_float(-10)
# 	assert True == is_integer_or_float(-10L)
# 	assert True == is_integer_or_float(-50)
# 	assert True == is_integer_or_float(-728172)
# 	assert True == is_integer_or_float(-1189278128127819721982879182971789)
# 	assert True == is_integer_or_float(-0)

# def test_is_integer_or_float_returns_true_for_floats():
# 	assert True == is_integer_or_float(0.0)
# 	assert True == is_integer_or_float(0.1)
# 	assert True == is_integer_or_float(0.5)
# 	assert True == is_integer_or_float(0.9)
# 	assert True == is_integer_or_float(1.0)
# 	assert True == is_integer_or_float(100.090908)
# 	assert True == is_integer_or_float(0.91291781381723717283)
# 	assert True == is_integer_or_float(10.5)
# 	assert True == is_integer_or_float(-0.0)
# 	assert True == is_integer_or_float(-0.1)
# 	assert True == is_integer_or_float(-0.2)
# 	assert True == is_integer_or_float(-0.5)
# 	assert True == is_integer_or_float(-0.9)
# 	assert True == is_integer_or_float(-1.0)
# 	assert True == is_integer_or_float(-100.877878332)
# 	assert True == is_integer_or_float(-00023.23)
# 	assert True == is_integer_or_float(-100.71638176381736183761876)
# 	assert True == is_integer_or_float(-10.5)

# def test_is_integer_or_float_returns_true_for_strings():
# 	assert True == is_integer_or_float('0')
# 	assert True == is_integer_or_float('1')
# 	assert True == is_integer_or_float('10')
# 	assert True == is_integer_or_float('10098932839293923989238923892')
# 	assert True == is_integer_or_float('-1')
# 	assert True == is_integer_or_float('-10')
# 	assert True == is_integer_or_float('-13726784636287462387462386487234')
# 	assert True == is_integer_or_float('0.0')
# 	assert True == is_integer_or_float('0.12')
# 	assert True == is_integer_or_float('10.5')
# 	assert True == is_integer_or_float('-0.1')
# 	assert True == is_integer_or_float('-0.12')
# 	assert True == is_integer_or_float('-10.5')		
# 	assert True == is_integer_or_float('12.')
# 	assert True == is_integer_or_float('.12')	

# def test_is_integer_or_float_returns_false():
# 	assert False == is_integer_or_float('')
# 	assert False == is_integer_or_float('a')
# 	assert False == is_integer_or_float('z')
# 	assert False == is_integer_or_float('hauhsa')
# 	assert False == is_integer_or_float('HAUshAUShusaushuAHSUA')
# 	assert False == is_integer_or_float('HAHAHUO(')
# 	assert False == is_integer_or_float(',<.>/?\'"]}[{=+-09897`')
# 	assert False == is_integer_or_float('12a')
# 	assert False == is_integer_or_float('12asadfasd')
# 	assert False == is_integer_or_float('h12')
# 	assert False == is_integer_or_float('hauhsuas12')
# 	assert False == is_integer_or_float('.12.')
# 	assert False == is_integer_or_float('12.0.0')
