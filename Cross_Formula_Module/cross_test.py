import cross_formula
import turtle
t = turtle.Turtle()

for amount in range(4):
    print(cross_formula.cross(t, thickness=12, size=5, color="black", rotate=True))