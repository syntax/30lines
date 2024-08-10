import turtle
def draw_triangle(points, color):
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.begin_fill()
    for i in range(1, 4):
        turtle.goto(points[i % 3])
    turtle.end_fill()
def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
def sierpinski_triangle(points, order):
    if order == 0:
        draw_triangle(points, 'blue')
    else:
        mid1 = midpoint(points[0], points[1])
        mid2 = midpoint(points[1], points[2])
        mid3 = midpoint(points[2], points[0])
        sierpinski_triangle([points[0], mid1, mid3], order - 1)
        sierpinski_triangle([mid1, points[1], mid2], order - 1)
        sierpinski_triangle([mid3, mid2, points[2]], order - 1)
def main():
    turtle.speed(0)
    points = [(-200, -100), (0, 200), (200, -100)]
    sierpinski_triangle(points, 5)
    turtle.hideturtle()
    turtle.done()
if __name__ == "__main__":
    main()