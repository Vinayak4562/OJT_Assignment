class Circle:

    def diameter(self, radius):
        return 2*radius
    
    def area(self,radius):
        return 3.142 * (radius ** 2)
    
c= Circle()
radius = int(input("Enter the Radius: "))
print(f'Diameter is {c.diameter(radius)}')
print(f'Area is {c.area(radius)}')
