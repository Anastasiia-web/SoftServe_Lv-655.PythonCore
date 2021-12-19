# https://pythonguides.com/python-pygame-tutorial/   Explanation

# import pygame  

# pygame.init()  
# scr = pygame.display.set_mode((600,500))  
# pygame.display.set_caption('Pygame Window')

# done = False  
# while not done:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             done = True  
# pygame.display.flip() 
#___________________
# import os
# import pygame
# import time
# X = 100
# Y = 100
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
# pygame.init()
# win_screen = pygame.display.set_mode((500,500))
# time.sleep(2)

#__________
# import pygame         # size of the screen
# pygame.init() 
# scr = pygame.display.set_mode()
# x, y = scr.get_size() 
# pygame.display.quit() 
# print(x, y) 
#_______-
# import pygame                         # resizable screen
# scr = pygame.display.set_mode((800, 700),pygame.RESIZABLE) 
# pygame.display.set_caption('Resizable Window') 
# running = True
# while running: 
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             running = False
# pygame.quit() 

#__________
# import pygame      #  adding circle
# pygame.init()
# scr = pygame.display.set_mode((600, 500))
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     scr.fill((255, 255, 255))
#     pygame.draw.circle(scr, (20, 150, 0), (170, 120), 20)         # 1 = color ; 2 = where it is ; 3 - size
#     pygame.display.flip()
# pygame.quit()

#________
# https://www.javatpoint.com/pygame

# with background

# import pygame  
# pygame.init()  
# white = (255, 255, 255)  
# # assigning values to height and width variable   
# height = 400  
# width = 400  
# # creating the display surface object   
# # of specific dimension..e(X, Y).   
# display_surface = pygame.display.set_mode((height, width))  
  
# # set the pygame window name   
# pygame.display.set_caption('Image')  
  
# # creating a surface object, image is drawn on it.   
# image = pygame.image.load('underReconstruction\pygame_image.png')  
  
# # infinite loop   
# while True:  
#     display_surface.fill(white)  
#     display_surface.blit(image, (0, 0))  
  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             pygame.quit()  
#             # quit the program.   
#             quit()  
#         # Draws the surface object to the screen.   
#         pygame.display.update()   
#______________________-
# with greeting

# import pygame  
# pygame.init()  
# screen = pygame.display.set_mode((640, 480))  
# done = False  
  
# #load the fonts  
# font = pygame.font.SysFont("Times new Roman", 72)  
# # Render the text in new surface  
# text = font.render("Hello, Pygame", True, (158, 16, 16))  
# while not done:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             done = True  
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
#             done = True  
#     screen.fill((255, 255, 255))  
#     #We will discuss blit() in the next topic  
#     screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))  
  
#     pygame.display.flip()  
#_________
# Typing game with eplanation 
# https://itsourcecode.com/free-projects/python-projects/speed-typing-test-python-project-with-source-code/

# Source Code of Flappy Bird Game in Python
# https://itsourcecode.com/free-projects/python-projects/flappy-bird-game-in-python-with-source-code/

# https://github.com/pygame/parrotjoy