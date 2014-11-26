class Fibonacci:

    def getTerms(self, terms = 10):
        f1 = 1
        f2 = 1
        if terms < 1:
            return []
        elif terms == 1:
            return [f1]
        elif terms == 2:
            return [f1, f2]
        else:
            # Implement an algorithm
            return []
