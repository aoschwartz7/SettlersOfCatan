import pygame

# Initialize pygame module
pygame.init()

white = (255,255,255)
black = (0, 0, 0)

# Set polygon vertices
v1=(600,463)
v2=(500,463)
v3=(450,550)
v4=(500,637)
v5=(600,637)
v6=(650,550)

# Create screen / gameDisplay
gameDisplay = pygame.display.set_mode((1000,800))

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    # Fill screen white
    gameDisplay.fill(white)
    # Draw hexagon on screen
    hexPiece = pygame.draw.polygon(gameDisplay, black, (v1,v2,v3,v4,v5,v6))
    # Update screen
    pygame.display.update()

pygame.quit()
quit()
