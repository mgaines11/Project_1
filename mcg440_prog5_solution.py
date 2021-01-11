'''
    Program Author:  <Matthew>
    MSU NetID: <mcg440>
    Assignment: <Program 5: Line art>

Description:
        <using the built in turtle graphical library to allow the user to drag cursor across the screen and create line art.>
'''

import turtle
import random


def trim_in_bounds(value):
	"""
			Step 4:  The parameter value should be a float. Regardless
			of the value of the parameter value, you want to return a value
			between 0 and 1.
	"""
	if value < 0.:
		return 0.
	elif value > 1.:
		return 1.
	return value

def random_offset(color):
	"""
					Step 3: Delete pass. The parameter color should be a tuple. You can access
			or unpack the RGB values from color using the following r, g, b = color.
			RGB should be float values between 0 and 1 representing how much red, green,
24.	        and blue are in the color.
25.
26.	        Once you have your r, g, b values, you need to select one of the 3 values.
27.	        Next you need to randomly create an offset. This random offset should be
28.	        between -0.1 and 0.1.  The larger the range the more drastically the colors
29.	        will change.  The smaller the range, the more subtle the color changes
30.	        will be.  Feel free to play with this range.
31.
32.	        This line of code will generate a random value between -0.1 and 0.1.
33.	        (random.random()- 0.5)/5
34.
35.	        Now that you have randomly selected a color and genrated a random offset
36.	        between -0.1 and 0.1, you need to add the offset to the randomly selected
37.	        color.  After you add the offset to the randomly selected color, set the
38.	        color equal to the function call trimInBounds with the randomly selected
39.	         color as the argument.
40.
41.	        Lastly return r, g, b
42.	    """

	r, g, b = color
	r = trim_in_bounds(r+(random.random()- 0.5/5))
	g = trim_in_bounds(g+(random.random()- 0.5/5))
	b = trim_in_bounds(b+(random.random()- 0.5/5))
	print(r, g, b)

	color = (r, g, b)

	return color

def draw_line(x1, y2):
	""""
48.	        (x1, y2) is the coordinate for where the cursor currently is.
49.	        To understand how this function works you need the imagine a box where one
50.	        corner is determined by the point (0,0) and the opposite corner is wherever
51.	        the cursor is being dragged too.
52.	        This function draws a line by
53.	            -picking the turtle's pen up
54.	            -telling the turtle to goto the point (x1, 0) which is on corner above
55.	                (0,0) and opposite the point (x1, y2)
56.	            -putting the pen back down
57.	            -telling the turtle to goto the point (0, y2) which is the point below
58.	                (x1, y2) and opposite the point (0,0)
59.	            -then pick the pen back up which is not necessary, but I think is a
60.	                good habit
61.	        .                              .(x1, y2)
62.	            .
63.	                  .
64.	                       .
65.	                            .
66.	                                  .
67.	                                          .
68.	        .(0,0)
69.
70.	        Step 1: Figure out how to draw the lines. Look into the following methods
71.	        t.up(), t.down(), and t.goto(). To run the program, click run and the
72.	        drag the circle in the middle of the turtle window around.
73.
74.	        Step 2:  Add the following two lines of code to this function.
75.	                r, g, b = random_offset1(t.color()[0])
76.	                t.color((r, g, b))
77.	    """
#cursor control
def click(x, y):
	print("you clicked on the button", x, y)
# t is a python turtle
#using defined offset function to call on rand_color as a tuple and get a float value for the color
	rand_color = (0.5, 0.5, 0.5)
	rgb = random_offset(rand_color)

	t.penup()
	t.goto(x, 0)
	t.color(rgb)
	t.pendown()
	t.goto(0, y)
	t.penup()

#specifying our t variable to the turtle library and declaring our shape as a circle
t = turtle.Turtle()
t.shape("circle")



#allowing user to drag cursor by clicking and binding that to button 1 in the on position when clicked
t.ondrag(fun=click, btn=1, add=None)

wn = turtle.Screen()
wn.listen()
wn.tracer(0)
#t.ondrag(draw_line)
wn.mainloop()
