import pgzrun
WIDTH=600
HEIGHT=600
TITLE="Bird Day"

bee=Actor('bee',(300,300))
flower=Actor('flower')

def draw():
    screen.clear()
    screen.blit('background',(0,0))
    flower.draw()
    bee.draw()
def update():
    if keyboard.left:
        bee.x=bee.x-2
        if bee.x<0:
           bee.x=10
    if keyboard.right:
        bee.x=bee.x+2
        if bee.x>600:
           bee.x=590
    if keyboard.down:
        bee.y=bee.y+2
        if bee.y>600:
           bee.y=590
    if keyboard.up:
        bee.y=bee.y-2
        if bee.y<0:
           bee.y=10
    






pgzrun.go()