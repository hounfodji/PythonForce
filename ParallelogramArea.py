breadth = int(input("Enter the parallelogram's breadth: "))
heigth  = int( input("Enter the parallelogram's heigth: "))

if(breadth<=0 or heigth<=0) :
    print("Breadth and height must be positive")
else :
    if(breadth<=100 and heigth<=100) : 
        area = breadth*heigth
        print("The parallelogram's area is: " + str(area))
