import pygame
import random as r
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
a=100
b=100
xpa=r.randint(-5, 5)
xpb=r.randint(-5, 5)
ypa=r.randint(-5, 5)
ypb=r.randint(-5, 5)
xa=xwsize/3
xb=(xwsize/3)*2
ya=ywsize/2
yb=ywsize/2
txa=(xwsize/3)-10
txb=((xwsize/3)*2)-10
tya=ywsize/2-6
tyb=ywsize/2-6
coordsa=xa,ya
coordsb=xb,yb
coordstexta=txa,tya
coordstextb=txb,tyb
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    distance=((xb-xa)**2+(yb-ya)**2)**0.5
    print(int(distance))
    if xa >= xwwsize or xa <= xwsize-xwwsize or distance<=30:
        xpa *= -1
    if ya >= ywwsize or ya <= ywsize-ywwsize or distance<=30:
        ypa *= -1
    if xb >= xwwsize or xb <= xwsize-xwwsize or distance<=30:
        xpb *= -1
    if yb >= ywwsize or yb <= ywsize-ywwsize or distance<=30:
        ypb *= -1
    if distance<=30:
        a-=1
        b-=1
    xa += xpa
    xb += xpb
    ya += ypa
    yb += ypb
    txa += xpa
    txb += xpb
    tya += ypa
    tyb += ypb
    coordsa=xa,ya
    coordsb=xb,yb
    coordstexta=txa,tya
    coordstextaa=txa-1, tya-1
    coordstextb=txb,tyb
    coordstextbb=txb-1, tyb-1

    screen.fill("white")
    pygame.draw.circle(screen, "black", coordsa, 17)
    pygame.draw.circle(screen, "red", coordsa, 15)
    pygame.draw.circle(screen, "black", coordsb, 17)
    pygame.draw.circle(screen, "blue", coordsb, 15)
    acounterr=fontt.render(str(a), True, "black")
    acounter=font.render(str(a), True, "white")
    bcounterr=fontt.render(str(b), True, "black")
    bcounter=font.render(str(b), True, "white")
    screen.blit(acounterr, coordstextaa)
    screen.blit(acounter, coordstexta)
    screen.blit(bcounterr, coordstextbb)
    screen.blit(bcounter, coordstextb)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()