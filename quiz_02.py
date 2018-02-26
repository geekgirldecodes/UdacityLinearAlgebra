from vector import Vector

# Quiz 02.
# Direction and magnitude
# of a vector
# Author : @geekgirldecodes

def main():
    # test magnitude 01
    x1 = Vector([-0.221, 7.437])
    print x1.magnitude()

    #test magnitude 02
    x2 = Vector([8.813,-1.331,-6.247])
    print x2.magnitude()

    #test direction 01
    x3 = Vector([5.581,-2.136])
    print x3.direction()
               
    #test direction 02
    x4 = Vector([1.996,3.108,-4.554])
    print x4.direction()
                
if __name__ == "__main__":
    main()
