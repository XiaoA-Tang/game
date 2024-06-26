import pygame

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_text_centered(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def draw_button(text, x, y, w, h, color, hover_color, action=None):
    screen = pygame.display.get_surface()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    small_text = pygame.font.SysFont("simhei", 20)
    draw_text(text, small_text, (0, 0, 0), screen, x + 10, y + 10)

def draw_score(start_time, font, color, surface, x, y):
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # 转换为秒
    score_text = f"得分：{elapsed_time}"
    draw_text(score_text, font, color, surface, x, y)
