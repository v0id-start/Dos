class Card:
    # Number and color
    # Draw 2 color
    # Draw 4 wild
    # Wild
    # Switch, color

    def __init__(self, t=None, c=None, n=None):
        self.type = t
        self.color = c
        self.number = n


    def __str__(self):
        out = ""
        if self.type == "skip" or self.type == "draw_two" or self.type == "reverse":
            out += "%s %s" % (self.color, self.type)
        elif self.type == "draw_four" or self.type == "wild":
            out += self.type
        else:
            out += "%s %s" % (self.color, self.number)
        return out