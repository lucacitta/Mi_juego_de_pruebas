import pygame

def draw_text(text, font, text_color, surface, x, y, bg_color=None, line_spacing=5):
    # Dividir el texto en líneas si hay saltos de línea o si es muy largo
    lines = text.splitlines()

    for i, line in enumerate(lines):
        textobj = font.render(line, True, text_color)
        textrect = textobj.get_rect(center=(x, y + i * (font.get_height() + line_spacing)))

        # Si se proporciona un color de fondo, dibuja un rectángulo detrás del texto
        if bg_color:
            bg_rect = textrect.inflate(10, 10)
            pygame.draw.rect(surface, bg_color, bg_rect)

        # Dibuja el texto en la superficie
        surface.blit(textobj, textrect)
