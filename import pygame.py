import pygame
import random as r
import math as m
import ctypes
pygame.init()
xwsize=500
ywsize=500
txwsize=1000
tywsize=600
adamage=1
a=100
bdamage=1
b=100
bv=5
brv=0.06
radius=ywsize/20
bv1=bv
aplayertype="sword"
bplayertype="sword"
aynhbinput = input("Do you want to see hit boxes? (True/False): ").strip().lower()
areyouneedhb = aynhbinput in ("True","true","TRUE","t","T","1","y","Y","Yes","yes","YES")
xwwsize=xwsize-radius
ywwsize=ywsize-radius
screen=pygame.display.set_mode(size=(xwsize, ywsize))
pygame.display.set_caption("яица")
fontaab=pygame.freetype.Font("arialnarrow.ttf", int(radius))
fontaab.wide=True
fontaab.strong=True
fontw=pygame.freetype.Font("arialnarrow.ttf", 40)
fontvs=pygame.freetype.Font("arialnarrow.ttf", 30)
fontd=pygame.freetype.Font("arialnarrow.ttf", 20)
_text_cache = {}
def textwithoutline(font, text, fg=(255,255,255), outline_col=(0,0,0), outline_size=2):
    key = (id(font), text, fg, outline_col, int(outline_size))
    if key in _text_cache:
        return _text_cache[key]
    base_surf, base_rect = font.render(text, fg)
    ow = outline_size
    w = base_surf.get_width() + 2*ow
    h = base_surf.get_height() + 2*ow
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    for dx in range(-ow, ow+1):
        for dy in range(-ow, ow+1):
            if dx*dx + dy*dy <= ow*ow:
                outline_surf, _ = font.render(text, outline_col)
                surf.blit(outline_surf, (dx+ow, dy+ow))
    surf.blit(base_surf, (ow, ow))
    _text_cache[key] = surf
    return surf
