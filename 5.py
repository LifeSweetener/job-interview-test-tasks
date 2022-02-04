class Screen:
    def __init__(self):  # конструктор
        self.__width = 50
        self.__height = 6
        self.__screen = [ [ '.' for j in range(self.__width) ] for i in range(self.__height) ]
    
    def __str__(self):  # строковое представление объекта при его выводе
        string = ""
        for row in self.__screen:
            for col in row:
                string += col
            string += '\n'
        
        return string
    
    def print_screen(self):  # напечатать экран
        for row in self.__screen:
            for col in row:
                print(col, end='')
            print()
    
    def rect(self, w, h):  # создать квадрат в левом верхнем углу
        for i in range(h):
            for j in range(w):
                if (w >= self.__width) or (h >= self.__height):
                    continue
                self.__screen[i][j] = '#'
    
    def rotate_row(self, row, value):  # прокрутить строку вправо
        if (row >= self.__height) or (row < 0):
            return -1
        
        r = self.__screen[row]
        for i in range(value):
            temp2 = r[0].split()
            temp2 = "".join(temp2)
            #==============================
            # Эта конструкция обеспечивает создание новой строки, а не копирование ссылки на старую:
            r[0] = r[self.__width - 1].split()
            r[0] = "".join(r[0])
            #==============================
            temp = temp2.split()
            temp = "".join(temp)
            for j in range(1, self.__width):
                temp2 = r[j].split()
                temp2 = "".join(temp2)
                
                r[j] = temp
                temp = temp2
    
    def rotate_col(self, col, value):  # прокрутить столбец вниз
        if (col >= self.__width) or (col < 0):
            return -1
        
        for i in range(value):
            temp2 = self.__screen[0][col]
            #==============================
            # Эта конструкция обеспечивает создание новой строки, а не копирование ссылки на старую:
            self.__screen[0][col] = self.__screen[self.__height-1][col].split()
            self.__screen[0][col] = "".join(self.__screen[0][col])
            #==============================
            temp = temp2
            for j in range(1, self.__height):
                temp2 = self.__screen[j][col].split()
                temp2 = "".join(temp2)
                
                self.__screen[j][col] = temp
                temp = temp2
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def screen(self):
        self.print_screen()

class Main:
    @staticmethod
    def main():
        data = ""
        try:
            file = open(r"C:\Users\User_ll\Downloads\08.txt")
            data = file.readlines()
            file.close()
        except OSError as ex:
            print(ex)
        
        screen = Screen()
        
        for cmd in data:
            if cmd.find("rect") != -1:
                x_index = cmd.find('x')
                a = int(cmd[5:x_index])
                b = int(cmd[x_index+1:cmd.find('\n')])
                screen.rect(a, b)
            elif cmd.find("rotate row") != -1:
                a = int(cmd[ (cmd.find("y=")+2) : (cmd.find("by")-1) ])
                b = int(cmd[ (cmd.find("by")+3) : (cmd.find('\n')) ])
                screen.rotate_row(a, b)
            elif cmd.find("rotate column") != -1:
                a = int(cmd[ (cmd.find("x=")+2) : (cmd.find("by")-1) ])
                b = int(cmd[ (cmd.find("by")+3) : (cmd.find('\n')) ])
                screen.rotate_col(a, b)
            
            print(screen)
        
#======================================

Main.main()