## 
## For documentation on this library see: 
##   http://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html
##
## 

from graphics import *

def main():
   win = GraphWin("My Circle", 100, 100)
   c = Circle(Point(50,50), 10)
   c.draw(win)
   
   while True:
      s = raw_input("Command: ")
      if s == 'quit':
         break
      elif s == 'move right':
         c.move(10, 0)
      elif s == 'move left':
         c.move(-10, 0)
      
   win.close()    

main()