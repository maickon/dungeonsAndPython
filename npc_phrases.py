from random import randint

def npc_say():
    phrases = [
        "Ah, indo embora tão cedo? Eu mal estava começando a me divertir!",
        "Sabe, você poderia ter pelo menos tentado antes de desistir.",
        "Bom trabalho! Você definitivamente será lembrado como o covarde mais famoso da cidade.",
        "Desistir é uma estratégia válida... para quem não tem coragem.",
        "Vai fugir? Deixe-me adivinhar, isso faz parte do seu plano mestre?",
        "Parece que alguém está com medo de um pequeno desafio.",
        "Espere! Aonde você vai? Eu ainda tenho tantos insultos para te lançar!",
        "Desistir é uma opção... para os fracos.",
        "Fugir é sempre uma boa ideia... para aqueles que não se importam com a vergonha.",
        "Você está desistindo? Ah, que surpresa... nenhuma."
    ]
    return phrases[randint(0, len(phrases) - 1)]

def battle_phrases():
    phrases = [
        "Você é mais fraco do que eu pensava. Este será fácil.",
        "Prepare-se para enfrentar a fúria do meu poder!",
        "Você não tem chance contra mim. Eu sou imparável!",
        "Eu espero que você tenha dito suas últimas palavras.",
        "Se prepare para uma derrota humilhante.",
        "Você ousa desafiar meu poder? Você vai se arrepender disso.",
        "Eu vou te mostrar o verdadeiro significado de dor e sofrimento.",
        "Seus dias estão contados. Você está prestes a encontrar seu fim.",
        "Este será o seu último confronto. Você não vai sobreviver.",
        "Eu vou destruir tudo o que você ama e então acabar com você."
    ]
    return phrases[randint(0, len(phrases) - 1)]

def damage_phrases():
    phrases = [
        "Ouch! Isso doeu... um pouco.",
        "Você acertou! Parabéns, você é oficialmente menos irritante agora.",
        "Aha! Você finalmente acertou algo. Agora me deixe devolver o favor.",
        "Hm, isso foi mais do que um tapinha nas costas. Vou ter que me esforçar agora.",
        "Bem jogado! Mas agora é minha vez.",
        "Hmm, esse golpe até que foi decente. Mas ainda estou de pé!",
        "Ai! Você tem um golpe forte! Mas não vou cair tão cedo!",
        "Interessante... você não é tão inútil quanto parecia.",
        "Isso foi uma tentativa de me machucar? Continue tentando, quem sabe um dia funciona.",
        "Haha, é melhor do que eu esperava. Vamos ver se você pode fazer de novo!"
    ]
    return phrases[randint(0, len(phrases) - 1)]

def sarcastic_heal_phrases():
    phrases = [
        "Ah, então você precisa de uma poção para se manter de pé? Que pena, eu estava esperando um desafio de verdade.",
        "Parece que alguém está com medo de um pouco de dor. Uma poção de cura, sério?",
        "Olha só quem precisa de uma poção para se manter vivo. Que patético!",
        "Hmm, uma poção de cura? Parece que você não é tão invencível quanto pensava.",
        "Aha! Uma poção de cura, você realmente sabe como arruinar a diversão de um bom combate.",
        "Usando poções agora, é? Parece que alguém está com medo de morrer.",
        "Interessante... você está tão desesperado que precisa de uma poção para se manter de pé.",
        "Que pena, eu estava esperando um adversário digno. Mas parece que você prefere se esconder atrás de poções de cura.",
        "Oh, uma poção de cura! Que surpresa... não. Mas não se preocupe, vou fazer isso durar mais tempo.",
        "Haha, uma poção de cura? Isso só vai adiar o inevitável."
    ]
    return phrases[randint(0, len(phrases) - 1)]