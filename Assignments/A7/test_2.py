from month_length import month_length
def test_2():
	assert month_length('April')==30
	assert month_length('January')==31
	assert month_length('February')==28
	assert month_length('February',leap_year=True)==29
	assert month_length(2018)==None