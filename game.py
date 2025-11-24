import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("XO Game")
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size = 200
board = [["","",""] ,
        ["","",""] ,
        ["","",""]]
player = "X"
font = pygame.font.Font(None, 100)
run = True
while run:
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (200,0), (200,600), 6)
    pygame.draw.line(screen, WHITE, (400,0), (400,600), 6)
    pygame.draw.line(screen, WHITE, (0,200), (600,200), 6)
    pygame.draw.line(screen, WHITE, (0,400), (600,400), 6)
    for row in range(3):
        for col in range(3) :
            if board[row][col] != "":
                text = font.render(board[row][col], True,RED)
                screen.blit(text, (col * size + 70), (row * size + 50))
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x , mouse_y = pygame.mouse.get_pos()
                row = mouse_y //200
                col = mouse_x //200
                if board[row][col]=="":
                    board[row][col]== player
                    if player == "X":
                        player = "O"
                    else :
                        player = "X"
    pygame.display.update()
pygame.quit()