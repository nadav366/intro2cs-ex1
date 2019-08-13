##############################################################################
# FILE: hello_turtle.py
# WRITER: Nadav Har-Tuv , nadav366 , 205457534
# EXERCISE: intro2cs1 ex1 20118-2019
# DESCRIPTION: A program that draws three flowers next to each other.
##############################################################################
import turtle


def draw_petal():
    """ This function draws a single petal """
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)
    return


def draw_flower():
    """ This function draws a single flower
    Drawing four petals, in a quarter-circle space"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    # Drawing a stalk for the flower
    turtle.forward(250)
    return


def draw_flower_advance():
    """ This function draws a single flower
    and put the marker in place, to draw another flower """
    # Drawing the flower
    draw_flower()
    # Lifting the head
    turtle.up()
    # Move the cursor
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    # Returning the head
    turtle.down()
    return


def draw_flower_bed():
    """ This function draws three flowers """
    # Place the cursor in place, without drawing
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    # Drawing three flowers
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()


if __name__ == "__main__":
    """ This main function draws three flowers. """
    draw_flower_bed()
    turtle.done()
