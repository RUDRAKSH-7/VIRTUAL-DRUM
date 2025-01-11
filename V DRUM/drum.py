import pygame ; from pygame import mixer
pygame.init()

height = 500 ; width = 800
screen = pygame.display.set_mode((width,height),) ; pygame.display.set_caption("V-DRUM") ; pygame.display.set_icon(pygame.image.load(r"assets\icon.png"))

def drum():
    kick = snare = close = open_ = mem = crash = ride = (255,255,255)

    #sounds
    kick_s = mixer.Sound(r"assets\kick_.wav")
    snare_s = mixer.Sound(r"assets\snare.wav")
    chat_s = mixer.Sound(r"assets\chat.wav")
    ohat_s = mixer.Sound(r"assets\ohat.wav")
    mem_s = mixer.Sound(r"assets\mem.wav")
    crash_s = mixer.Sound(r"assets\crash.wav")
    ride_s = mixer.Sound(r"assets\Ride.wav")

    font = pygame.font.Font(r"assets\mc.ttf",28)
    font_ = pygame.font.Font(r"assets\mc.ttf",16)
    f = pygame.font.Font("freesansbold.ttf",28)

    while True:
        screen.fill((0,5,10))
        #texts
        colon = f.render(":",True,(255,255,255))
        help_text = font_.render("HELP    esc",True,(255,255,255))
        kick_ = font.render("kick - ",True,kick)
        snare_ = font.render("snare",True,snare)
        c_hat = font.render("C-HAT",True,close)
        o_hat = font.render("O-HAT",True,open_)
        mem_ =  font.render("MEM",True,mem)
        crash_ = font.render("CRASH",True,crash)
        ride_ = font.render("RIDE",True,ride)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_k:
                    kick = (0,69,255)
                    mixer.Sound.play(kick_s)

                if e.key == pygame.K_s:
                    snare = (2,240,250)
                    mixer.Sound.play(snare_s)

                if e.key == pygame.K_a:
                    close = (67,255,0) 
                    mixer.Sound.stop(ohat_s)
                    mixer.Sound.play(chat_s)

                if e.key == pygame.K_d:
                    open_ = (255,239,1)
                    mixer.Sound.play(ohat_s)

                if e.key == pygame.K_m:
                    mem = (255,0,52)
                    mixer.Sound.play(mem_s)
                
                if e.key == pygame.K_w:
                    crash = (255,190,17)
                    mixer.Sound.play(crash_s)
                
                if e.key == pygame.K_r:
                    ride = (247,212,17)
                    mixer.Sound.play(ride_s)

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_k:
                    kick = (255,255,255)
                elif e.key == pygame.K_s:
                    snare = (255,255,255)
                elif e.key == pygame.K_a:
                    close = (255,255,255)
                elif e.key == pygame.K_d:
                    open_ = (255,255,255)
                elif e.key == pygame.K_m:
                    mem = (255,255,255)
                if e.key == pygame.K_ESCAPE:
                    return True
                elif e.key == pygame.K_w:
                    crash = (255,255,255)
                elif e.key == pygame.K_r:
                    ride = (255,255,255)

        screen.blit(help_text,(10,10))
        screen.blit(colon,(65,2))

        #snare
        pygame.draw.rect(screen,snare,(285,280,200,100),10)
        screen.blit(snare_,(338,320))
        #kick drum
        screen.blit(kick_,(350,435))
        pygame.draw.rect(screen,kick,(135,395,500,100),10)

        #close hi-hat
        pygame.draw.rect(screen,close,(135,280,120,100),10)
        screen.blit(c_hat,(150,320))

        #open hi-hat
        pygame.draw.rect(screen,open_,(515,280,120,100),10)
        screen.blit(o_hat,(528,320))

        #MEMPHIS COWBELL
        pygame.draw.rect(screen,mem,(670,250,120,100),10)
        screen.blit(mem_,(695,290))

        #CRASH
        pygame.draw.rect(screen,crash,(10,60,180,150),10)
        screen.blit(crash_,(50,125))

        #RIDE
        pygame.draw.rect(screen,ride,(610,60,180,150),10)
        screen.blit(ride_,(670,125))

        pygame.display.update()
drum()


def help():
    font = pygame.font.Font(r"assets\mc.ttf",48)
    font_ = pygame.font.Font("freesansbold.ttf",40)
    sep_ = font_.render(":",True,(255,255,255))
    help_text = font.render("CONTROLS",True,(255,255,255))
    kick = font.render("KICK            K",True,(0,69,255))
    snare = font.render("SNARE          S",True,(2,240,250))
    ohat = font.render("o  HAT         D",True,(255,239,1))
    chat = font.render("C  HAT         A",True,(67,255,0))
    mem = font.render("MEM            M",True,(255,0,52))
    crash = font.render("CRASH          W",True,(255,190,17))
    ride = font.render("RIDE            R",True,(247,212,17))

    while True:
        screen.fill((0,0,0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    return True
        
        screen.blit(help_text,(260,20))

        screen.blit(kick,(160,100))

        screen.blit(snare,(155,160))

        screen.blit(chat,(163,220))

        screen.blit(ohat,(163,280))

        screen.blit(mem,(165,340))

        screen.blit(ride,(163,400))

        screen.blit(crash,(158,455))


        pygame.display.update()
# help()

while True:
    if drum():
        if help():
            continue