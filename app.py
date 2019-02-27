from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ruch_sign = 'x'

board = [[[' ' for x in range(3)] for y in range(3)] for z in range(3)]


def make_move(x, y, z):
    global ruch_sign
    board[x][y][z] = ruch_sign
    for item in board:
        print(item)


def board_full():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i][j][k] is not ' ':
                    return False
    return True


def check_if_game_ended():
    if board_full():
        return ' '
    for dim in range(3):
        for i in range(3):
            if board[dim][i][0] is not ' ' and board[dim][i][0] == board[dim][i][1] and board[dim][i][1] == board[dim][i][2]:
                return board[dim][i][0]
            if board[dim][0][i] is not ' ' and board[dim][0][i] == board[dim][1][i] and board[dim][1][i] == board[dim][2][i]:
                return board[dim][0][i]
        if board[dim][0][0] is not ' ' and board[dim][0][0] == board[dim][1][1] and board[dim][1][1] == board[dim][2][2]:
            return board[dim][0][0]
        if board[dim][2][0] is not ' ' and board[dim][2][0] == board[dim][1][1] and board[dim][1][1] == board[dim][0][2]:
            return board[dim][0][2]
    for row in range(3):
        for i in range(3):
            if board[0][row][i] is not ' ' and board[0][row][i] == board[1][row][i] and board[1][row][i] == board[2][row][i]:
                return board[0][row][i]
            if board[i][row][0] is not ' ' and board[i][row][0] == board[i][row][1] and board[i][row][1] == board[i][row][2]:
                return board[i][row][0]
        if board[0][row][0] is not ' ' and board[0][row][0] == board[1][row][1] and board[1][row][1] == board[2][row][2]:
            return board[0][row][0]
        if board[2][row][0] is not ' ' and board[2][row][0] == board[1][row][1] and board[1][row][1] == board[0][row][2]:
            return board[2][row][0]
    for column in range(3):
        for i in range(3):
            if board[0][i][column] is not ' ' and board[0][i][column] == board[1][i][column] and board[2][i][column] == board[2][i][column]:
                return board[0][i][column]
            if board[i][0][column] is not ' ' and board[i][0][column] == board[i][1][column] and board[i][1][column] == board[i][2][column]:
                return board[i][0][column]
        if board[0][0][column] is not ' ' and board[0][0][column] == board[1][1][column] and board[1][1][column] == board[2][2][column]:
            return board[0][0][column]
        if board[2][0][column] is not ' ' and board[2][0][column] == board[1][1][column] and board[1][1][column] == board[0][2][column]:
            return board[2][0][column]
    if board[0][0][0] is not ' ' and board[0][0][0] == board[1][1][1] and board[1][1][1] == board[2][2][2]:
        return board[0][0][0]
    if board[0][0][2] is not ' ' and board[0][0][2] == board[1][1][1] and board[1][1][1] == board[2][2][0]:
        return board[0][0][2]
    if board[0][2][0] is not ' ' and board[0][2][0] == board[1][1][1] and board[1][1][1] == board[2][0][2]:
        return board[0][2][0]
    if board[0][2][2] is not ' ' and board[0][2][2] == board[1][1][1] and board[1][1][1] == board[2][0][0]:
        return board[0][2][2]
    return 'nie'


@app.route('/end')
def win():
    global board
    board = [[[' ' for x in range(3)] for y in range(3)] for z in range(3)]
    return render_template('win.html', winner=ruch_sign)


@app.route('/end_check')
def check():
    global board
    board = [[[' ' for x in range(3)] for y in range(3)] for z in range(3)]
    return render_template('remis.html')


@app.route('/link', methods={'GET'})
def link():
    global ruch_sign
    x = request.args.get('x', None)
    y = request.args.get('y', None)
    z = request.args.get('z', None)
    x = int(x)
    y = int(y)
    z = int(z)
    make_move(x, y, z)
    if check_if_game_ended() is 'x':
        return redirect(url_for('win'))
    elif check_if_game_ended() is 'o':
        return redirect(url_for('win'))
    elif check_if_game_ended() is ' ':
        return redirect(url_for('check'))
    else:
        if ruch_sign == 'x':
            ruch_sign = 'o'
        else:
            ruch_sign = 'x'
        return redirect('/gra')


@app.route('/gra', methods={'GET', 'POST'})
def gra():
    lista = []
    if request.method == ['POST']:
        lista.append(request.form['x'])
        lista.append(request.form['y'])
        lista.append(request.form['z'])
    return render_template('gra.html', lista=lista, board=board)


@app.route('/', methods={'GET', 'POST'})
def hello_world():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True, port=5043)
