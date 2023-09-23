from flask import Flask, render_template, request, redirect, session, flash


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
app.secret_key = 'tribo'


#####################
####### ROTAS #######
#####################
@app.route('/')
def mainpage():
    return render_template('login.html', title='Enter with your credentials')


@app.route('/list')
def games_list():
    return render_template('list.html', title='My new title', jogos=games)

@app.route('/insert')
def insertpage():
    return render_template('insert.html', title='Insert a new game')


@app.route('/login')
def login():
    return render_template('login.html', title='Enter with your credentials')

@app.post('/auth')
def authenticate():
    if request.form['user_password'] == 'chateau182':
        session['current_user'] = request.form['username']
        flash(f"Usuário {session['current_user']} logado com sucesso.")
        return redirect('/list')
    
    else:
        flash('Algo deu errado... Por favor, revise seus dados e tente novamente.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash(f"Usuário deslogado.")
    return redirect('/login')


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