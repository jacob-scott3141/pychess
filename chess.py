import pygame

# Initialize Pygame
pygame.init()

# Define the size of the chess board
board_size = 700

# Create the Pygame display
screen = pygame.display.set_mode((board_size, board_size))

# Define colors
white = (255, 255, 255)
black = (90, 90, 150)

debug = True

def log(msg):
    if debug:
        print(msg)

# Load the chess piece images
wp = pygame.image.load("wp.png")
wr = pygame.image.load("wr.png")
wn = pygame.image.load("wn.png")
wb = pygame.image.load("wb.png")
wq = pygame.image.load("wq.png")
wk = pygame.image.load("wk.png")
bp = pygame.image.load("bp.png")
br = pygame.image.load("br.png")
bn = pygame.image.load("bn.png")
bb = pygame.image.load("bb.png")
bq = pygame.image.load("bq.png")
bk = pygame.image.load("bk.png")

# Create a dictionary to map piece names to their images
piece_images = {
    "wp": wp,
    "wr": wr,
    "wn": wn,
    "wb": wb,
    "wq": wq,
    "wk": wk,
    "bp": bp,
    "br": br,
    "bn": bn,
    "bb": bb,
    "bq": bq,
    "bk": bk,
}

# Define the starting position of the pieces
pieces = [
    "br", "bn", "bb", "bq", "bk", "bb", "bn", "br",
    "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",
    "wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr",
]

def print_board():
    s = ""
    for i in range(8):
        for j in range(8):
            p = pieces[i * 8 + j]
            if p == "":
                p = "  "
            s += p + " "
        s += "\n"
    return s

# Define the size of the chess squares
square_size = board_size / 8

# Define the font for the coordinates
font = pygame.font.SysFont("Arial", 20)

# Draw the chess board and pieces
for i in range(8):
    for j in range(8):
        # Calculate the position of the square
        x = j * square_size
        y = i * square_size

        # Determine the color of the square
        if (i + j) % 2 == 0:
            color = white
        else:
            color = black

        # Draw the square
        pygame.draw.rect(screen, color, [x, y, square_size, square_size])

        # Draw the piece, if there is one
        piece_name = pieces[i * 8 + j]
        if piece_name != "":
            piece_image = piece_images[piece_name]
            piece_rect = piece_image.get_rect()
            piece_rect.center = (x + square_size / 2, y + square_size / 2)
            screen.blit(piece_image, piece_rect)

        # Draw the coordinates
        if j == 0:
            label = font.render(str(8 - i), True, black)
            screen.blit(label, (x - 20, y + square_size / 2 - 10))
        if i == 7:
            label = font.render(chr(j + 97), True, black)
            screen.blit(label, (x + square_size / 2 - 10, y + square_size + 10))

# Update the display
pygame.display.flip()

# Define variables for tracking the current piece and its position
current_piece = None
current_piece_position = None

# Run the Pygame event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handle mouse button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position in terms of the chess board
            mouse_x, mouse_y = pygame.mouse.get_pos()
            board_x = int(mouse_x // square_size)
            board_y = int(mouse_y // square_size)

            # Get the name and position of the piece at the mouse position
            piece_name = pieces[board_y * 8 + board_x]
            piece_position = (board_x, board_y)

            # If there is a piece at the mouse position, pick it up
            if piece_name != "":
                current_piece = piece_name
                current_piece_position = piece_position

        elif event.type == pygame.MOUSEBUTTONUP:
            # If there is a current piece, try to move it to the new position
            if current_piece is not None:
                # Get the mouse position in terms of the chess board
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board_x = int(mouse_x // square_size)
                board_y = int(mouse_y // square_size)
                log("picked up piece")

                # Get the name and position of the piece at the new position
                new_piece_name = pieces[board_y * 8 + board_x]
                new_piece_position = (board_x, board_y)

                # If there is no piece at the new position, move the current piece there
                if new_piece_name == "":
                    pieces[board_y * 8 + board_x] = current_piece
                    pieces[current_piece_position[1] * 8 + current_piece_position[0]] = ""
                    log("moved piece")
                # Otherwise, if there is an enemy piece at the new position, capture it and move the current piece there
                elif current_piece[0] != new_piece_name[0]:
                    pieces[board_y * 8 + board_x] = current_piece
                    pieces[current_piece_position[1] * 8 + current_piece_position[0]] = ""
                    log("taken piece")
                # Otherwise, move the current piece back to its original position
                else:
                    pieces[current_piece_position[1] * 8 + current_piece_position[0]] = current_piece

                # Clear the current piece
                current_piece = None
                current_piece_position = None
                log(print_board())

    # Draw the chess board and pieces
    for i in range(8):
        for j in range(8):
            # Calculate the position of the square
            x = j * square_size
            y = i * square_size

            # Determine the color of the square
            if (i + j) % 2 == 0:
                color = white
            else:
                color = black

            # Draw the square
            pygame.draw.rect(screen, color, [x, y, square_size, square_size])

            # Draw the piece, if there is one
            piece_name = pieces[i * 8 + j]
            if piece_name != "":
                piece_image = piece_images[piece_name]
                piece_rect = piece_image.get_rect()
                piece_rect.center = (x + square_size / 2, y + square_size / 2)
                screen.blit(piece_image, piece_rect)

            # Draw the coordinates
            if j == 0:
                label = font.render(str(8 - i), True, black)
                screen.blit(label, (x - 20, y + square_size / 2 - 10))
            if i == 7:
                label = font.render(chr(j + 97), True, black)
                screen.blit(label, (x + square_size / 2 - 10, y + square_size + 10))
                
    pygame.display.flip()
    

