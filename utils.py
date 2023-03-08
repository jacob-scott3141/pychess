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

def isInCheck(king, pieces, isWhite):
    team = "w" if isWhite else "b"
    oppo = "b" if isWhite else "w"
    x, y = king

    # Check knight moves
    knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for move in knight_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
            if get_piece_at(new_x, new_y, pieces) == oppo + "n":
                return True

    # Check pawn
    pawn_moves = [(1, -1), (-1, -1)] if team == "w" else [(1, 1), (-1, 1)]
    for move in pawn_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        p = get_piece_at(new_x, new_y, pieces)
        if p == oppo + "p":
            return True

    # Check king
    king_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for move in pawn_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
            p = get_piece_at(new_x, new_y, pieces)
            if p == oppo + "p":
                return True
    
    # Top left, top, top right
    tl, tr, bl, br, t, r, l, b = True, True, True, True, True, True, True, True
    
    for i in range(1, 8):
        if tl:
            new_x = x - i
            new_y = y + i

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    tl = False
                elif p == oppo + "b" or p == oppo + "q":
                    return True
                else:
                    tl = False

        if t:
            new_x = x
            new_y = y + i

            if new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    t = False
                elif p == oppo + "r" or p == oppo + "q":
                    return True
                else:
                    t = False
        
        if tr:
            new_x = x + i
            new_y = y + i

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    tr = False
                elif p == oppo + "b" or p == oppo + "q":
                    return True
                else:
                    tr = False
        if bl:
            new_x = x - i
            new_y = y - i

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    bl = False
                elif p == oppo + "b" or p == oppo + "q":
                    return True
                else:
                    bl = False

        if b:
            new_x = x
            new_y = y - i

            if new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    b = False
                elif p == oppo + "r" or p == oppo + "q":
                    return True
                else:
                    b = False
        
        if br:
            new_x = x + i
            new_y = y - i

            if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    br = False
                elif p == oppo + "b" or p == oppo + "q":
                    return True
                else:
                    br = False

        if l:
            new_x = x - i
            new_y = y

            if new_x >= 0 and new_x <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    l = False
                elif p == oppo + "r" or p == oppo + "q":
                    return True
                else:
                    l = False
        if r:
            new_x = x + i
            new_y = y

            if new_x >= 0 and new_x <= 7:
                p = get_piece_at(new_x, new_y, pieces)
                if p == "":
                    pass
                elif p[0] == team:
                    r = False
                elif p == oppo + "r" or p == oppo + "q":
                    return True
                else:
                    r = False
    return False

def move_pawn(piece_name, pieces, x, y, last_move):
    en_passant = (None, None, None)
    # Determine the type of piece
    if piece_name == "wp":
        # White pawn
        possible_moves = []

        last_piece, last_position_from, last_position_to = last_move
        if last_piece == "bp" and last_position_from[1] == 1 and last_position_to[1] == 3 and y == 3 and (x == last_position_to[0] + 1 or x == last_position_to[0] - 1):
            en_passant = ("wp", (x, y), (last_position_to[0], 2))
            print("en passant: ", en_passant)
            possible_moves.append((last_position_to[0], 2))
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
        return possible_moves, en_passant

    elif piece_name == "bp":
        # Black pawn
        possible_moves = []

        last_piece, last_position_from, last_position_to = last_move
        if last_piece == "wp" and last_position_from[1] == 6 and last_position_to[1] == 4 and y == 4 and (x == last_position_to[0] + 1 or x == last_position_to[0] - 1):
            en_passant = ("bp", (x, y), (last_position_to[0], 5))
            print(en_passant)
            possible_moves.append((last_position_to[0], 5))
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
        return possible_moves, en_passant

