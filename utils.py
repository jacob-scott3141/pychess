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



