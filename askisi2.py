import random
 
 
def draw_board(board):
    print('\n')
    print(' 7' + ' '*4 + '|' + '8' + ' '*4 + '|' + '9' + ' '*4)
    print('   ' + board[7] + '  ' + '|' + '  ' + board[8] + '  ' + '|' + '  ' + board[9] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print(' -----+-----+-----')
    print(' 4' + ' '*4 + '|' + '5' + ' '*4 + '|' + '6' + ' '*4)
    print('   ' + board[4] + '  ' + '|' + '  ' + board[5] + '  ' + '|' + '  ' + board[6] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print(' -----+-----+-----')
    print(' 1' + ' '*4 + '|' + '2' + ' '*4 + '|' + '3' + ' '*4)
    print('   ' + board[1] + '  ' + '|' + '  ' + board[2] + '  ' + '|' + '  ' + board[3] + '  ')
    print(' '*6 + '|' + ' '*5 + '|' + ' '*5)
    print('\n')
 
 
def player_sign():
    sign = ''
    while not (sign == 'X' or sign == 'O' or sign == 'Χ' or sign == 'Ο'):
        print('Διάλεξε με ποιό γράμμα θες να πέξεις το Χ ή με το Ο;')
        sign = input().upper()

    if sign == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
 
def whos_turn():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
 
def make_move(board, sign, move):
    board[move] = sign
 
 
def win(board, mark): 
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))
 
def copy_board(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
 
def free_space(board, move):
    return board[move] == ' '
 
def player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        print('Ποιά θα είναι η επόμενη σας κίνηση; [1-9]: ')
        move = input()
    return int(move)
 
def random_move(board, movesList):
    possibleMoves = []
    for i in movesList:
        if free_space(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def computer_move(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = copy_board(board)
        if free_space(boardCopy, i):
            make_move(boardCopy, computerLetter, i)
            if win(boardCopy, computerLetter):
                return i
 
    for i in range(1, 10):
        boardCopy = copy_board(board)
        if free_space(boardCopy, i):
            make_move(boardCopy, playerLetter, i)
            if win(boardCopy, playerLetter):
                return i
 
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    if free_space(board, 5):
        return 5

    return random_move(board, [2, 4, 6, 8])
 
def full_board(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True
 
 
print('Καλωσήρθατε στο παιχνίδι!')
 
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = player_sign()
    turn = whos_turn()
    print('Πρώτος παίζει: ' + turn)
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'player':
            draw_board(theBoard)
            move = player_move(theBoard)
            make_move(theBoard, playerLetter, move)
 
            if win(theBoard, playerLetter):
                draw_board(theBoard)
                print('Συγχαρητήρια! Νίκησες.')
                gameIsPlaying = False
            else:
                if full_board(theBoard):
                    draw_board(theBoard)
                    print('Ισοπαλία!')
                    break
                else:
                    turn = 'computer'
 
        else:
            move = computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)
 
            if win(theBoard, computerLetter):
                draw_board(theBoard)
                print('Νικητής το computer!!! try agian next time')
                gameIsPlaying = False
            else:
                if full_board(theBoard):
                    draw_board(theBoard)
                    print('Ισοπαλία!')
                    break
                else:
                    turn = 'player'
 
    print('Θέλετε να ξαναπαίξετε; (Ναι/Όχι): ')
    if not input().lower().startswith('ν'):
        break