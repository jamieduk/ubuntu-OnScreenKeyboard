import pygame
import sys
import pyperclip  # For copying to clipboard

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT=800, 400
BUTTON_WIDTH, BUTTON_HEIGHT=60, 40
FONT_SIZE=24
EMOJI_SIZE=30  # Emoji size
BACKGROUND_COLOR=(30, 30, 30)
BUTTON_COLOR=(50, 50, 50)
BUTTON_HOVER_COLOR=(100, 100, 100)
TEXT_COLOR=(255, 255, 255)

# Set up the display
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("On-Screen Keyboard")
font=pygame.font.Font(None, FONT_SIZE)

# Font for emojis (ensure this path is correct)
emoji_font=pygame.font.Font("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", EMOJI_SIZE)

# Keyboard layout
keys=[
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L",
    "Z", "X", "C", "V", "B", "N", "M",
    "Space", "Caps", "Minimize", "Close"
]

# Special characters layout
special_chars=[
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\",
    ":", ";", "\"", "'", "<", ">", ",", ".", "/"
]

# Emojis layout
emojis=[
    "😀", "😁", "😂", "😃", "😄", "😅", "😆", "😇", "😉", "😊",
    "😍", "😘", "😗", "😙", "😚", "😋", "😎", "😏", "😐", "😑",
    "😶", "😏", "😣", "😥", "😮", "😯", "😲", "😴", "😵", "😡",
    "😠", "😇", "😈", "👿", "👹", "👺", "💀", "👻", "👽", "👾"
]

# Create buttons
buttons=[]
for i, key in enumerate(keys):
    x=(i % 10) * BUTTON_WIDTH + 10
    y=(i // 10) * BUTTON_HEIGHT + 100
    buttons.append((key, pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)))

# Create special character buttons
special_buttons=[]
for i, key in enumerate(special_chars):
    x=(i % 10) * BUTTON_WIDTH + 10
    y=(i // 10) * BUTTON_HEIGHT + 100
    special_buttons.append((key, pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)))

# Create emoji buttons with adjusted layout
emoji_buttons=[]
for i, emoji in enumerate(emojis):
    x=(i % 10) * BUTTON_WIDTH + 10
    y=(i // 10) * BUTTON_HEIGHT + 100 + (len(keys) // 10) * BUTTON_HEIGHT  # Start below the regular keys
    emoji_buttons.append((emoji, pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)))

# Text boxes
all_keys_text=""
last_key_text=""
text_box_rect=pygame.Rect(10, 10, WIDTH - 20, 30)
last_key_box_rect=pygame.Rect(10, 50, WIDTH - 20, 30)

# Copy buttons
copy_all_rect=pygame.Rect(WIDTH - 120, 10, 100, 30)
copy_last_rect=pygame.Rect(WIDTH - 120, 50, 100, 30)

# Tab buttons
tab_buttons=[
    pygame.Rect(10, 80, 100, 30),  # Main
    pygame.Rect(120, 80, 120, 30), # Special Characters
    pygame.Rect(250, 80, 100, 30), # Emojis
]

# Caps state
caps_lock_on=False

# Current tab
current_tab=0  # 0: Main, 1: Special Characters, 2: Emojis

# Function to toggle Caps Lock
def toggle_caps_lock():
    global caps_lock_on
    caps_lock_on=not caps_lock_on

# Function to draw buttons
def draw_buttons(button_list):
    for key, rect in button_list:
        color=BUTTON_COLOR
        if rect.collidepoint(pygame.mouse.get_pos()):
            color=BUTTON_HOVER_COLOR
        
        # Change the text based on the Caps Lock state
        display_key=key.upper() if caps_lock_on and key.isalpha() else key.lower()
        
        pygame.draw.rect(screen, color, rect)
        text_surface=font.render(display_key, True, TEXT_COLOR)
        text_rect=text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

# Function to draw emoji buttons
def draw_emoji_buttons():
    for emoji, rect in emoji_buttons:
        color=BUTTON_COLOR
        if rect.collidepoint(pygame.mouse.get_pos()):
            color=BUTTON_HOVER_COLOR
        
        pygame.draw.rect(screen, color, rect)
        emoji_surface=emoji_font.render(emoji, True, TEXT_COLOR)  # Render emoji with the specified size
        emoji_rect=emoji_surface.get_rect(center=rect.center)
        screen.blit(emoji_surface, emoji_rect)

# Function to draw copy buttons
def draw_copy_buttons():
    pygame.draw.rect(screen, BUTTON_COLOR, copy_all_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, copy_last_rect)

    all_text_surface=font.render("Copy All", True, TEXT_COLOR)
    last_text_surface=font.render("Copy Last", True, TEXT_COLOR)

    all_text_rect=all_text_surface.get_rect(center=copy_all_rect.center)
    last_text_rect=last_text_surface.get_rect(center=copy_last_rect.center)

    screen.blit(all_text_surface, all_text_rect)
    screen.blit(last_text_surface, last_text_rect)

# Function to draw tabs
def draw_tabs():
    tab_names=["Main", "Special", "Emojis"]
    for i, rect in enumerate(tab_buttons):
        color=BUTTON_COLOR if i != current_tab else BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, color, rect)
        text_surface=font.render(tab_names[i], True, TEXT_COLOR)
        text_rect=text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

# Main loop
running=True
while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Draw text boxes
    pygame.draw.rect(screen, (50, 50, 50), text_box_rect)
    pygame.draw.rect(screen, (50, 50, 50), last_key_box_rect)
    
    all_keys_surface=font.render(all_keys_text, True, TEXT_COLOR)
    last_key_surface=font.render(last_key_text, True, TEXT_COLOR)
    
    screen.blit(all_keys_surface, (text_box_rect.x + 5, text_box_rect.y + 5))
    screen.blit(last_key_surface, (last_key_box_rect.x + 5, last_key_box_rect.y + 5))
    
    # Draw tabs
    draw_tabs()

    # Draw buttons based on the current tab
    if current_tab == 0:
        draw_buttons(buttons)
    elif current_tab == 1:
        draw_buttons(special_buttons)
    elif current_tab == 2:
        draw_emoji_buttons()

    # Draw copy buttons
    draw_copy_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for i, rect in enumerate(tab_buttons):
                    if rect.collidepoint(event.pos):
                        current_tab=i

                # Check buttons in the current tab
                button_list=buttons if current_tab == 0 else special_buttons if current_tab == 1 else emoji_buttons
                for key, rect in button_list:
                    if rect.collidepoint(event.pos):
                        if key == "Space":
                            all_keys_text += " "
                            last_key_text="Space"
                        elif key == "Caps":
                            toggle_caps_lock()
                        elif key == "Minimize":
                            pygame.display.iconify()  # Minimize the window
                        elif key == "Close":
                            running=False
                        else:
                            if caps_lock_on and key.isalpha():
                                all_keys_text += key.upper()
                                last_key_text=key.upper()
                            else:
                                all_keys_text += key.lower() if key.isalpha() else key
                                last_key_text=key.lower() if key.isalpha() else key

                # Check copy buttons
                if copy_all_rect.collidepoint(event.pos):
                    pyperclip.copy(all_keys_text)
                if copy_last_rect.collidepoint(event.pos):
                    pyperclip.copy(last_key_text)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False

    pygame.display.flip()

pygame.quit()
sys.exit()

