# cross formula
def shimmy_90(t, size, down=False):
    if down:
        t.down()
    else:
        t.up()
    t.forward(size)
    t.left(90)
def square(t, size, side_value=0, end=None):
    if end == None:
        for side in range(4):
            if side % 2 == side_value:
                t.up()
            else:
                t.down()
                
            t.forward(size)
            t.left(90)
    elif end == "left":
        
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=False)
        
    elif end == "top":
        
        shimmy_90(t, size, down=False) # bottom side
        shimmy_90(t, size, down=True) # right side
        shimmy_90(t, size, down=True) # top side
        shimmy_90(t, size, down=True) # left side
        
    elif end == "right":
        
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=False)
        
    elif end == "bottom":
        
        shimmy_90(t, size, down=True) # top
        shimmy_90(t, size, down=True)
        shimmy_90(t, size, down=False) # bottom
        shimmy_90(t, size, down=True)
        
    elif end == "center":
        
        shimmy_90(t, size, down=False)
        shimmy_90(t, size, down=False)
        shimmy_90(t, size, down=False)
        shimmy_90(t, size, down=False)


def bounce_up(t, size):
    t.left(90)
    t.forward(size)
    t.right(90)
        
def cross(t, thickness=15, size=7, color="red", rotate=False):
    t.speed(0)
    t.hideturtle()

    t.begin_fill()
    t.color(color)
    size = int(size)
    
    if size < 2:
        return "Cross input size is too small."
    
    bottom = size
    top = int(size/2)
    length = int(size/2)
    
    
    #assert type(size) == int, "size only handles integer values"
    #assert height < 5, "height must be less than 5"
    #assert height > 2, "height must be greater than 2"
    # the formula is this:
    #assert top == length, "invalid cross shape"
    #assert length + top == bottom, "invalid cross shape"
    
    bottom += 1
    square(t, thickness, 0, end="bottom")
    bounce_up(t, thickness)
    
    for sq in range(bottom-2):
        square(t, thickness, 0)
        bounce_up(t, thickness)
    
    square(t, thickness, 0, end="center") # closing square
    bounce_up(t, thickness)
        
    for sq in range(length-1): # left
        square(t, -thickness, 1)
        t.forward(-thickness)
        
    square(t, -thickness, 1, end="left") # closing square
    t.forward(-thickness)
        
    t.forward(thickness*(length+1))
    bounce_up(t, -thickness)
    
    for sq in range(length-1): # right
        square(t, thickness, 1)
        t.forward(thickness)
    
    square(t, thickness, 1, end="right") # closing square
    t.forward(thickness)
    
    t.forward(-(thickness*(length+1)))
    bounce_up(t, thickness)
    
    for sq in range(top-1):
        square(t, thickness, 0)
        bounce_up(t, thickness)
    
    square(t, thickness, 0, end="top") # closing square
    bounce_up(t, thickness)
    
    
    
    
    t.end_fill()
    
    t.begin_fill()
    t.color(color)
    t.right(90)
    t.forward(top*thickness)
    square(t, thickness, 0)
    t.end_fill()
    
    if not rotate:
        t.right(-90)
    
    return f"Cross has been created with a size of {size}"
    
    
if __name__ == "__main__":
    #cross(tb, 25, 4, 2, 2)
    import turtle
    tb = turtle.Turtle()
    print(cross(tb))

    
    