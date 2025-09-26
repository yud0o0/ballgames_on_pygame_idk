import pygame
import random as r
import math as m
import time as t
pygame.init()
xwsize=500
ywsize=500
xwwsize=xwsize-15
ywwsize=ywsize-15
screen=pygame.display.set_mode(size=(xwsize, ywsize))
font=pygame.font.Font(None, 23)
fontt=pygame.font.Font(None, 25)
clock = pygame.time.Clock()

running=True
radius = 40
a=100
b=100
bv=5
brv=0.05
anglesa=m.radians(90)
anglesb=m.pi
anglea=r.uniform(0, 2*m.pi)
angleb=r.uniform(0, 2*m.pi)
xva=m.cos(anglea)*bv
xvb=m.cos(angleb)*bv
yva=m.sin(anglea)*bv
yvb=m.sin(angleb)*bv
xa=xwsize/3
xb=(xwsize/3)*2
ya=ywsize/2
yb=ywsize/2
coordsa=xa,ya
coordsb=xb,yb
sword=pygame.image.load("withoutname.png")
sword_rect=sword.get_rect()
sword_mask=pygame.mask.from_surface(sword)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    distance=((xb-xa)**2+(yb-ya)**2)**0.5
    if xa >= xwwsize or xa <= xwsize-xwwsize:
        xva *= -1
    if ya >= ywwsize or ya <= ywsize-ywwsize:
        yva *= -1
    if xb >= xwwsize or xb <= xwsize-xwwsize:
        xvb *= -1
    if yb >= ywwsize or yb <= ywsize-ywwsize:
        yvb *= -1
    anglesa += brv
    anglesa += brv
    xva2=xva
    yva2=yva
    xvb2=xvb
    yvb2=yvb
    if distance<=30:
        xva=xvb2
        yva=yvb2
        xvb=xva2
        yvb=yva2
        a-=1
        b-=1
        t.sleep(0.5)
    xa += xva
    xsa = xa + radius * m.cos(anglesa)
    xb += xvb
    xsb = xb
    ya += yva
    ysa = ya + radius * m.sin(anglesa)
    yb += yvb
    ysb = yb
    coordsa=xa,ya
    coordsb=xb,yb

    screen.fill("white")
    pygame.draw.circle(screen, "black", coordsa, 17)
    pygame.draw.circle(screen, "red", coordsa, 15)
    pygame.draw.circle(screen, "black", coordsb, 17)
    pygame.draw.circle(screen, "blue", coordsb, 15)
    acounterr=fontt.render(str(a), True, "black")
    acounter=font.render(str(a), True, "white")
    bcounterr=fontt.render(str(b), True, "black")
    bcounter=font.render(str(b), True, "white")
    rect_a = acounter.get_rect(center=(xa, ya))
    rect_ar = acounterr.get_rect(center=(xa, ya))
    rect_b = bcounter.get_rect(center=(xb, yb))
    rect_br = bcounterr.get_rect(center=(xb, yb))
    screen.blit(acounterr,rect_ar)
    screen.blit(acounter, rect_a)
    screen.blit(bcounterr, rect_br)
    screen.blit(bcounter, rect_b)
    sword_rotated = pygame.transform.rotate(sword, -m.degrees(anglesa)-90)
    sword_rect = sword_rotated.get_rect(center=(xsa, ysa))
    screen.blit(sword_rotated, sword_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()