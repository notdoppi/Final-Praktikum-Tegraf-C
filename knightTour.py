MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

def inside(x, y, n):
    return 0 <= x < n and 0 <= y < n

def degree(x, y, board, n):
    cnt = 0
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if inside(nx, ny, n) and board[nx][ny] == -1:
            cnt += 1
    return cnt

def next_moves(x, y, board, n):
    nxt = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if inside(nx, ny, n) and board[nx][ny] == -1:
            nxt.append((nx, ny))
    nxt.sort(key=lambda pos: degree(pos[0], pos[1], board, n))
    return nxt

def knight_tour(n=8, start=(0,0), closed=False):
    board = [[-1]*n for _ in range(n)]
    sr, sc = start
    sx, sy = sc, sr
    board[sx][sy] = 0
    path = [(sx, sy)]
    total = n*n

    def backtrack(x, y, step):
        if step == total:
            if not closed:
                return True
            for dx, dy in MOVES:
                if x + dx == sx and y + dy == sy:
                    return True
            return False

        for nx, ny in next_moves(x, y, board, n):
            board[nx][ny] = step
            path.append((nx, ny))
            if backtrack(nx, ny, step + 1):
                return True
            path.pop()
            board[nx][ny] = -1

        return False

    if backtrack(sx, sy, 1):
        return board
    return None

def print_board(board):
    size = len(board)
    width = len(str(size*size))
    for r in range(size):
        print(" ".join(str(board[r][c]).rjust(width) for c in range(size)))


# ======== MAIN PROGRAM ========

n = 8
x = int(input("Start X (0-7): "))
y = int(input("Start Y (0-7): "))
jenis = input("closed atau open? (c/o): ")

closed = (jenis.lower() == 'c')

print("\nMencari tour...\n")
result = knight_tour(n=n, start=(x,y), closed=closed)

if result:
    print("Tour ditemukan:\n")
    print_board(result)
else:
    print("Tidak ditemukan tour dari posisi itu.")