clock = pygame.time.Clock()
running=True
radiuss = radius*2 + 3 + 30
anglesa=m.radians(180)
anglesb=m.radians(360)
anglea=r.uniform(0, 2*m.pi)
anglea1=anglea
anglea=0
angleb=r.uniform(0, 2*m.pi)
angleb1=angleb
angleb=0
xva=0
xvb=0
yva=0
yvb=0
xa=xwsize/5
xb=(xwsize/5)*4
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
swords_hit=True
sratio=40/150
scale=3.5
sword_height = radius * scale
sword_width = int(sword_height * sratio)
sworda = pygame.transform.scale(sworda, (sword_width, sword_height))
swordb = pygame.transform.scale(swordb, (sword_width, sword_height))
metal_sound=pygame.mixer.Sound("hit-metal.mp3")
punchwithwall_sound=pygame.mixer.Sound("classic-punch.mp3")
fistpunch_sound=pygame.mixer.Sound("fist-fight.mp3")
game_ended=pygame.mixer.Sound("game-ended.mp3")
game_started=pygame.mixer.Sound("sound-effec.mp3")
game_endede=pygame.USEREVENT+1
game_startede=pygame.USEREVENT+2
wc0=0
wc1=0
bv=0
pygame.time.set_timer(game_startede, 3000)
hwnd = pygame.display.get_wm_info()["window"]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == game_startede and wc1==0:
            wc1+=1
            ctypes.windll.user32.SetForegroundWindow(hwnd)
            bv=bv1
            anglea=anglea1
            angleb=angleb1
            xva=m.cos(anglea)*bv
            xvb=m.cos(angleb)*bv
            yva=m.sin(anglea)*bv
            yvb=m.sin(angleb)*bv
            pygame.mixer.Sound.play(game_started)
    distance=((xb-xa)**2+(yb-ya)**2)**0.5
    if a > 0:
        if xa >= xwwsize or xa <= xwsize-xwwsize:
            xva *= -1
            pygame.mixer.Sound.play(punchwithwall_sound)
        if ya >= ywwsize or ya <= ywsize-ywwsize:
            yva *= -1
            pygame.mixer.Sound.play(punchwithwall_sound)
    if b > 0:
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
    if a > 0 and b > 0:
        if distance<=radius*2:
            xva=xvb2
            yva=yvb2
            xvb=xva2
            yvb=yva2
            pygame.mixer.Sound.play(punchwithwall_sound)
    if a > 0 and b > 0:
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
    if a > 0:
        aball = pygame.Surface((radius, radius), pygame.SRCALPHA)
        aball_rect = pygame.Rect(xa-(radius * 0.8), ya-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
    if b > 0:
        bball = pygame.Surface((radius, radius), pygame.SRCALPHA)
        bball_rect = pygame.Rect(xb-(radius * 0.8), yb-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
    if a > 0 and b > 0:
        if sworda_rect.colliderect(bball_rect):
            if not swordb_hit:
                swordb_hit = True
                b -= adamage
                adamage += 1
                pygame.mixer.Sound.play(fistpunch_sound)
                pygame.time.delay(90)
        else:
            swordb_hit = False
        if swordb_rect.colliderect(aball_rect):
            if not sworda_hit:
                sworda_hit = True
                a -= bdamage
                bdamage += 1
                pygame.mixer.Sound.play(fistpunch_sound)
                pygame.time.delay(90)
        else:
            sworda_hit = False
    screen.fill((252, 250, 250))
    if a > 0:
        pygame.draw.circle(screen, "black", coordsa, radius+2)
        pygame.draw.circle(screen, "red", coordsa, radius)
        acounter, arect=fontaab.render(str(a), "black")
        arect.center=coordsa
        screen.blit(acounter, arect)
        sworda_rotated = pygame.transform.rotate(sworda, -m.degrees(anglesa)-90)
        sworda_rect = sworda_rotated.get_rect(center=(xsa, ysa))
        screen.blit(sworda_rotated, sworda_rect)
    if b > 0:
        pygame.draw.circle(screen, "black", coordsb, radius+2)
        pygame.draw.circle(screen, "blue", coordsb, radius)
        bcounter, brect=fontaab.render(str(b), "black")
        brect.center=coordsb
        screen.blit(bcounter, brect)
        swordb_rotated = pygame.transform.rotate(swordb, -m.degrees(anglesb)-90)
        swordb_rect = swordb_rotated.get_rect(center=(xsb, ysb))
        screen.blit(swordb_rotated, swordb_rect)
    if areyouneedhb==True:
        if a > 0:
            pygame.draw.rect(screen, (0, 255, 0), aball_rect, 3)
            pygame.draw.rect(screen, (0, 0, 255), sworda_rect, 3)
        if b > 0:
            pygame.draw.rect(screen, (255, 0, 0), bball_rect, 3)
            pygame.draw.rect(screen, (255, 255, 0), swordb_rect, 3)
    if a <= 0 or b <= 0:
        if a <= 0:
            game_endedee=pygame.event.Event(game_endede, {"winner": "blue"})
        if b <= 0:
            game_endedee=pygame.event.Event(game_endede, {"winner": "red"})
        if wc0==0:
            wc0=1
            pygame.mixer.Sound.play(game_ended)
            w=(f"The winner is {game_endedee.winner}!")
            pygame.time.set_timer(game_endede, 20000)
        winertext=textwithoutline(fontw, w)
        wrect=winertext.get_rect(center=(xwsize/2, ywsize/2))
        screen.blit(winertext, wrect)
        if event.type == game_endede:
            running = False
    vs=f"{aplayertype} VS {bplayertype}"
    vstext=textwithoutline(fontvs, vs)
    vsrect=vstext.get_rect(center=(xwsize/2, 20))
    adtext=textwithoutline(fontd, f"A damage: {adamage}")
    adrect=adtext.get_rect(center=(xwsize/4-60, ywsize-20))
    bdtext=textwithoutline(fontd, f"D damage: {bdamage}")
    bdrect=bdtext.get_rect(center=((xwsize/4)*3+60, ywsize-20))
    screen.blit(vstext, vsrect)
    screen.blit(adtext, adrect)
    screen.blit(bdtext, bdrect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()