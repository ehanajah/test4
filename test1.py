import pygame

def rotate_surf(screen, surf_rect, topleft, angle):
    rotated_surf_rect = pygame.transform.rotate(surf_rect, angle)
    new_rect = rotated_surf_rect.get_rect(center = surf_rect.get_rect(topleft = topleft).center)

    screen.blit(rotated_surf_rect, new_rect.topleft)

def main():
    SURFACE_SIZE = 500
    RECT_W = 300
    RECT_H = 100
    TOPLEFT_SURFACE = (200, 200)
    TOPLEFT_RECT = (SURFACE_SIZE//2 - RECT_W//2, 
                SURFACE_SIZE//2 - RECT_H//2)

    pygame.init()
    screen = pygame.display.set_mode((1910, 1040))
    clock = pygame.time.Clock()
    running = True
    # rects = create_diagonal_rect(500)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        surf = pygame.Surface((SURFACE_SIZE, SURFACE_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(surf, (107, 50, 207), pygame.Rect(TOPLEFT_RECT,(RECT_W, RECT_H)), 3)

        # screen.blit(surf, TOPLEFT_SURFACE)

        for angle in range(0, -81, -15):
            rotate_surf(screen, surf, TOPLEFT_SURFACE, angle)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()