class Rectangle:

    def __init__(self, width, height) :
        self.width = width
        self.height = height
    
    def set_width(self, width) :
        self.width = width
    
    def set_height(self, height) :
        self.height = height

    def get_area(self) :
        return (self.width * self.height)

    def get_perimeter(self) :
        return (2*(self.width+self.height))

    def get_diagonal(self) :
        return ((self.width**2 + self.height**2)**0.5)
    
    def get_picture(self) :
        if self.width>50 or self.height>50 :
            return ("Too big for picture.")
        picture = '*'*self.width + "\n"
        picture = picture*self.height
        return picture
    def get_amount_inside(self, shape) :
        fitted_shape = 0
        con_height = self.height
        while con_height>=shape.height and self.width>=shape.width :
            con_height-=shape.height
            fitted_shape = fitted_shape + (self.width//shape.width)
        return fitted_shape

    def __str__(self) :
        return ("Rectangle(width={}, height={})".format(self.width, self.height))



class Square(Rectangle):
    
    def __init__(self, side) :
        super().__init__(side, side)

    def set_side(self, side) :
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self) :
        return ("Square(side={})".format(self.width))