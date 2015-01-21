from graphics import *
import random
import time

def gen_random_color():
   return "#%0.2X%0.2X%0.2X" % (random.randint(1, 245), random.randint(1, 245), random.randint(1, 245))


def add_circle(win):
   '''Create a new circle, draw it & return it'''
   c = Circle(Point(random.randint(1, 460), 2), 30)
   c.setFill(gen_random_color())
   c.draw(win)
   return c
   
def main():
   # List of active falling circles
   circles = []

   # Initialze graphics window
   win = GraphWin("Ball Drop", 500, 660)
   
   # Create first circle & save in our active list 
   circles.append(add_circle(win))
   
   while True:
      time.sleep(0.05)

      # Keep track of any circles that have fallen off the screen here
      deleted_circles = []
      
      # Loop through all active circles. Move them all down the screen for this frame
      # If the current position of the circle is off screen, erase it & flag it
      # for deletion from the active circle list
      for idx, c in enumerate(circles):
         c.move(0, 4)
         curCenter = c.getCenter()
         if curCenter.getY() > 700:
            c.undraw()
            deleted_circles.append(idx)
            
      # Remove any circles off screen as they are out of the game play area
      for i in deleted_circles:
         del circles[i]
            
         
      # Implement the game rule that if the last dropped circle is > 300 pixels
      # from the top of the screen, we need to drop a new circle from the top
      last_circle = circles[-1]
      cCenter = last_circle.getCenter()
      addNew = False
      if cCenter.getY() > 220:
         addNew = True
            
      # Only drop a new circle if we need to & there are already less than
      # 4 circles currently active (so we don't add too many)
      if addNew and len(circles) < 4:
         circles.append(add_circle(win))
         
      # Not used
      #~ keyPress = win.checkKey()
      #~ if keyPress:
         #~ print keyPress
      

   win.close()    

main()
