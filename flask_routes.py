from flask import Flask, render_template, request, redirect, session, flash, url_for
import classes


app = Flask(__name__)
app.secret_key = 'tribo'


#####################
####### ROTAS #######
#####################
@app.route('/')
def mainpage():
    next = request.args.get('next')
    return render_template('login.html', title='Enter with your credentials', next=next)

@app.route('/list')
def list():
    if 'current_user' not in session or session['current_user'] == None:
        return redirect(url_for("mainpage", next=url_for("list")))
    
    return render_template('list.html', title='My new title', jogos=classes.games)

@app.route('/insert')
def insert():
    if 'current_user' not in session or session['current_user'] == None:
        return redirect(url_for("mainpage", next=url_for("insert")))
    
    return render_template('insert.html', title='Insert a new game')

@app.post('/auth')
def authenticate():
    if request.form['username'] in classes.users:
        actual_user = classes.users[request.form['username']]

        if request.form['user_password'] == actual_user.password:
            session['current_user'] = actual_user.nickname
            flash(f"Usuário {actual_user.nickname} logado com sucesso.")
            
            next = request.form['next']
            return redirect(next)

    else:
        flash('Algo deu errado... Por favor, revise seus dados e tente novamente.')
        return redirect(url_for("mainpage"))

@app.route('/logout')
def logout():
    session['current_user'] = None
    flash(f"Usuário deslogado.")
    return redirect(url_for("mainpage"))


#####################
######## CRUD #######
#####################

#@app.route('/new_game', methods=['POST',])
@app.post('/new_game')
def new_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novoJogo = classes.meusJogos(nome, categoria, console)
    classes.games.append(novoJogo)

    return redirect(url_for("games_list"))


app.run(debug=True)