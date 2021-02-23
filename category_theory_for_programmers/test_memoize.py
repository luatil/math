from memoize import fib, Memoize

def test_fib():
    assert fib(5) == 5
    assert fib(7) == 13

def test_fib_memoized():
    fib_memoized = Memoize(fib)
    assert fib_memoized.memoized(10) == 55
    assert fib_memoized.memoized(35) == 9227465