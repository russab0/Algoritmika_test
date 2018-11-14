import turtle


class Length: # Class for refference to lenght value
    def __init__(self, l):
        self.l = l

    def get(self):
        return self.l

    def set(self, l):
        self.l = l


class Draw: # Class for drawing
    # Constant for converting Russian color names to their English analogue
    RUS_ENG_COLOR = {"зеленый": "green",
                     "синий": "blue",
                     "default": "black"} 

    def get_eng_color(self, rus): # Function that returns English name of given in Russain color
        if rus in self.RUS_ENG_COLOR: # Color is defined
            return self.RUS_ENG_COLOR[rus]
        return self.RUS_ENG_COLOR["default"]

    def __init__(self, count, color):
        assert 1 <= count <= 6, "Unacceptable number of figures" 

        length = Length(150).get() # Variable that points to 150
        turtle.color(self.get_eng_color(color)) # Assigning right color

        turtle.left(30) # Initial rotation
        for i in range(count): # Loop for pointning figures `count` time
            for j in range(4): # Loop for each side of rectangle
                turtle.forward(length)
                turtle.left(90)
            turtle.right(60) # Preparing for next iteration
        turtle.exitonclick() # To prevent closing right after drawing


def main():
    ts = turtle.getscreen()
    number = int(ts.numinput("Фигуры", "Введите количество фигру: 1-6", default=6, minval=1, maxval=6)) # Reading number
    color = ts.textinput("Цвет", "Выберите цвет: синий, зеленый") # Readlng color

    Draw(number, color) 


if __name__ == "__main__": # If program exetuted directly (not imported)
    main()