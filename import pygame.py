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
adamage=1
a=100
bdamage=1
b=100
bv=5
brv=0.1
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
sworda=pygame.image.load("withoutname.png")
sworda_rect=sworda.get_rect()
sworda_mask=pygame.mask.from_surface(sworda)
swordb=pygame.image.load("withoutname.png")
swordb_rect=swordb.get_rect()
swordb_mask=pygame.mask.from_surface(swordb)
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
    anglesb += brv
    xva2=xva
    yva2=yva
    xvb2=xvb
    yvb2=yvb
    if distance<=30:
        xva=xvb2
        yva=yvb2
        xvb=xva2
        yvb=yva2
    xa += xva
    xsa = xa + radius * m.cos(anglesa)
    xb += xvb
    xsb = xb + radius * m.cos(anglesb)
    ya += yva
    ysa = ya + radius * m.sin(anglesa)
    yb += yvb
    ysb = yb + radius * m.sin(anglesb)
    coordsa=xa,ya
    coordsb=xb,yb
    aball = pygame.Surface((30, 30), pygame.SRCALPHA)
    aball_rect = pygame.Rect(xa-15, ya-15, 30, 30)
    aball_mask=pygame.mask.from_surface(aball)
    bball = pygame.Surface((30, 30), pygame.SRCALPHA)
    bball_rect = pygame.Rect(xb-15, yb-15, 30, 30)
    bball_mask=pygame.mask.from_surface(bball)
    offset2C = (swordb_rect.x - sworda_rect.x, swordb_rect.y - sworda_rect.y)
    if sworda_mask.overlap(swordb_mask, offset2C):
        brv *= -1
    offsetbball = (bball_rect.x - sworda_rect.x, bball_rect.y - sworda_rect.y)
    if sworda_mask.overlap(pygame.Mask((30,30), fill=True), offsetbball):
        if not swordb_hit:
            swordb_hit = True
            b -= adamage
            adamage += 1
            t.sleep(0.5)
    else:
        swordb_hit = False
    offsetaball = (aball_rect.x - swordb_rect.x, aball_rect.y - swordb_rect.y)
    if swordb_mask.overlap(pygame.Mask((30,30), fill=True), offsetaball):
        if not sworda_hit:
            sworda_hit = True
            a -= bdamage
            bdamage += 1
            t.sleep(0.5)
    else:
        sworda_hit = False

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
    sworda_rotated = pygame.transform.rotate(sworda, -m.degrees(anglesa)-90)
    sworda_rect = sworda_rotated.get_rect(center=(xsa, ysa))
    screen.blit(sworda_rotated, sworda_rect)
    swordb_rotated = pygame.transform.rotate(swordb, -m.degrees(anglesb)-90)
    swordb_rect = swordb_rotated.get_rect(center=(xsb, ysb))
    screen.blit(swordb_rotated, swordb_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()