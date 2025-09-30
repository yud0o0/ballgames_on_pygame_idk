import pygame
import random as r
import math as m
pygame.init()
xwsize=500
ywsize=500
radius=ywsize/20
xwwsize=xwsize-radius
ywwsize=ywsize-radius
screen=pygame.display.set_mode(size=(xwsize, ywsize))
font=pygame.font.Font(None, int(radius))
fontt=pygame.font.Font(None, int(radius+3))
clock = pygame.time.Clock()
aynhbinput = input("Do you want to see hit boxes? (True/False): ").strip().lower()
areyouneedhb = aynhbinput in ("True","true","TRUE","t","T","1","y","Y","Yes","yes","YES")
running=True
radiuss = radius*2 + 3 + 40
adamage=1
a=100
bdamage=1
b=100
bv=5
brv=0.06
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
sworda=pygame.image.load("sword.png")
sworda_rect=sworda.get_rect()
swordb=pygame.image.load("sword.png")
swordb_rect=swordb.get_rect()
swordb_hit=False
sworda_hit=False
swords_hit=False
sratio=40/150
scale=4
sword_height = radius * scale
sword_width = int(sword_height * sratio)
sworda = pygame.transform.scale(sworda, (sword_width, sword_height))
swordb = pygame.transform.scale(swordb, (sword_width, sword_height))
metal_sound=pygame.mixer.Sound("hit-metal.mp3")
punchwithwall_sound=pygame.mixer.Sound("classic-punch.mp3")
fistpunch_sound=pygame.mixer.Sound("fist-fight.mp3")
game_ended=pygame.mixer.Sound("game-ended.mp3")
game_started=pygame.mixer.Sound("sound-effec.mp3")
pygame.mixer.Sound.play(game_started)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if a <= 0 or b <= 0:
        if a <= 0:
            print("Blue won!")
        if b <= 0:
            print("Red won!")
        pygame.mixer.Sound.play(game_ended)
        pygame.time.delay(2000)
        running = False
    distance=((xb-xa)**2+(yb-ya)**2)**0.5
    if xa >= xwwsize or xa <= xwsize-xwwsize:
        xva *= -1
        pygame.mixer.Sound.play(punchwithwall_sound)
    if ya >= ywwsize or ya <= ywsize-ywwsize:
        yva *= -1
        pygame.mixer.Sound.play(punchwithwall_sound)
    if xb >= xwwsize or xb <= xwsize-xwwsize:
        xvb *= -1
        pygame.mixer.Sound.play(punchwithwall_sound)
    if yb >= ywwsize or yb <= ywsize-ywwsize:
        yvb *= -1
        pygame.mixer.Sound.play(punchwithwall_sound)
    anglesa += brv
    anglesb += brv
    xva2=xva
    yva2=yva
    xvb2=xvb
    yvb2=yvb
    if distance<=radius*2:
        xva=xvb2
        yva=yvb2
        xvb=xva2
        yvb=yva2
        pygame.mixer.Sound.play(punchwithwall_sound)
    if sworda_rect.colliderect(swordb_rect):
        if not swords_hit:
            swords_hit = True
            brv *= -1
            pygame.mixer.Sound.play(metal_sound)
    else:
        swords_hit = False
    xa += xva
    xsa = xa + radiuss * m.cos(anglesa)
    xb += xvb
    xsb = xb + radiuss * m.cos(anglesb)
    ya += yva
    ysa = ya + radiuss * m.sin(anglesa)
    yb += yvb
    ysb = yb + radiuss * m.sin(anglesb)
    coordsa=xa,ya
    coordsb=xb,yb
    aball = pygame.Surface((radius, radius), pygame.SRCALPHA)
    aball_rect = pygame.Rect(xa-(radius * 0.8), ya-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
    bball = pygame.Surface((radius, radius), pygame.SRCALPHA)
    bball_rect = pygame.Rect(xb-(radius * 0.8), yb-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
    if sworda_rect.colliderect(bball_rect):
        if not swordb_hit:
            swordb_hit = True
            b -= adamage
            adamage += 1
            pygame.mixer.Sound.play(fistpunch_sound)
    else:
        swordb_hit = False
    if swordb_rect.colliderect(aball_rect):
        if not sworda_hit:
            sworda_hit = True
            a -= bdamage
            bdamage += 1
            pygame.mixer.Sound.play(fistpunch_sound)
    else:
        sworda_hit = False

    screen.fill("white")
    pygame.draw.circle(screen, "black", coordsa, radius+3)
    pygame.draw.circle(screen, "red", coordsa, radius)
    pygame.draw.circle(screen, "black", coordsb, radius+3)
    pygame.draw.circle(screen, "blue", coordsb, radius)
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
    if areyouneedhb==True:
        pygame.draw.rect(screen, (0, 255, 0), aball_rect, 3)
        pygame.draw.rect(screen, (255, 0, 0), bball_rect, 3)
        pygame.draw.rect(screen, (0, 0, 255), sworda_rect, 3) 
        pygame.draw.rect(screen, (255, 255, 0), swordb_rect, 3)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()