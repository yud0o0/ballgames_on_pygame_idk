version="snapshot 1.4/05.10.2025"
# https://github.com/yud0o0/ballgames_on_pygame_idk 
import pygame
import random as r
import math as m
pygame.init()
_text_cache = {}
class Rendering:
    class text:
        @staticmethod
        def textwithoutline(text, x, y, size, fg=(255, 255, 255), outline_col=(0, 0, 0), outline_size=2):
            global screen
            font=pygame.freetype.Font("arialnarrow.ttf", int(size))
            key = (text, size, fg, outline_col, outline_size)
            if key in _text_cache:
                surf = _text_cache[key]
            else:
                base_surf, _ = font.render(text, fg)
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
            rect = surf.get_rect(center=(x, y))
            screen.blit(surf, rect)
        @staticmethod
        def textfill(text, x=None, y=None, pos=None, size=20, fg=(0,0,0)):
            global screen
            font=pygame.freetype.Font("arialnarrow.ttf", int(size))
            if pos is not None:
                x, y = pos
            font.wide = True
            font.strong = True
            surf, _ = font.render(text, fg)
            rect = surf.get_rect(center=(x, y))
            screen.blit(surf, rect)
            font.wide = False
            font.strong = False
    @staticmethod
    def ball(color,coords,radius,hp):
        pygame.draw.circle(screen, "black", coords, radius+2)
        pygame.draw.circle(screen, color, coords, radius)
        Rendering.text.textfill(str(hp), pos=coords)
    @staticmethod
    def button(color,left,top,width,height,text):
        global screen
        buttonrectd=pygame.Rect(left-3,top-3,width+6,height+6)
        buttonrect=pygame.Rect(left,top,width,height)
        pygame.draw.rect(screen,"black",buttonrectd)
        pygame.draw.rect(screen,color,buttonrect)
        Rendering.text.textwithoutline(text, left+width/2, top+height/2, height/1.5)
        return buttonrect
    def sword(sword,angles,xs,ys):
        sword_rotated = pygame.transform.rotate(sword, -m.degrees(angles)-90)
        sword_rect = sword_rotated.get_rect(center=(xs, ys))
        screen.blit(sword_rotated, sword_rect)
        return sword_rect
class menu:
    def __init__(self):
        self.sworda=menu.files.sworda
        self.swordb=menu.files.swordb
    class statics:
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
        areyouneedhb = True
        xwwsize=xwsize-radius
        ywwsize=ywsize-radius
        MRunning=True
        Running=False
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
        swordb_hit=False
        sworda_hit=False
        swords_hit=True
        sratio=40/150
        scale=3.5
        sword_height = radius * scale
        sword_width = int(sword_height * sratio)
        game_endede=pygame.USEREVENT+1
        game_startede=pygame.USEREVENT+2
    class files:
        metal_sound=pygame.mixer.Sound("hit-metal.mp3")
        punchwithwall_sound=pygame.mixer.Sound("classic-punch.mp3")
        fistpunch_sound=pygame.mixer.Sound("fist-fight.mp3")
        game_ended=pygame.mixer.Sound("game-ended.mp3")
        game_started=pygame.mixer.Sound("sound-effec.mp3")
    class math:
        def gamestartedmath(wc1, bv1, anglea1, angleb1):
            wc1+=1
            bv=bv1
            anglea=anglea1
            angleb=angleb1
            xva=m.cos(anglea)*bv
            xvb=m.cos(angleb)*bv
            yva=m.sin(anglea)*bv
            yvb=m.sin(angleb)*bv
            pygame.mixer.Sound.play(menu.files.game_started)
            return wc1,bv,anglea,angleb,xva,xvb,yva,yvb
        def punchwwall(x,y, xv,yv, xwsize,ywsize, xwwsize,ywwsize):
            if x >= xwwsize or x <= xwsize-xwwsize:
                xv *= -1
                pygame.mixer.Sound.play(menu.files.punchwithwall_sound)
            if y >= ywwsize or y <= ywsize-ywwsize:
                yv *= -1
                pygame.mixer.Sound.play(menu.files.punchwithwall_sound)
            return xv,yv
        def punchBALLS(distance,radius,xvb2,yvb2,xva2,yva2,xva,yva,xvb,yvb):
            if distance <= radius*2:
                xva, yva = xvb2, yvb2
                xvb, yvb = xva2, yva2
                pygame.mixer.Sound.play(menu.files.punchwithwall_sound)
            return xva, yva, xvb, yvb
        def swordspunch(sworda_rect,swordb_rect,swords_hit,brv):
            if sworda_rect.colliderect(swordb_rect):
                if swords_hit==False:
                    swords_hit = True
                    brv *= -1
                    pygame.mixer.Sound.play(menu.files.metal_sound)
            else:
                swords_hit = False
            return swords_hit,brv
        def coordscount(xa,xva,radiuss,anglesa,anglesb,xb,xvb,ya,yva,yb,yvb):
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
            return xa,xsa,xb,xsb,ya,ysa,yb,ysb,coordsa,coordsb
        def swordhitball(sword_rect,ball_rect,sword_hit,hp,damage):
            if sword_rect.colliderect(ball_rect):
                if not sword_hit:
                    sword_hit = True
                    hp -= damage
                    damage += 1
                    pygame.mixer.Sound.play(menu.files.fistpunch_sound)
                    pygame.time.delay(90)
            else:
                sword_hit = False
            return sword_hit,hp,damage
