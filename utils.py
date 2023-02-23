def print_board(pieces):
    s = ""
    for i in range(8):
        for j in range(8):
            p = pieces[i * 8 + j]
            if p == "":
                p = "  "
            s += p + " "
        s += "\n"
    return s

def get_piece_at(x, y, pieces):
    return pieces[y * 8 + x]

def is_opposition(piece, oppo):
    if (piece[0] == "w" and oppo[0] == "b") or (piece[0] == "b" and oppo[0] == "w"):
        return True
    return False

def move_king(piece_name, pieces, x, y):
    # King
    possible_moves = []
    king_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for move in king_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
            if pieces[new_y * 8 + new_x] == "" or pieces[new_y * 8 + new_x][0] != piece_name[0]:
                possible_moves.append((new_x, new_y))
    return possible_moves

def move_knight(piece_name, pieces, x, y):
    possible_moves = []
    knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for move in knight_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
            if pieces[new_y * 8 + new_x] == "" or pieces[new_y * 8 + new_x][0] != piece_name[0]:
                possible_moves.append((new_x, new_y))
    return possible_moves

def move_queen(piece_name, pieces, x, y):
    return move_rook(piece_name, pieces, x, y) + move_bishop(piece_name, pieces, x, y)

def move_rook(piece_name, pieces, x, y):
    r, l, b, t = True, True, True, True

    possible_moves = []

    for i in range(1,8):
        # Check top
        if t and y-i >= 0:
            piece = get_piece_at(x , y-i, pieces)
            if piece == "":
                possible_moves.append((x, y-i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x, y-i))
                t = False
            else:
                t = False
        else:
            t = False

        # Check right
        if r and x+i <= 7:
            piece = get_piece_at(x+i , y, pieces)
            if piece == "":
                possible_moves.append((x+i, y))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x+i, y))
                r = False
            else:
                r = False
        else:
            r = False

        # Check bottom
        if b and y+i <= 7:
            piece = get_piece_at(x , y+i, pieces)
            if piece == "":
                possible_moves.append((x, y+i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x, y+i))
                b = False
            else:
                b = False
        else:
            b = False

        # Check left
        if l and x-i >= 0:
            piece = get_piece_at(x-i , y, pieces)
            if piece == "":
                possible_moves.append((x-i, y))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x-i, y))
                l = False
            else:
                l = False
        else:
            l = False
    return possible_moves

def move_bishop(piece_name, pieces, x, y):
    tr, tl, br, bl = True, True, True, True

    possible_moves = []

    for i in range(1,8):
        # Check top left
        if tl and x-i >= 0 and y-i >= 0:
            piece = get_piece_at(x-i , y-i, pieces)
            if piece == "":
                possible_moves.append((x-i, y-i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x-i, y-i))
                tl = False
            else:
                tl = False
        else:
            tl = False

        # Check top right
        if tr and x+i <= 7 and y-i >= 0:
            piece = get_piece_at(x+i , y-i, pieces)
            if piece == "":
                possible_moves.append((x+i, y-i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x+i, y-i))
                tr = False
            else:
                tr = False
        else:
            tr = False

        # Check bottom left
        if bl and x-i >= 0 and y+i <= 7:
            piece = get_piece_at(x-i , y+i, pieces)
            if piece == "":
                possible_moves.append((x-i, y+i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x-i, y+i))
                bl = False
            else:
                bl = False
        else:
            bl = False

        # Check top left
        if br and x+i <= 7 and y+i <= 7:
            piece = get_piece_at(x+i , y+i, pieces)
            if piece == "":
                possible_moves.append((x+i, y+i))
            elif is_opposition(piece_name, piece):
                possible_moves.append((x+i, y+i))
                br = False
            else:
                br = False
        else:
            br = False
    return possible_moves
            
            

def move_pawn(piece_name, pieces, x, y):
    # Determine the type of piece
    if piece_name == "wp":
        # White pawn
        possible_moves = []
        print(print_board(pieces))
        print(x, y)
        if y > 0 and get_piece_at(x, y-1, pieces) == "":
            # The pawn can move one square forward
            possible_moves.append((x, y-1))
            
            if y == 6:
                # If the pawn is on its starting square, it can move two squares forward
                if get_piece_at(x, y-2, pieces) == "":
                    possible_moves.append((x, y-2))
        if x > 0 and y > 0:
            take_piece = get_piece_at(x-1, y-1, pieces)
            if take_piece != "" and take_piece[0] == "b":
                # The pawn can capture an enemy piece to its left
                possible_moves.append((x-1, y-1))
        if x < 7 and y > 0:
            take_piece = get_piece_at(x+1, y-1, pieces)
            if take_piece != "" and take_piece[0] == "b":
                # The pawn can capture an enemy piece to its left
                possible_moves.append((x+1, y-1))
        return possible_moves

    elif piece_name == "bp":
        # Black pawn
        possible_moves = []
        print(x, y)
        if y < 7 and get_piece_at(x, y+1, pieces) == "":
            # The pawn can move one square forward
            possible_moves.append((x, y+1))
            
            if y == 1:
                # If the pawn is on its starting square, it can move two squares forward
                if get_piece_at(x, y+2, pieces) == "":
                    possible_moves.append((x, y+2))
        if x > 0 and y < 7:
            take_piece = get_piece_at(x-1, y+1, pieces)
            if take_piece != "" and take_piece[0] == "w":
                # The pawn can capture an enemy piece to its left
                possible_moves.append((x-1, y+1))
        if x < 7 and y < 7:
            take_piece = get_piece_at(x+1, y+1, pieces)
            if take_piece != "" and take_piece[0] == "w":
                # The pawn can capture an enemy piece to its left
                possible_moves.append((x+1, y+1))
        return possible_moves



