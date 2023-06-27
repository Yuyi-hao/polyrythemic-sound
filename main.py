import tkinter as tk 
import math 
import time 
from playsound import playsound


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SPEED = 100

def draw_arc(canvas, radius, x, y):
  arc = canvas.create_arc(x-radius, y-radius, x+radius, y+radius, start=0, extent= 180)
  return arc

def draw_point(canvas, size, x, y, radius):
  point = canvas.create_oval(x-size, y-size, x+size, y+size, fill='pink')
  return point


def cal_pos(angle, radius):
  return (radius * math.cos(math.radians(self.angle)),
  radius * math.sin(math.radians(self.angle)))


class Ball:
  def __init__(self, ball, radius, size, speed, angle):
    self.ball = ball 
    self.radius = radius 
    self.size = size 
    self.speed = speed
    self.angular_speed = self.cal_angular_speed()
    self.angle = angle 

  def cal_angular_speed(self):
    return self.speed / self.radius

  def increment_angle(self):
    self.angle += self.angular_speed
    return self.angle

  def neg_angular_speed(self):
    self.angular_speed *= -1

  def calculate_pos(self, centerX, centerY):
      x = centerX + self.radius * math.cos(math.radians(self.angle))
      y = centerY + self.radius * math.sin(math.radians(self.angle))

      return x,y


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Polyrythemic sound")
    self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    self.vel = 2
    self.FPS = 60

    # canvas 
    self.canvas = tk.Canvas(self, bg="#bae7f7", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
    self.canvas.pack(anchor=tk.CENTER, expand=True)
    
    # canvas heigh and canvas width 
    canvas_height = WINDOW_HEIGHT
    canvas_width = WINDOW_WIDTH

    self.center_x = canvas_width // 2
    self.center_y = canvas_height //2

    # creating lines 
    canvas_center_x, canvas_center_y = canvas_width//2, canvas_height//2
    self.arcs = []
    self.balls = []
    arc_size = 30
    for i in range(13):
      radius = arc_size+(i)*20
      self.arcs.append(draw_arc(self.canvas, radius, canvas_center_x, canvas_center_y))
      ball = draw_point(self.canvas, 5, canvas_center_x-(radius), canvas_center_y, 2)
      self.balls.append(Ball(ball, radius, 5, SPEED, 180))

    self.animate()

  def animate(self):


    # Update the oval's position
    for ball in self.balls:
      x, y = ball.calculate_pos(self.center_x, self.center_y)
      ball.increment_angle()
      if ball.angle > 360 or ball.angle < 180:
        playsound('mixkit-cool-guitar-riff-2321.wav', block=False)
        ball.neg_angular_speed()
      self.canvas.coords(ball.ball, x-ball.size, y-ball.size, x+ball.size, y+ball.size)

    # Schedule the next update
    self.canvas.after(int(1000/self.FPS), self.animate)



def main():
  app = App()
  app.mainloop()




if __name__=="__main__": 
  main()