screen=pygame.display.set_mode(size=(menu.statics.xwsize, menu.statics.ywsize))
pygame.display.set_caption("яица")
clock = pygame.time.Clock()
class menureal:
    def __init__(self):
        s=1

    def menu(self):
        MRunning=menu.statics.MRunning
        global screen
        amenu=False
        bmenu=False
        radius=menu.statics.radius
        coordsbba=(menu.statics.xwsize/7*2,menu.statics.ywsize/7*3)
        coordsbbb=(menu.statics.xwsize/7*5,menu.statics.ywsize/7*3)
        bwidth=menu.statics.xwsize/4
        bheight=menu.statics.ywsize/8
        while MRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MRunning = False 
            screen.fill("mediumseagreen")
            if amenu==False and bmenu==False:
                abutton=Rendering.button("red",((menu.statics.xwsize/7*2)-bwidth/2),(menu.statics.ywsize/7*5),bwidth,bheight,"abutton")
                bbutton=Rendering.button("blue",((menu.statics.xwsize/7*5)-bwidth/2),(menu.statics.ywsize/7*5),bwidth,bheight,"bbutton")
                Rendering.ball("red",coordsbba,radius,100)
                Rendering.ball("blue",coordsbbb,radius,100)
                mpos=pygame.mouse.get_pos()
                if abutton.collidepoint(mpos):
                    Rendering.button((250, 137, 117),((menu.statics.xwsize/7*2)-bwidth/2),(menu.statics.ywsize/7*5),bwidth,bheight,"abutton")
                    Rendering.ball((250, 137, 117),coordsbba,radius,100)
                    mp=pygame.mouse.get_pressed()
                    if mp==(True,False,False):
                        amenu=True
                if bbutton.collidepoint(mpos):
                    Rendering.button((134, 177, 209),((menu.statics.xwsize/7*5)-bwidth/2),(menu.statics.ywsize/7*5),bwidth,bheight,"bbutton")
                    Rendering.ball((117, 157, 250),coordsbbb,radius,100)
                    mp=pygame.mouse.get_pressed()
                    if mp==(True,False,False):
                        bmenu=True
            if amenu or bmenu == True:
                screen.fill("black")
                Rendering.text.textwithoutline("I haven't had time to do this part of menu yet", menu.statics.xwsize/2, menu.statics.ywsize/3*2, (menu.statics.xwsize+menu.statics.ywsize)/50, "crimson")
                Rendering.text.textwithoutline("press a Space to start", menu.statics.xwsize/2, menu.statics.ywsize/2, (menu.statics.xwsize+menu.statics.ywsize)/20, "crimson")
            pygame.mouse.get_pressed
            key=pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                MRunning=False
                start=True
            pygame.display.flip()
            clock.tick(60)
        return MRunning, start
class swordfiles:
    sworda=pygame.image.load("sword.png")
    swordb=pygame.image.load("sword.png")
    sworda = pygame.transform.scale(sworda, (menu.statics.sword_width, menu.statics.sword_height))
    swordb = pygame.transform.scale(swordb, (menu.statics.sword_width, menu.statics.sword_height))
