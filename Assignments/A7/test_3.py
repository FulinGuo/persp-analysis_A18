from operate import operate
import pytest
def test_3():
	assert operate(3,5,'+')==8
	assert operate(3,5,'-')==-2
	assert operate(3,5,'*')==15
	assert operate(3,5,'/')==0.6
	with pytest.raises(TypeError) as typinfo:
		operate(3,5,3)
	assert typinfo.value.args[0]=='open must be a string'
	with pytest.raises(ZeroDivisionError) as zeroinfo:
		operate(3,0,'/')
	assert zeroinfo.value.args[0]=='division by zero is undefined'
	with pytest.raises(ValueError) as valinfo:
		operate(3,5,'&')
	assert valinfo.value.args[0]=="open must be one of '+','/','-', or '*'"