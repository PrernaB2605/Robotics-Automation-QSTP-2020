


import math # Importing math library
print ("A. Polar to Cartesian  B. Cartesian to Polar")
print ("choose your option: A or B")
option =input("enter your option") #reading the option

# Converting cartesian to polar coordinate
def polar():
    x = float(input('Enter value of x: ')) # Reading cartesian coordinates
    y = float(input('Enter value of y: '))
    radius = math.sqrt( x * x + y * y ) #Calculating Radius
    theta = math.atan(y/x) #Calculating the angle in radians
    theta = 180 * theta/math.pi # Converting theta from radian to degree

# Displaying polar coordinates
    print('Polar coordinate is: (radius = %0.2f,theta = %0.2f)' %(radius, theta))



# Converting Polar Coordinate to Cartesian Coordinates
def cartesian():
    radius = float(input('Enter radius: '))# Reading radius and angle of polar coordinate
    theta = float(input('Enter theta in degree: '))
    theta = theta * math.pi/180.0; # Converting theta from degree to radian
    x = radius * math.cos(theta) # Converting polar to cartesian coordinates
    y = radius * math.sin(theta)

# Displaying cartesian coordinates
    print('Cartesian coordinate is: (x = %0.2f, y = %0.2f)' %(x,y))

if (option == 'A'): #Conditional statement to be executed when user selects the option.
    cartesian()
else:
    polar()