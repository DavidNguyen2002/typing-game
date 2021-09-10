import pygame
from random import random

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

x_size = 800
y_size = 600
red = (255, 0, 0)

dis = pygame.display.set_mode((x_size, y_size))
pygame.display.set_caption('Typing Game')

def new_word():
    file = open('1-1000.txt')
    word = file.readlines()[int(random() * 1000)][:-1]
    file.close()
    return word

game_over = False
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
end_buffer = 0
word = new_word()
text_surface = my_font.render(word, False, red)
dis.blit(text_surface, (100, 100))
score = 0

while not game_over:
    seconds = (pygame.time.get_ticks() - start_time) / 1000
    for event in pygame.event.get():
        if seconds >= 10 + end_buffer:
            game_over = True
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key), word)
            if pygame.key.name(event.key) == word[0]:
                word = word[1:]
                if len(word) == 0:
                    score += 1
                    word = new_word()
                    end_buffer += 1
            else:
                end_buffer -= 1
    dis.fill((173, 216, 230))
    text_surface = my_font.render(word, False, red)
    dis.blit(text_surface, (100, 100))
    score_surface = my_font.render("Score: {}".format(score), False, red)
    dis.blit(score_surface, (400, 100))
    time_surface = my_font.render("Time: {}".format(10 + end_buffer - seconds), False, red)
    dis.blit(time_surface, (400, 200))
    pygame.display.update()
    clock.tick(15)

show = True
while show:
    dis.fill((173, 216, 230))
    dis.blit(my_font.render("Your score is {}".format(score), False, (0,0,0)), [x_size / 2, y_size / 2])
    dis.blit(my_font.render("Press any button to quit", False, (0,0,0)), [x_size / 2, 100 + (y_size / 2)])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            show = False
                
pygame.quit()
quit()