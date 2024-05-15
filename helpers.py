
from random import randint
from npc_phrases import npc_say

def create_name():
    vogals = ['a','e','i','o','u']
    consoants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
    name_size = randint(4,8)
    name = ''
    for i in range(name_size):
        if i%2 == 0:
            name += vogals[randint(0,4)]
        elif i%2 == 1:
            name += consoants[randint(0,20)]
    return name.capitalize()

def d6_dice():
    return randint(1, 6)

def create_npc():
    name = create_name()
    level = randint(1,10)
    damage = randint(1,10) * 5
    life = randint(1,10) * 15

    return {
        "name": name,
        "level": level,
        "damage": damage,
        "life": life,
        "damage_taken": 0
    }

def npc_says_when_winning(npc, player):
    print(f"Que pena {player['name']}! Você sofreu uma derrota!")
    print(f"- {npc['name']} diz... ")
    print(f"- {npc_say()}")

def battle_game_messages(phase):
    phrases = [
        "Você está numa arena com milhares de pessoas te assistindo, um oponente aparece diante de você...",
        "De volta à arena, o sol quente parece derreter sua pele, o povo agitado pelo combate anseia ver mais sangue. \nUm novo oponente se aproxima da arena.",
        "Depois de algumas lutas, as forças parecem estar indo embora. Mas mesmo assim, \nvocê entra na arena com a esperança de continuar e sair como um vencedor. \nMais um oponente aparece diante de ti sedento pelo seu sangue.",
        "Um novo desafiante entra na arena,\n os gritos da multidão ecoam em seus ouvidos enquanto você se prepara para mais um confronto mortal.",
        "O ambiente tenso da arena preenche seus sentidos enquanto você se prepara \npara enfrentar mais um oponente determinado a testar sua habilidade.",
        "Os olhares ansiosos da multidão parecem pesar sobre seus ombros enquanto \nvocê se prepara para mais uma batalha na arena lotada.",
        "O cheiro de suor e sangue permeia o ar enquanto você aguarda o próximo desafiante, \nsabendo que cada luta na arena é uma prova de sua coragem.",
        "O rugido da multidão ressoa na arena, alimentando sua determinação enquanto \nvocê se prepara para enfrentar mais um oponente na luta pela sobrevivência.",
        "A adrenalina corre pelas suas veias enquanto você encara seu próximo adversário na arena, \nsabendo que apenas um sairá vitorioso deste confronto.",
        "O calor escaldante da arena não é páreo para a intensidade de sua determinação \nenquanto você se prepara para mais um duelo com um novo oponente.",
        "Cada passo em direção ao centro da arena parece mais pesado do que o anterior, \nmas você sabe que precisa enfrentar mais um desafiante se quiser sair vitorioso.",
        "Os murmúrios da multidão ecoam em seus ouvidos, alimentando sua determinação enquanto você se \nprepara para mais um confronto na arena implacável.",
        "A tensão no ar é palpável enquanto você aguarda seu próximo oponente, \nsabendo que cada combate na arena é uma prova de sua habilidade e coragem.",
        "A perspectiva de mais uma batalha na arena não o intimida, \nmas sim o inspira a enfrentar seu próximo desafiante com ainda mais determinação.",
        "Os olhos famintos da multidão observam cada movimento seu enquanto você \nse prepara para enfrentar mais um oponente na arena lotada.",
        "A vontade de vencer queima em seu peito enquanto você encara seu próximo desafiante na arena, \npronto para provar sua força e habilidade mais uma vez.",
        "Cada novo oponente que entra na arena é apenas mais uma oportunidade para você mostrar sua coragem \ne determinação diante da multidão que aguarda ansiosamente.",
        "A energia elétrica na arena é contagiante enquanto você se prepara para mais uma batalha, \ndeterminado a sair vitorioso e conquistar o respeito da multidão.",
        "A determinação em seus olhos não passa despercebida pela multidão enquanto você aguarda seu próximo desafiante, \npronto para mais um combate emocionante na arena.",
        "O calor da batalha é palpável enquanto você se prepara para enfrentar mais um oponente na arena, \ndeterminado a superar qualquer obstáculo em seu caminho.",
        "A multidão agitada pela emoção da luta observa atentamente enquanto você se prepara para mais um confronto na arena, \npronto para provar sua valentia mais uma vez."
        "O som dos tambores ressoa na arena, anunciando o início de mais um desafio.\n Você se prepara para enfrentar seu próximo oponente, determinado a sair vitorioso.",
        "A atmosfera carregada de expectativa na arena só aumenta sua determinação \nenquanto você se prepara para mais um duelo emocionante.",
        "Os olhares ansiosos da multidão acompanham seus passos enquanto você avança para o centro da arena, \npronto para enfrentar mais um desafiante.",
        "A tensão no ar é palpável enquanto você aguarda seu próximo oponente, \nsabendo que cada combate na arena é uma oportunidade para provar sua habilidade.",
        "A vibração da arena é contagiante, alimentando sua determinação enquanto \nvocê se prepara para mais um confronto emocionante.",
        "O brilho dos refletores ilumina a arena lotada, destacando você e seu próximo \noponente enquanto se preparam para o embate.",
        "Cada novo desafiante que entra na arena é apenas mais uma chance para você vmostrar sua coragem e habilidade diante da multidão que aguarda ansiosamente.",
        "A expectativa do próximo combate só aumenta sua vontade de vencer \nenquanto você se prepara para mais uma batalha na arena.",
        "O calor do confronto é sentido em cada respiração enquanto você se \nprepara para enfrentar mais um oponente na arena implacável.",
        "A determinação brilha em seus olhos enquanto você encara seu próximo \ndesafiante na arena, pronto para provar sua valentia mais uma vez.",
        "A emoção do combate é palpável na arena enquanto você se prepara \npara mais uma batalha, determinado a superar qualquer obstáculo em seu caminho.",
        "Os murmúrios da multidão ecoam em seus ouvidos, alimentando sua \ndeterminação enquanto você aguarda seu próximo oponente.",
        "A intensidade do confronto é sentida em cada músculo tenso enquanto \nvocê se prepara para mais um duelo na arena implacável.",
        "O rugido da multidão enche seus ouvidos enquanto você avança \npara o centro da arena, pronto para enfrentar mais um desafio.",
        "A ansiedade toma conta de você enquanto aguarda seu próximo \noponente na arena, sabendo que cada luta é uma oportunidade para provar sua coragem.",
        "A empolgação da multidão só aumenta sua determinação enquanto \nvocê se prepara para mais uma batalha na arena lotada.",
        "A adrenalina corre em suas veias enquanto você se prepara para enfrentar \nseu próximo adversário na arena, pronto para lutar até o fim.",
        "A energia eletrizante na arena é contagiosa enquanto você avança para o próximo combate,\n determinado a sair vitorioso e conquistar o respeito de todos.",
        "Os olhares curiosos da multidão acompanham seus movimentos enquanto \nvocê se prepara para mais um duelo emocionante na arena.",
        "A vontade de vencer queima em seu peito enquanto você avança para o centro da arena, \npronto para enfrentar qualquer desafio que surja em seu caminho."
    ]
    if(phase == 1):
        return phrases[0]
    else:
        return phrases[phase]