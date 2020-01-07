import turtle

wn = turtle.Screen()

def test():
  pass


def createPong(pos:int, shapesize:bool = True):
  p = turtle.Turtle()
  p.speed(0)
  p.shape('square')
  p.color('white')
  shapesize and p.shapesize(stretch_wid=5, stretch_len=1)
  p.penup()
  p.goto(pos, 0)
  return p

wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer()
wn.listen()
wn.onkeypress()

paddle_a = createPong(-350)
paddle_b = createPong(350)
ball = createPong(0, False)


while True:
  wn.update()