# 1 
class Memoize():

    def __init__(self, f) -> None:
        self.f = f
        self.mapping = dict() 

    def memoized(self, x):
        if x not in self.mapping:
            self.mapping[x] = self.f(x) 
        return self.mapping[x]

def fib(n: int) -> int:
    if n <= 2: 
        return 1
    return fib(n - 1) + fib(n - 2)

# 2 
# Running Memoized(np.random.randint)
# After the first call to g.memoized(10), 
# for instance, the result is always the same

# 3
# Don't know how to use a seed in python

# 4 
# (a) The factorial is pure
# (b) std::getchar() is not pure
# (c) f() will not print "Hello!" every time it is called
# (d) Running f(1) 5 times with it not memoized will return 
# 1, 2, 3, 4, 5. Therefore it is not pure

# 5
# There are 2 * 2 functions from bool to bool. You can see it
# by thinking of the following mapping {True : x, False : y}, 
# where x, y in {True, False}. 

def always_false(x: bool) -> bool:
    return False

def always_true(x: bool) -> bool:
    return True

def identity(x: bool) -> bool:
    return x

def negation(x: bool) -> bool:
    return not x

# 6


def unit(_) -> None:
    return None
