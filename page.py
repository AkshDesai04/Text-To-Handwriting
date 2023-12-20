from PIL import Image, ImageDraw

WHITE = "white"
BLACK = "black"
RED = "red"

class Paper:
    def __init__(self, page_height = 1410, page_width = 1000, margin_left = 150, margin_right = 0, margin_top = 150, margin_bottom = 75, line_height = 35, line_gap = 0, page_color = WHITE, line_color = BLACK, margin_color = RED):
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
        self.page_color = page_color
    
    def draw_page_PIL(self, page, save = True):
        w, h = page.page_width, page.page_height

        canvas_shape = [(0, 0), (h*2, w*2)]

        left_margin_shape = [(page.margin_left, 0), (page.margin_left, page.page_height)]
        right_margin_shape = [(w - page.margin_right, 0), (w - page.margin_right, h)]
        top_margin_shape = [(0, page.margin_top), (w, page.margin_top)]
        bottom_margin_shape = [(0, h - page.margin_bottom), (w, h - page.margin_bottom)]

        # creating new Image object
        img = Image.new("RGBA", (w, h))
        
        img1 = ImageDraw.Draw(img)

        img1.rectangle(canvas_shape, fill=page.page_color)

        img1.line(left_margin_shape, width = 0, fill=page.margin_color)
        img1.line(right_margin_shape, width = 0, fill=page.margin_color)
        img1.line(top_margin_shape, width = 0, fill=page.margin_color)
        img1.line(bottom_margin_shape, width = 0, fill=page.margin_color)

        for i in range(page.margin_top + page.line_height, page.page_height - page.margin_bottom, page.line_height):
            img1.line([(0, i), (w, i)], width = 0, fill=page.line_color)
        
        if save:
            img.save("output.png")
        page.img = img

page = Paper(1410, 1000)
page.draw_page_PIL(page)