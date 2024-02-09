class stul:
    def __init__(self, count, color, figure):
        self.count = count
        self.color = color
        self.figure = figure

    def __str__(self):
        return "Stul" + " " + "(" + self.count.__str__() + "," + self.color + "," + self.figure + ")"
    def __repr__(self):
        return "Stul" + " " + "(" + self.count.__str__() + "," + self.color + "," + self.figure + ")"


chair = stul(4, "Red", "comfortable")

print([chair])
