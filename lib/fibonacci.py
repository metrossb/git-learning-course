class Fibonacci:

    def getTerms(self, terms = 10):
        if terms < 1:
            return []
        elif terms == 1:
            return [1]
        elif terms == 2:
            return [1, 1]
        else:
            # Implement an algorithm
            vals = [1, 1]
            for i in range(1,terms-1):
                vals.append(vals[i] + vals[i-1])
            return vals