class game: 
    def __init__(self):
        self.game_startede=menu.statics.game_startede
        self.bv1=menu.statics.bv1
        self.anglea1=menu.statics.anglea1
        self.angleb1=menu.statics.angleb1
        self.xwsize=menu.statics.xwsize
        self.ywsize=menu.statics.ywsize
        self.xwwsize=menu.statics.xwwsize
        self.ywwsize=menu.statics.ywwsize
        self.xa=menu.statics.xa
        self.xb=menu.statics.xb
        self.ya=menu.statics.ya
        self.yb=menu.statics.yb
        self.anglesa=menu.statics.anglesa
        self.anglesb=menu.statics.anglesb
        self.xva=menu.statics.xva
        self.xvb=menu.statics.xvb
        self.yva=menu.statics.yva
        self.yvb=menu.statics.yvb
        self.a=menu.statics.a
        self.b=menu.statics.b
        self.brv=menu.statics.brv
        self.radius=menu.statics.radius
        self.radiuss=menu.statics.radiuss
        self.adamage=menu.statics.adamage
        self.bdamage=menu.statics.bdamage
        self.swordb_hit=menu.statics.swordb_hit
        self.sworda_hit=menu.statics.sworda_hit
        self.swords_hit=menu.statics.swords_hit
        self.game_endede=menu.statics.game_endede
        self.sworda=swordfiles.sworda
        self.swordb=swordfiles.swordb
    def gamestart(self):
        xa=self.xa
        xb=self.xb
        ya=self.ya
        yb=self.yb
        anglesa=self.anglesa
        anglesb=self.anglesb
        xva=self.xva
        yva=self.yva
        xvb=self.xvb
        yvb=self.yvb
        a=self.a
        b=self.b
        brv=self.brv
        radius=self.radius
        radiuss=self.radiuss
        adamage=self.adamage
        bdamage=self.bdamage
        swordb_hit=self.swordb_hit
        sworda_hit=self.sworda_hit
        game_endede=self.game_endede
        swords_hit=self.swords_hit
        sworda=self.sworda
        swordb=self.swordb
        global Running
        swordb_rect=swordb.get_rect()
        sworda_rect=sworda.get_rect()
        wc1=0
        wc0=0
        pygame.time.set_timer(self.game_startede, 3000)
        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False 
                if event.type == self.game_startede and wc1==0:
                    wc1,bv,anglea,angleb,xva,xvb,yva,yvb=menu.math.gamestartedmath(wc1, self.bv1,self.anglea1,self.angleb1)
            distance=((xb-xa)**2+(yb-ya)**2)**0.5
            if a > 0:
                xva,yva=menu.math.punchwwall(xa,ya,xva,yva,self.xwsize,self.ywsize,self.xwwsize,self.ywwsize)      
            if b > 0:
                xvb,yvb=menu.math.punchwwall(xb,yb,xvb,yvb,self.xwsize,self.ywsize,self.xwwsize,self.ywwsize)
            anglesa += brv
            anglesb += brv
            xva2=xva
            yva2=yva
            xvb2=xvb
            yvb2=yvb
            if a > 0 and b > 0:
                xva,yva,xvb,yvb=menu.math.punchBALLS(distance,radius,xvb2,yvb2,xva2,yva2,xva,yva,xvb,yvb)
                swords_hit,brv=menu.math.swordspunch(sworda_rect,swordb_rect,swords_hit,brv)
            xa,xsa,xb,xsb,ya,ysa,yb,ysb,coordsa,coordsb=menu.math.coordscount(xa,xva,radiuss,anglesa,anglesb,xb,xvb,ya,yva,yb,yvb)
            if a > 0:
                aball = pygame.Surface((radius, radius), pygame.SRCALPHA)
                aball_rect = pygame.Rect(xa-(radius * 0.8), ya-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
            if b > 0:
                bball = pygame.Surface((radius, radius), pygame.SRCALPHA)
                bball_rect = pygame.Rect(xb-(radius * 0.8), yb-(radius * 0.8), (radius * 0.8)*2, (radius * 0.8)*2)
            if a > 0 and b > 0:
                swordb_hit,b,adamage=menu.math.swordhitball(sworda_rect,bball_rect,swordb_hit,b,adamage)
                sworda_hit,a,bdamage=menu.math.swordhitball(swordb_rect,aball_rect,sworda_hit,a,bdamage)
            screen.fill((252, 250, 250))
            if a > 0:
                Rendering.ball("red",coordsa,radius,a)
                sworda_rect=Rendering.sword(sworda,anglesa,xsa,ysa)
            if b > 0:
                Rendering.ball("blue",coordsb,radius,b)
                swordb_rect=Rendering.sword(swordb,anglesb,xsb,ysb)
            if menu.statics.areyouneedhb==True:
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
                    pygame.mixer.Sound.play(menu.files.game_ended)
                    w=(f"The winner is {game_endedee.winner}!")
                    pygame.time.set_timer(game_endede, 20000)
                Rendering.text.textwithoutline(w, self.xwsize/2, self.ywsize/2,40)
                if event.type == game_endede:
                    Running = False
            vs=f"{menu.statics.aplayertype} VS {menu.statics.bplayertype}"
            Rendering.text.textwithoutline(vs, 250, 20, 30)
            Rendering.text.textwithoutline(f"A damage: {adamage}", self.xwsize/4-60, self.ywsize-20,20)
            Rendering.text.textwithoutline(f"D damage: {bdamage}", (self.xwsize/4)*3+60, self.ywsize-20,20)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
mr = menureal()
MRunning, start=mr.menu()
if MRunning==False and start==True:
    Running=True
    g = game() 
    g.gamestart()