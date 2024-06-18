import turtle as t

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_center(self):
        return Point(self.x, self.y)

    def __str__(self):
        return f"Centered at ({self.x}, {self.y}) with width {self.width} and height {self.height}"

def get_x(point):
    return point.x

def get_y(point):
    return point.y

def getRectangle(points):
    min_x = min(points, key=get_x).x
    max_x = max(points, key=get_x).x
    min_y = min(points, key=get_y).y
    max_y = max(points, key=get_y).y

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y

    return Rectangle2D(center_x, center_y, width, height)


def drawRectangle(rectangle):
    topLeftX = rectangle.x - rectangle.width / 2
    topLeftY = rectangle.y + rectangle.height / 2
    t.penup()
    t.setpos(topLeftX, topLeftY)
    t.pendown()
    for _ in range(2):
        t.forward(rectangle.width)
        t.right(90)
        t.forward(rectangle.height)
        t.right(90)

def drawPoint(point):
    t.penup()
    t.setpos(point.x, point.y)
    t.pendown()
    t.dot(5)  

def main():
    points = []

    try:
        coords = list(map(float, input("Enter the points as x1 y1 x2 y2 ... : ").split()))
        points = [Point(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
    except ValueError:
        print("Invalid input. Please enter coordinates as pairs of x y.")


    screen = t.Screen()
    t.speed(0)

    if points:
        bounding_rectangle = getRectangle(points)
        print("Bounding Rectangle:")
        print(f"X: {bounding_rectangle.x}, Y: {bounding_rectangle.y}")
        print(f"Width: {bounding_rectangle.width}, Height: {bounding_rectangle.height}")

        drawRectangle(bounding_rectangle)
        for point in points:
            drawPoint(point)
        t.done()
    else:
        print("No points input.")

if __name__ == "__main__":
    main()
