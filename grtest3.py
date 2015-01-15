from graphics import *
import random
import time

def gen_random_color():
   return "#%0.2X%0.2X%0.2X" % (random.randint(1, 245), random.randint(1, 245), random.randint(1, 245))

def main():
   win = GraphWin("My Circle", 400, 400)
   
   circles = []
   count = 0 
   
   while True:
      
      #time.sleep(0.1)
      mousePos = win.checkMouse()
      if mousePos:
         
         #if count % 10 == 0 and len(circles) < 300:
         
         np = Circle(Point(mousePos.getX(), mousePos.getY()), random.randint(6, 40))
         #np = Circle(Point(random.randint(20, 380), random.randint(20, 380)), random.randint(6, 40))
         np.draw(win)
         np.setFill(gen_random_color()) #random.choice(['red', 'blue', 'green', 'yellow', "#882019"]))
         circles.append(np)
         
      for c in circles:
         mv = random.randint(0, 3)
         if mv == 0:
            c.move(0, 1)
         elif mv == 1:
            c.move(1, 0)
         elif mv == 2:
            c.move(-1, 0)
         elif mv == 3:
            c.move(0, -1)
         
      
      count += 1
      
      #~ s = raw_input("Command: ")
      #~ if s == 'quit':
         #~ break
      #~ elif s == 'move right':
         #~ c.move(10, 0)
      #~ elif s == 'move left':
         #~ c.move(-10, 0)
      
   win.close()    

main()