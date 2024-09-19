#pip3 install pytest
#pytest test.py
import pytest

def func(x):
  return x + 1

#테스트 함수
def test_answer():
  assert func(4) == 5