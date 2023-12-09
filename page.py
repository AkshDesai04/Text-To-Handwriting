from PIL import Image, ImageDraw

BLACK = 0
RED = 10

class Paper:
    def __init__(self, page_height = 1410, page_width = 1000, margin_left = 150, margin_right = 0, margin_top = 150, margin_bottom = 75, line_height = 35, line_gap = 0, line_color = BLACK, margin_color = RED):
        self.page_height = page_height
        self.page_width = page_width
        self.margin_left = margin_left
        self.margin_right = margin_right
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom

        self.line_height = line_height
        self.line_gap = line_gap

        self.line_color = line_color
        self.margin_color = margin_color


    def draw_page(self, page):
        screen = Screen()
        cur = Turtle()
        hideturtle()

        screen.setup(1000, 1410)
        
        cur.forward(1000)

        ts = getscreen()
        ts.getcanvas().postscript(file="output.ps", colormode='color')
        Image.open("output.ps").save("output.png")

        done()