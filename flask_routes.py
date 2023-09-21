from flask import Flask, render_template, request, redirect


class meusJogos():
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


jogoUm = meusJogos('Sniper Elite', 'Ação', 'PC')
jogoDois = meusJogos('Final Fantasy', 'RPG', 'PC')
jogoTres = meusJogos('FIFA', 'Esportes', 'Playstation')
games = [jogoUm, jogoDois, jogoTres]


app = Flask(__name__)


#####################
####### ROTAS #######
#####################
@app.route('/')
def mainpage():
    return render_template('list.html', title='My new title', jogos=games)


@app.route('/insert')
def insertpage():
    return render_template('insert.html', title='Insert a new game')


#####################
######## CRUD #######
#####################

#@app.route('/new_game', methods=['POST',])
@app.post('/new_game')
def new_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novoJogo = meusJogos(nome, categoria, console)
    games.append(novoJogo)

    return redirect('/')


app.run(debug=True)