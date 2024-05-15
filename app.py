from random import randint
import npc_phrases as say
import helpers as helper
import classes as the_class
import sys, os

sys.stdout.reconfigure(encoding='utf-8')

player = {
    "name": '',
    "class": '',
    "level": 1,
    "damage": 0,
    "life": 0,
    "damage_taken": 0,
    "recover": 2,
    "xp":0
}

npcs = []

def npc_action(npc):
    action = False
    npc_damage = npc['damage'] + helper.d6_dice()
    npc_say = say.damage_phrases()
    player['damage_taken'] = player['damage_taken'] - (npc_damage)
    print(f"- {npc['name']} diz... {npc_say}\n")
    print(f"Oponente {npc['name']} fez um contra-ataque que lhe causou {npc_damage} de dano\n")
    print(f"Sua vida foi reduzida em {player['damage_taken']}\n")
    print(f"Seus status [{player['name']}] > VIDA {abs(player['damage_taken'])}/{player['life']} <=> DANO {player['damage']}\n")
    print(f"Status do oponente [{npc['name']}] > VIDA {abs(npc['damage_taken'])}/{npc['life']} <=> DANO {player['damage']}\n")
    os.system("clear")
    if(abs(player['damage_taken']) >= player['life']):
        action = 'player-lose'
    else:
        action = 'next-phase'

    return action

def use_potion():
    if(player['recover'] > 0):
        player['recover'] = player['recover'] - 1
        potion = helper.d6_dice() * randint(2, 6)
        player['life'] = player['life'] + potion
        return potion
    
    return False

def actions(npc):
    action = False
    response = False
    attacks = 0

    while(action == False):
        if(attacks > 0):
            print("O combate continua... Esta é sua ação! Selecione o que deseja fazer:\n")
        else:
            print("Esta é sua ação de combate. Selecione o que deseja fazer:\n")

        print(f"1 - Atacar")
        print(f"2 - Usar poção")
        print(f"3 - Desistir\n")
        response = int(input("Selecione: "))
        os.system('clear')
        if(response < 1 or response > 3):
            print("Resposta inválida!")
            os.system('clear')
        else:
            action = True

        attacks = attacks+1
    
    if(response == 1):
        damage = helper.d6_dice() + player['damage']
        npc['life'] = npc['life'] - damage
        npc['damage_taken'] += damage
        if(abs(npc['damage_taken']) > npc['life']):
            print("Você venceu o combate!")
            return 'player-winner'
        else:
            print(f"Você causou {damage} de dano em {npc['name']}\n")
            return 'next-phase'

    if(response == 2):
        potion = use_potion()
        if(potion):
            npc_say = say.sarcastic_heal_phrases()
            print(f"Você usou uma poção que aumentou +{potion} de vida")
            print(f"- {npc['name']} diz... ")
            print(f"- {npc_say}")
            return 'next-phase'
        else:
            print("Você tentou usar uma poção de cura. Mas que pena! Você não possui uma e perdeu sua vez de atacar.")
            return 'next-phase'

    if(response == 3):
        npc_say = say.npc_say()
        print("Você desistiu do combate. Que triste...")
        return 'player-lose'

def player_status():
    print("Status dos personagens:\n")
    print(f"Personagem > [{player['name']}] - VIDA: {player['damage_taken']}/{player['life']} <=> DANO: {player['damage']} <=> POÇÕES: {player['recover']}\n")

def npc_status(npc):
    print(f"NPC > [{npc['name']}] - VIDA: {npc['damage_taken']}/{npc['life']} <=> DANO: {npc['damage']}\n")

def game_status(npc, message):
    print(f"\n{message}\n")
    player_status()
    npc_status(npc)

def battle_game(phase):
    npc = helper.create_npc()
    combat = True
    action = False
    combat_winner = False
    npc_say = say.battle_phrases()
    helper.battle_game_messages(phase)
    print(f"OPONENTE: {npc['name']} diz... {npc_say}\n")
    print("Ele vem em sua direção e um combate se inicia...\n")
    turn = 'player'
    while(combat):
        if(turn == 'player'):
            action = actions(npc)
            if(action == 'next-phase'):
                turn = 'npc'
            elif(action == 'player-winner'):
                print(f"Parabéns {player['name']}! Você venceu o combate!")
                combat = False
                combat_winner = True
            elif(action == 'player-lose'):
                helper.npc_says_when_winning(npc, player)
                combat = False

        if(turn == 'npc'):
            action = npc_action(npc)
            if(action == 'next-phase'):
                turn = 'player'
            elif(action == 'player-lose'):
                helper.npc_says_when_winning(npc, player)
                combat = False
    
    game_status(npc, message="Batalha finalizada!")
    return combat_winner

