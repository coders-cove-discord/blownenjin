import pygame

# Initialize Pygame
pygame.init()

# Set up display (not required for key mapping)
screen = pygame.display.set_mode((800, 600))

# Dictionary mapping Pygame key values to key labels
key_map = {
    # esc key is special so it gets its own category of autism!
    pygame.K_ESCAPE: 'Escape',
    # alphanumericals
    pygame.K_a: 'A',
    pygame.K_b: 'B',
    pygame.K_c: 'C',
    pygame.K_d: 'D',
    pygame.K_e: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_i: 'I',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_m: 'M',
    pygame.K_n: 'N',
    pygame.K_o: 'O',
    pygame.K_p: 'P',
    pygame.K_q: 'Q',
    pygame.K_r: 'R',
    pygame.K_s: 'S',
    pygame.K_t: 'T',
    pygame.K_u: 'U',
    pygame.K_v: 'V',
    pygame.K_w: 'W',
    pygame.K_x: 'X',
    pygame.K_y: 'Y',
    pygame.K_z: 'Z',
    # numbers
    pygame.K_0: '0',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9',
    # function keys
    pygame.K_F1: 'F1',
    pygame.K_F2: 'F2',
    pygame.K_F3: 'F3',
    pygame.K_F4: 'F4',
    pygame.K_F5: 'F5',
    pygame.K_F6: 'F6',
    pygame.K_F7: 'F7',
    pygame.K_F8: 'F8',
    pygame.K_F9: 'F9',
    pygame.K_F10: 'F10',
    pygame.K_F11: 'F11',
    pygame.K_F12: 'F12',
    #other non important autism
    pygame.K_KP_ENTER: "ENTER",
    pygame.K_BACKSPACE: "BACKSPACE",
    pygame.K_LSHIFT: "LEFTSHIFT",
    pygame.K_RSHIFT: "RIGHTSHIFT"
}

# Example usage: check if a key is pressed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    for key, label in key_map.items():
        if keys[key]:
            print(f"{label} key pressed")

pygame.quit()