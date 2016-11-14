# Eagle eye
# This game is to test your colour level distinguish ablity
# By xmzhang xinmingamil@163.com

import sys,pygame,random,datetime
from pygame.locals import *

def title_screen():
    pygame.display.set_caption('Eagle eye')
    title_surface = font_surface('Eagle eye',120,(250,250,210))
    text = 'Click the green block to start the game'
    text_surface = font_surface(text,20,(0,255,0))

    pygame.mixer.music.load('start_screen_sound.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while True:
        background((65,105,225),(0,0,0))
        screen.blit(title_surface,(40,100))
        screen.blit(text_surface,(120,500))
        green_rect = pygame.Rect(162,402,77,77)
        pygame.draw.rect(screen,(0,255,0),green_rect,0)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if green_rect.collidepoint((x,y)):
                    pygame.mixer.music.stop()
                    return
                else:
                    pass


def timer(set_second):
    timer = datetime.datetime.now()-timer_start
    timer_second = timer.seconds
    return set_second - timer_second

def background(bg_colour,line_colour):
    screen.fill(bg_colour)
    for line in range(0,720,80):
        pygame.draw.line(screen,line_colour,(0,line),(640,line),3)
        pygame.draw.line(screen,line_colour,(line,0),(line,640),3) 

def font_surface(text,size,colour):
    font = pygame.font.get_default_font()
    font_layer = pygame.font.Font(font,size)
    font_surface = font_layer.render(text,True,colour)
    return font_surface

def transparent(surface):
    # action_effect_1
    surface_c = surface.copy()
    for i in xrange(128,255):
        surface_c.set_alpha(255-i)
        surface_c.fill(find_colour)
        background(bg_colour,line_colour)
        x,y = find_rect.center
        w,h = surface_c.get_size()
        screen.blit(surface_c,(x-w/2,y-h/2))
        pygame.display.update()
        pygame.time.wait(2)
        if pygame.event.get(pygame.QUIT):
            break
    return
        
def rotate(surface):
    #action_effect_2
    degree = 0
    while True:
        background(bg_colour,line_colour)
        surface.fill(find_colour)
        surface.set_colorkey((255,255,255))
        rotate_surface = pygame.transform.rotate(surface,degree)
        rotate_surface.set_colorkey((255,255,255))
        x,y = find_rect.center
        w,h = rotate_surface.get_size()
        screen.blit(rotate_surface,(x-w/2,y-h/2))
        pygame.display.update()
        pygame.time.wait(10)
        degree += 10
        if degree == 180:
            return
        if pygame.event.get(pygame.QUIT):
            break

def end_screen():
    rect_x,rect_y = 82,82
    pygame.display.set_caption('Game over')
    pygame.mixer.music.load('end_sound.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    
    if score >= 100:
        rank = 'SSS'
        comment = 'Perfect! Click the green block to play again.'
    elif score >= 98:
        rank = 'SS'
        comment = 'Awesome! Click the green block to play again.'
    elif score >= 95:
        rank = 'S'
        comment = 'Fantastic! Click the green block to play again.'
    elif score >= 90:
        rank = 'A'
        comment = 'Wonderful! Click the green block to play again.'
    elif score >= 80:
        rank = 'B'
        comment = 'Good! Click the green block to play again.'
    elif score >= 70:
        rank = 'C'
        comment = 'Cool! Click the green block to play again.'
    elif score >= 60:
        rank = 'D'
        comment = 'Aha! Click the green block to play again.'
    else:
        rank = 'E'
        comment = 'Er... Click the green block to play again.'
    
    while True:
        background((240,255,240),(240,255,0))
        rank_rect = pygame.Rect(rect_x,rect_y,77,77)
        pygame.draw.rect(screen,(218,112,214),rank_rect,0)

        # loop action effect 
        if rect_x == 82 and rect_y < 402:
            rect_y += 80
        elif rect_y == 402 and rect_x < 482:
            rect_x += 80
        elif rect_x == 482 and rect_y > 82:
            rect_y -= 80
        elif rect_y == 82 and rect_x > 82:
            rect_x -= 80
        pygame.time.wait(100)
        
        play_rect = pygame.Rect(82,402,77,77)
        pygame.draw.rect(screen,(0,255,127),play_rect,0)

        text_surface = font_surface('Score:',40,(0,0,128))
        score_surface = font_surface(str(score),200,(255,0,0))
        w,h = score_surface.get_size()

        comment_surface = font_surface(comment,25,(107,142,35))
        rank_surface = font_surface(rank,50,(255,105,180))
        w1,h1 = rank_surface.get_size()

        screen.blit(rank_surface,(120-w1/2,440-h1/2))
        screen.blit(comment_surface,(50,500))
        screen.blit(score_surface,(320-w/2,300-h/2))
        screen.blit(text_surface,(50,100))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if play_rect.collidepoint((x,y)):
                    return
                else:
                    pass

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640,640))
title_screen()

while True:
    timer_start = datetime.datetime.now()
    level = 50
    score = 50
    while level > 0 and timer(60):

        # creat the random colour of bg ,block and lines
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rgb=[red,green,blue]
        bg_colour = []
        find_colour =[]
        bg_colour[:] = find_colour[:] = rgb
        colour_channel = random.randint(0,2)
        find_colour[colour_channel] += level
        if find_colour[colour_channel]>255:
            find_colour[colour_channel] -= level*2
        line_colour = [255-bg_colour[0],255-bg_colour[1],255-bg_colour[2]]

        # creat the block position
        find_colour_pos_x = random.randint(0,7)*80
        find_colour_pos_y = random.randint(0,7)*80

        done = True
        while done and timer(60): 
            background(bg_colour,line_colour)
            pygame.display.set_caption(str(timer(60)))

            find_rect = pygame.Rect(find_colour_pos_x,find_colour_pos_y,80,80)
            rect_surface = screen.subsurface(find_rect)
            rect_surface.fill(find_colour)

            for line in range(0,720,80):
                pygame.draw.line(screen,line_colour,(0,line),(640,line),3)
                pygame.draw.line(screen,line_colour,(line,0),(line,640),3)
                
            # check whether it is right or wrong
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if find_rect.collidepoint((x,y)):
                        pygame.mixer.music.load('right_sound.ogg')
                        pygame.mixer.music.play()
                        transparent(rect_surface)
                        score += 1
                    else:
                        pygame.mixer.music.load('wrong_sound.ogg')
                        pygame.mixer.music.play()
                        rotate(rect_surface)
                    level -= 1
                    done = False
                    
            pygame.display.update()
    end_screen()
pygame.quit() 
                   
    




    

        

        
