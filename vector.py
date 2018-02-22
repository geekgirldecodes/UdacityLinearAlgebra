# File : vector.py
# Implements vector operations, supports v_sum(), v_diff(), s_product()


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self,v):
        # Find the sum of two vectors 
        # using zip() takes two equal length collections and
        # merges them together in "pairs"
        # Also, using the List comprehensions in Python -
        # a concise way to create lists in Python, always returns a List
        v_sum = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(v_sum)
        
    def subtract(self,v):
        # find the difference between two vectors
        v_diff = [x-y for (x,y) in zip(self.coordinates, v.coordinates)]
        return Vector(v_diff)

    def scalar_multiply(self, s):
        #find the scalar product of vetcor and scalar passed
        s_prod = [s*x for x in self.coordinates]
        return Vector(s_prod)

