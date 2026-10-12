def print_board(board):
    n = len(board)

    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):

    # cek kolom atas
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # cek diagonal kiri atas
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # cek diagonal kanan atas
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True



def solve_nqueen(board, row, n):
    # jika semua ratu berhasil ditempatkan
    if row == n:
        print("Solusi ditemukan:")
        print_board(board)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            # 1. TEMPATKAN RATU
            board[row][col] = 'Q'
            # TAMBAHKAN OUTPUT INI: Menampilkan posisi (baris, kolom) saat menempatkan Q
            print(f"Menempatkan Q di ({row},{col})")
            
            # rekursi ke baris berikutnya
            solve_nqueen(board, row + 1, n)
            
            # 2. BACKTRACKING
            board[row][col] = '.'
            # TAMBAHKAN OUTPUT INI: Menampilkan posisi (baris, kolom) saat menghapus Q
            print(f"Backtrack dari ({row},{col})")


n = int(input("Masukkan nilai N (ukuran papan catur): "))

board = []

for i in range(n):
    board.append(['.' for j in range(n)])

solve_nqueen(board, 0, n)
