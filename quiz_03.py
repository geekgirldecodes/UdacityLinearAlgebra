from vector import Vector

# Quiz 03.
# Dot product and angle between vectors

def main():
    # test dot product  
    X1 = Vector([7.887, 4.138])
    X2 = Vector([-8.802, 6.776])
    print X1.dot_product(X2)

    # test dot product  
    X1 = Vector([-5.955,-4.904,-1.874])
    X2 = Vector([-4.496,-8.755,7.103])
    print X1.dot_product(X2)

    # test angle in radians
    X1 = Vector([3.183,-7.627])
    X2 = Vector([-2.668,5.319])
    print X1.angle_between(X2)

    # test angle in degrees
    X1 = Vector([7.35,0.221,5.188])
    X2 = Vector([2.751,8.259,3.985])
    print str(X1.angle_between(X2,True))
    
if __name__ == "__main__":
    main()
