def hangman(word):
    wrong = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|    l | l     ",
              "|     | |     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1:
        print("\n")
        print("予想してね\n")
        msg = "予想"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print("あなたの勝ち\n")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("あなたの負け...。正解は　{}.".format(word))
        print("\n".join(stages[0:wrong+1]))

print("player1 prease input your word:\n")
a = "answer"
word = input(a)
hangman(word)

