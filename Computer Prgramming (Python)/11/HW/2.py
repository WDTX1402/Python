import turtle
import math


def RobotBattle():
    robotList = []
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()
        
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, ": ", end="")
            robot.displayStatus()
            i += 1
        print()

        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")

        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")

            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            
            robotList.append(newRobot)
        else:
            n = int(choice)
            robotList[n].command(robotList)

        robotList = [robot for robot in robotList if robot.health > 0]

class Robot:
    def __init__(self):
        self.energy = 100
        self.health = 100
        self.x = 100
        self.y = 100

    def move(self, newX, newY):

        if self.energy > 0:
            self.x = newX
            self.y = newY
            self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - 15)
        turtle.pendown()
        turtle.circle(15)  
        turtle.penup()

    def displayStatus(self):
        print(f"x={self.x}, y={self.y}, energy={self.energy}, health={self.health}")

    def command(self, robotList):
        newX = int(input("Enter new x-coordinate for the robot: "))
        newY = int(input("Enter new y-coordinate for the robot: "))
        self.move(newX, newY)


class MedicBot(Robot):
    def draw(self):
        super().draw() 
        
        turtle.color("red")
        crossSize = 10  
 
        turtle.penup()
        turtle.goto(self.x, self.y + crossSize/2)
        turtle.pendown()
        turtle.goto(self.x, self.y - crossSize/2)

        turtle.penup()
        turtle.goto(self.x - crossSize/2, self.y)
        turtle.pendown()
        turtle.goto(self.x + crossSize/2, self.y)

        turtle.penup()
        turtle.color("black") 

    def heal(self, r):
        distance = math.sqrt((self.x - r.x)**2 + (self.y - r.y)**2)
        if self.energy >= 20 and distance <= 10:
            self.energy -= 20
            r.health += 10

    def command(self, robotList):
        action = input("Do you want to move the MedicBot or heal another robot? Enter 'move' or 'heal': ").lower()

        if action == "move":
            newX = int(input("Enter new x-coordinate for the MedicBot: "))
            newY = int(input("Enter new y-coordinate for the MedicBot: "))
            self.move(newX, newY)
        elif action == "heal":
            for i, robot in enumerate(robotList):
                print(f"{i}: Robot at x={robot.x}, y={robot.y}")
            
            target = int(input("Which robot do you want to heal? Enter the robot's number: "))
            if 0 <= target < len(robotList):
                self.heal(robotList[target])
            else:
                print("Invalid choice!")
class StrikerBot(Robot):
    def __init__(self):
        super().__init__()  
        self.missile = 5

    def draw(self):
        super().draw() 

        squareSide = 20
        diagonal = squareSide * (2**0.5)  
        
        turtle.penup()
        turtle.goto(self.x, self.y + diagonal / 2) 
        turtle.setheading(-45) 
        turtle.pendown()

        for _ in range(4):
            turtle.forward(squareSide)
            turtle.right(90)

        turtle.penup()
        turtle.setheading(0) 
        turtle.color("black") 
        
    def strike(self, r):
        distance = math.sqrt((self.x - r.x)**2 + (self.y - r.y)**2)
        if self.energy >= 20 and self.missile > 0 and distance <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50

    def displayStatus(self):
        super().displayStatus()
        print(f"missile={self.missile}")

    def command(self, robotList):
        action = input("Do you want to move the StrikerBot or strike another robot? Enter 'move' or 'strike': ").lower()

        if action == "move":
            newX = int(input("Enter new x-coordinate for the StrikerBot: "))
            newY = int(input("Enter new y-coordinate for the StrikerBot: "))
            self.move(newX, newY)
        elif action == "strike":
            for i, robot in enumerate(robotList):
                print(f"{i}: Robot at x={robot.x}, y={robot.y}")
            
            target = int(input("Which robot do you want to strike? Enter the robot's number: "))
            if 0 <= target < len(robotList):
                self.strike(robotList[target])
            else:
                print("Invalid choice!")

RobotBattle()
