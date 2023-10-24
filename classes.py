class meusJogos():
    def __init__(self, nome, categoria, plataforma):
        self.nome = nome
        self.categoria = categoria
        self.plataforma = plataforma


class meusUsuarios():
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password


jogoUm = meusJogos('Sniper Elite', 'Ação', 'PC')
jogoDois = meusJogos('Final Fantasy', 'RPG', 'PC')
jogoTres = meusJogos('FIFA', 'Esportes', 'Playstation')
games = [jogoUm, jogoDois, jogoTres]

userUm = meusUsuarios('Guilherme', 'xuot1', 'magno')
userDois = meusUsuarios('Thyerris', 'flop', 'batu')
userTres = meusUsuarios('Melissa', 'mel', 'auauau')
users = { userUm.nickname : userUm,
         userDois.nickname : userDois,
         userTres.nickname : userTres }