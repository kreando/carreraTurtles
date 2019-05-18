import turtle
import random
class Circuito():
    corredores=[]
    __posStartY=(-30, -10, 10, 30)
    __colorTurtle=("red", "blue", "green", "orange")
    
    def __init__(self, width, height):
        self.__screen=turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine= -width/2+(width*0.05)
        self.__finishLine= width/2-(width*0.04)
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle=turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)

    def competir(self):
        hayGanador=False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.pos()[0] >= self.__finishLine:
                    hayGanador=True
                    return print("\nla tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    #en lugar de return que compi sugirió, ramon puso break debajo
                    #break
if __name__=="__main__":
    circuito=Circuito(640, 480)
    print(circuito.corredores[2].pos())
    print(circuito.corredores[2].pos()[0])
    print(circuito.corredores[2].pos()[1])
    print(circuito.corredores[2].color())
    circuito.competir()
    