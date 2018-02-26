# File : vector.py
# Supports various vector operations
# Linear algebra library implemented as part of 
# Udacity Linear Algebra Refresher course.
# Refer : https://classroom.udacity.com/courses/ud953
# Author : @geekgirldecodes

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

###########################
# quiz 01
# Add , Subtract and
# Scalar multiplication
###########################  

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

    
###########################
# quiz 02
# Magnitude and direction
###########################

    def magnitude(self):
        # Finds magnitude of the given vector
        # magnitude(V) = sqrt(V1^2 +V2^2 + ...Vn^2)
        v_mag = 0
        for x in self.coordinates:
            print x
            v_mag = x**2+v_mag #** is operator for : raised to the power of
        return (v_mag**0.5)


    def direction(self):
        # Finds direction of the given vector
        # diection(V) = 1/magnitude(V) * V
        s = (1/self.magnitude())
        v_dir = self.scalar_multiply(s)
        return v_dir
        
        
        
