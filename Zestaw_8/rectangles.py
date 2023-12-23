from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Niepoprawne wspolrzedne")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return self.pt1

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def bottomright(self):
        return self.pt2

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return self.width * self.height

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

    def intersection(self, other):
        left = max(self.left, other.left)
        right = min(self.right, other.right)
        top = min(self.top, other.top)
        bottom = max(self.bottom, other.bottom)

        if left < right and bottom < top:
            return Rectangle(left, bottom, right, top)
        else:
            return None

    def cover(self, other):
        left = min(self.left, other.left)
        right = max(self.right, other.right)
        top = max(self.top, other.top)
        bottom = min(self.bottom, other.bottom)
        return Rectangle(left, bottom, right, top)

    def make4(self):
        cx, cy = self.center.x, self.center.y

        return (
            Rectangle(self.left, self.bottom, cx, cy),
            Rectangle(cx, self.bottom, self.right, cy),
            Rectangle(self.left, cy, cx, self.top),
            Rectangle(cx, cy, self.right, self.top)
        )
        