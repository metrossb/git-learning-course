from lib.fibonacci import *

if __name__ == "__main__":
    fib = Fibonacci()

    print "First 30 fibonacci terms."
    print fib.getTerms(terms = 30)
