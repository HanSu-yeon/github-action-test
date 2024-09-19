#해당 코드 실행시켰을 때 테스트가 마킹되어 있는 함수일 경우 테스트 함수로 분류되고
#assert 키워드 내에 있는 이 조건문이 참이라면 테스트가 통과되고 실패라면 fail 뜨는 코드
import pytest

def func(x):
  return x + 1

#테스트 함수
def test_answer():
  assert func(3) == 5