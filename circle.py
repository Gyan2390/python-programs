class Circle:
    def __init__(self, radius):
        self.radius = radius
        # self.area = area

    # @property
    # def radius(self):
    #     return self._radius
    #
    # # @radius.setter
    # def radius(self, value):
    #     self._radius = value

    def area(self):
        pi = 3.141592653589793
        # return 3.14 * self.radius * self.radius
        return pi*self.radius**2

    # def display(self):
    #     print(f'area : {self.area}')

    # def print_area(self):
    #     pi = 3.141592653589793
    #     area = pi * (self.radius ** 2)
    #     print(f"The area of the circle is {area}")

r= int(input("radius of circle: "))
obj = Circle(r)
# circle.radius(4)
area= obj.area()
print(f'area = {area}')
# obj.display()









# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError("Radius cannot be negative")
#         self._radius = value
#
#     def area(self):
#         pi = 3.141592653589793  # Using a fixed value of pi
#         return pi * (self.radius ** 2)
#
# # Example usage:
# circle = Circle(5)
# print(f"Radius: {circle.radius}")
# print(f"Area: {circle.area()}")


# import math
#
#
# class circle():
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# r = int(input("Enter radius of circle: "))
# obj = circle(r)
# print("Area of circle:", round(obj.area(), 2))
# print("Perimeter of circle:", round(obj.perimeter(), 2))