def reward():
    additional = randint(2, 5)
    player['recover'] = player['recover'] + additional
    return additional

def player_menu_after_battle(current_phase):
    print(f"Você venceu o combate {current_phase}! Que interessante!\n")
    print(f"Você está descançando até a chegada do combate {current_phase+1}. O que deseja fazer?\n")
    option = True
    next_action = True
    while(option):
        print("Digite:")
        print("1 - Usar poção")
        print("2 - Ver meus status")
        print("3 - Seguir para o próximo combate")
        print("4 - Desistir")
        response = int(input("Inserir resposta: "))
        os.system("clear")
        
        if(response == 1):
            potion = use_potion()
            if(potion):
                print(f"Você usou uma poção e aumentou +{potion} de vida!")
            else:
                print(f"Você já usou todas as suas poções de cura! Tente ganhar uma nova vencendo o próximo combate.")
        elif(response == 2):
            player_status()
        elif(response == 3):
            option = False
        elif(response == 4):
            print("Você desistiu de lutar. Sua aventura termina aqui. :(")
            option = False
            next_action = False
        else:
            print("Por favor, informe uma opção válida!")
    return next_action

def main():
    monk = the_class.class_monk()
    warrior = the_class.class_warrior()
    barbarian = the_class.class_barbarian()
    selected_class = 0
    chosen_class = False
    phases = 2
    current_phase = 1

    while(selected_class != 1 and selected_class != 2 and selected_class != 3):
        print("Bem vindo ao Dungeons and Pythons, um mini RPG de terminal para você brincar\n")
        player['name'] = input("Informe o seu nome nobre aventureiro:")
        os.system("clear")
        print(f"Olá {player['name']}! Seja bem vindo ao nosso mundo\n")
        print("Selecione sua classe: ")
        print(f"1 - {monk['name']} >> NÍVEL {monk['level']} DANO {monk['damage']} VIDA {monk['life']}")
        print(f"2 - {warrior['name']} >> NÍVEL {warrior['level']} DANO {warrior['damage']} VIDA {warrior['life']}")
        print(f"3 - {barbarian['name']} >> NÍVEL {barbarian['level']} DANO {barbarian['damage']} VIDA {barbarian['life']}\n")
        selected_class = int(input("Digite: "))
        os.system('clear')
        if selected_class <= 0 or selected_class >=4:
            selected_class = 0
            print("Selecione uma classe válida!!!\n\n")
            os.system('clear')
        else:
            classes = the_class.classes()
            chosen_class = classes[selected_class-1]
            player['class'] = chosen_class['name']
            player['damage'] = chosen_class['damage']
            player['life'] = chosen_class['life']

    if chosen_class != False:
        print(f"Parabéns {player['name']}! Você escolheu a classe: {player['class']}\n")
        print(f"Sua ficha: [{player['name']}] - VIDA: {player['life']} <=> DANO: {player['damage']} <=> POÇÕES GUARDADAS: {player['recover']}\n")

        while(battle_game(current_phase) and current_phase <= phases):
            print(f"::::::::::::FASE {current_phase}::::::::::::\n")
            current_phase += 1
            next_action = player_menu_after_battle(current_phase)
            if(next_action):
                os.system("clear")
                print(f"Bem vindo a fase {current_phase}. Um novo oponente está a espera por você!\n")
                print(f"{helper.battle_game_messages(current_phase)}\n")
                print(f"E você {player['name']}, aguardou anciosamente pelo seu próximo combate\n")
                print(f"Durante a sua espera, você recebeu {reward()} poções de cura para o seu próximo combate. Use-as com inteligência!\n")
                os.system("clear")
                print("Horas depois...\n\n")
            else:
                print("Fim da aventura")
                break
main()
