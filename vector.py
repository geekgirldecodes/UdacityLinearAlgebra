# File : vector.py
# Supports various vector operations
# Linear algebra library implemented as part of 
# Udacity Linear Algebra Refresher course.
# Refer : https://classroom.udacity.com/courses/ud953
# Author : @geekgirldecodes

# Imports
from math import sqrt, acos, pi
from decimal import Decimal, getcontext
getcontext.prec = 30

class Vector(object):

    ATTEMPTING_ZERO_VECTOR_NORMALIZE_ERROR = "Zero vector cannot be normalized"
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            # All co-ordinates are "Decimal" instead of float/integer
            # This is needed for numerical precision to help with
            # acos computation (refer : dot product)
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        s_prod = [Decimal(s)*x for x in self.coordinates]
        return Vector(s_prod)

    
###########################
# quiz 02
# Magnitude and direction
###########################

    def magnitude(self):
        # Finds magnitude of the given vector
        # magnitude(V) = sqrt(V1^2 +V2^2 + ...Vn^2)
        v_sqr = [x**2 for x in self.coordinates] #** is operator for : raised to the power of
        return Decimal(sqrt(sum(v_sqr)))

    def direction(self):
        # Finds direction of the given vector
        # diection(V) = 1/magnitude(V) * V
        s = (1/self.magnitude())
        v_dir = self.scalar_multiply(s)
        return v_dir
        
###########################
# quiz 03
# Inner/Dot Product and
# angle between vectors
###########################        

    def normalize(self):
        try:
            mag = self.magnitude()
            return self.scalar_multiply(Decimal('1.0')/mag)
        except ZeroDivisionError:
            raise Exception(self.ATTEMPTING_ZERO_VECTOR_NORMALIZE_ERROR)

    def dot_product(self,v):
        # Compute the inner product between
        # two vectors
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
            
    def angle_between(self,v, in_degree=False):
        # Compute the angle between two vectors
        # angle_in_radians = arccos(V1/magnitude(V1) . V2/(magnitude(V2))

        try:
            V1 = self.normalize()
            V2 = v.normalize()
            # use acos() from Math library 
            angle_in_radians = acos(V1.dot_product(V2))

            if (in_degree):
                degrees_per_rad = 180./pi
                return angle_in_radians * degrees_per_rad
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.ATTEMPTING_ZERO_VECTOR_NORMALIZE_ERROR:
                raise Exception("cannot compute angle with Zero vector")
            else:
                raise e                
            
