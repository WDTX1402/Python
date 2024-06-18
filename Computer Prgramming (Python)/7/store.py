if self.x - rec.x >= 0:
            x_distance = self.x - rec.x
        else:
            x_distance = rec.x - self.x

        if self.y - rec.y >= 0:
            y_distance = self.y - rec.y
        else:
            y_distance = rec.y - self.y 

        if x_distance <= (self.width - rec.width)/2 and y_distance <= (self.height - rec.height)/2:
            t.penup()
            n1 = t.xcor()
            t.goto(n1 + 100)
            t.pendown()
            t.write("Rectangle #2 is inside Rectangle #1")
        elif x_distance <= (self.width + rec.width)/2 and y_distance <= (self.height + rec.height)/2:
            t.write("Rectangle #2 overlaps Rectangle #1")
        else:
            t.write("Rectangle #2 does not overlap Rectangle #1")
            width = self.x - rec.x
            height = self.y - rec.x
            return Rectangle(self.x - self.y, width, height)