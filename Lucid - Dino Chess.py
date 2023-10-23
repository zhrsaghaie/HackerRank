# Lucid - Dino Chess
n , m = map(int, input().split())

board = [[0 for i in range(n)] for j in range(n)]

dino = 0
for i in range(n):
    for j in range(n):
        if i % (2*m) < m and j %(2*m) < m:
            board[i][j] = 1
        else: 
            board[i][j] = 0


# for i in range(n):
#     print (board[i])


print(sum(sum(board,[])))
