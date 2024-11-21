import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Tool")
screen.fill((255, 255, 255))

current_tool = "rectangle" 
draw_color = (255, 0, 0) 
brush_size = 5
start_pos = None

print("Press R for Rectangle, C for Circle, E for Eraser, B for Brush")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_tool = "rectangle"
                print("Selected tool: Rectangle")
            elif event.key == pygame.K_2:
                draw_color = (0,255,0)
                print("Selected color: Green")
            elif event.key == pygame.K_1:
                draw_color = (255,0,0)
                print("Selected color: Red")
            elif event.key == pygame.K_3:
                draw_color = (0,0,255)
                print("Selected color: Blue")
            elif event.key == pygame.K_c:
                current_tool = "circle"
                print("Selected tool: Circle")
            elif event.key == pygame.K_e:
                current_tool = "eraser"
                print("Selected tool: Eraser")
            elif event.key == pygame.K_b:
                current_tool = "brush"
                print("Selected tool: Brush")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and current_tool == "brush":
                pygame.draw.circle(screen, draw_color, event.pos, brush_size)
            if pygame.mouse.get_pressed()[0] and current_tool == "eraser":
                pygame.draw.circle(screen, (255,255,255), event.pos, 50)
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if current_tool == "rectangle":
                pygame.draw.rect(screen, draw_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
            elif current_tool == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5 / 2)
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(screen, draw_color, center, radius)

    pygame.display.flip()

pygame.quit()
sys.exit()