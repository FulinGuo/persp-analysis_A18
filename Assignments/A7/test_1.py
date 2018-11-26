from smallest_factor import smallest_factor

def test_1():
	assert smallest_factor(2)==2
	assert smallest_factor(18)==2
	assert smallest_factor(17)==17
	assert smallest_factor(1)==1 # This test case is added in problem 2
	assert smallest_factor(8)==2