def check_ksc(piece_name, pieces):
    team = piece_name[0]
    ksc = [(5, 7), (6, 7)] if team == "w" else [(5, 0), (6, 0)]
    oppo = "b" if team == "w" else "w"
        
    # Check that the spaces are free
    for p_x, p_y in ksc:
        if get_piece_at(p_x, p_y, pieces) != "":
            return None

    for i in range(2):
        x, y = ksc[i]

        # Check knight moves
        knight_moves = [(1, -2), (2, -1), (-1, -2), (-2, -1)] if team == "w" else [(1, 2), (2, 1), (-1, 2), (-2, 1)]
        for move in knight_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x >= 0 and new_x <= 7:
                if get_piece_at(new_x, new_y, pieces) == oppo + "n":
                    return None

        # Check pawn and king moves
        pawn_moves = [(1, -1), (-1, -1)] if team == "w" else [(1, 1), (-1, 1)]
        for move in pawn_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            p = get_piece_at(new_x, new_y, pieces)
            if p == oppo + "p" or p == oppo + "k":
                return None

        # Check final king move
        new_x = x
        new_y = y + (-1 if team == "w" else 1)
        p = get_piece_at(new_x, new_y, pieces)
        if p == oppo + "k":
            return None
        
        # Top left, top, top right
        tl, t, tr = True, True, True
        
        dir = -1 if team == "w" else 1
        
        for i in range(1, 8):
            if tl:
                new_x = x - i
                new_y = y + dir*i

                if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        tl = False
                    elif p == oppo + "b" or p == oppo + "q":
                        return None
                    else:
                        tl = False

            if t:
                new_x = x
                new_y = y + dir*i

                if new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        t = False
                    elif p == oppo + "r" or p == oppo + "q":
                        return None
                    else:
                        t = False
            
            if tr:
                new_x = x + i
                new_y = y + dir*i

                if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        tr = False
                    elif p == oppo + "b" or p == oppo + "q":
                        return None
                    else:
                        tr = False

    return ksc[1]

def check_qsc(piece_name, pieces):
    team = piece_name[0]
    qsc = [(2, 7), (3, 7)] if team == "w" else [(2, 0), (3, 0)]
    oppo = "b" if team == "w" else "w"
        
    # Check that the spaces are free
    for p_x, p_y in qsc:
        if get_piece_at(p_x, p_y, pieces) != "":
            return None

    for i in range(2):
        x, y = qsc[i]
        
        knight_moves = [(1, -2), (2, -1), (-1, -2), (-2, -1)] if team == "w" else [(1, 2), (2, 1), (-1, 2), (-2, 1)]
        for move in knight_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if new_x >= 0 and new_x <= 7:
                if get_piece_at(new_x, new_y, pieces) == oppo + "n":
                    return None

        # Check pawn and king moves
        pawn_moves = [(1, -1), (-1, -1)] if team == "w" else [(1, 1), (-1, 1)]
        for move in pawn_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            p = get_piece_at(new_x, new_y, pieces)
            if p == oppo + "p" or p == oppo + "k":
                return None

        # Check final king move
        new_x = x
        new_y = y + (-1 if team == "w" else 1)
        p = get_piece_at(new_x, new_y, pieces)
        if p == oppo + "k":
            return None
        
        # Top left, top, top right
        tl, t, tr = True, True, True
        
        dir = -1 if team == "w" else 1
        
        for i in range(1, 8):
            if tl:
                new_x = x - i
                new_y = y + dir*i

                if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        tl = False
                    elif p == oppo + "b" or p == oppo + "q":
                        return None
                    else:
                        tl = False

            if t:
                new_x = x
                new_y = y + dir*i

                if new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        t = False
                    elif p == oppo + "r" or p == oppo + "q":
                        return None
                    else:
                        t = False
            
            if tr:
                new_x = x + i
                new_y = y + dir*i

                if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
                    p = get_piece_at(new_x, new_y, pieces)
                    if p == "":
                        pass
                    elif p[0] == team:
                        tr = False
                    elif p == oppo + "b" or p == oppo + "q":
                        return None
                    else:
                        tr = False
    return qsc[0]

def move_king(piece_name, pieces, x, y, castle_state):
    castle = [(None, None, None), (None, None, None)]
    # King
    possible_moves = []
    king_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for move in king_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if new_x >= 0 and new_x <= 7 and new_y >= 0 and new_y <= 7:
            if pieces[new_y * 8 + new_x] == "" or pieces[new_y * 8 + new_x][0] != piece_name[0]:
                possible_moves.append((new_x, new_y))

    # Check king side castle
    if castle_state[0]:
        ksc = check_ksc(piece_name, pieces)
        if ksc is not None:
            possible_moves.append(ksc)
            castle[0] = (piece_name, (x, y), ksc)

    # Check queen side castle
    if castle_state[1]:
        qsc = check_qsc(piece_name, pieces)
        if qsc is not None:
            possible_moves.append(qsc)
            castle[1] = (piece_name, (x, y), qsc)
            
    return possible_moves, castle

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

