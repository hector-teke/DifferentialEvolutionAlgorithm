import math


class ObjFunction:

    def sphere(self, vector):

        sum = 0

        for e in vector:
            sum += pow(e, 2)

        return 1 / (1 + sum)    # Inverse. Cause we wanna found the minimum

    def schwefel(self, vector):

        v1 = 4189.829   # Already multiplied for d=10
        sum = 0

        for e in vector:
            sum += e * math.sin(pow(abs(e), 0.5))

        result = v1 - sum

        return 1 / (1 + result)   # Inverse. Cause we wanna found the minimum


    def rastrigin(self, vector):

        v1 = 100    # 10 * d
        sum = 0

        for e in vector:
            sum += pow(e, 2) - 10 * math.cos(2 * math.pi * e)

        result = v1 + sum

        return 1 / (1 + result)   # Inverse. Cause we wanna found the minimum