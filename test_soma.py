import pytest
from soma import soma

def test_soma():
	assert soma(1,2)== 3
	assert soma('1','3')==4
	assert soma('2',4)==6
	assert soma(5)==10
	assert soma('7')==14
	assert soma('um')==False	
	assert soma('-1')==-2
	assert soma(-1, '-2')==-3
	assert soma(15.2,'-7.1')==8.1
	assert soma(7.2,'j')== False
