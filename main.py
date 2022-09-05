from genericpath import exists
import json
import random
from gtts import gTTS
from playsound import playsound

import pyttsx3

pronounciationEnabled = False
glossary = '生词本.json'
num_iter = 1

def both_know(select_word, weight):
    if select_word in weight.keys():
        weight[select_word] += 1
    else:
        weight[select_word] = 1
    return weight


def misunderstand(select_word, weight):
    if select_word in weight.keys() and weight[select_word] < -6:
        return weight

    if select_word in weight.keys():
        weight[select_word] -= 2
    else:
        weight[select_word] = -2
    return weight


def dont_know(select_word, weight):
    if select_word in weight.keys() and weight[select_word] < -6:
        return weight

    if select_word in weight.keys():
        weight[select_word] -= 3
    else:
        weight[select_word] = -3
    return weight

def pronounceOnline(word):
    tts = gTTS(word, lang='en')
    tts.save('temp.mp3')
    playsound('temp.mp3')

def pronounce(engine, word):
    engine.setProperty("rate", 300)
    engine.say(word)
    engine.runAndWait()
    

def main():
    word_dict = json.load(open(glossary, 'r'))

    try:
        word_dict_weight = json.load(open('weight.json', 'r'))
    except:
        word_dict_weight = {}
    engine = pyttsx3.init()

    for i in range(num_iter):
        print('---------------------第', i+1, '个单词---------------------')
        select_word_cn = random.choice(list(word_dict.keys()))
        reco, know = None, None
        select_word = random.choice(word_dict[select_word_cn])

        while select_word in word_dict_weight.keys() and word_dict_weight[select_word] > 2:
            select_word_cn = random.choice(list(word_dict.keys()))
            select_word = random.choice(word_dict[select_word_cn])
        if (pronounciationEnabled):
            pronounce(engine, select_word)
    # input user's answer
        while reco != "j" and reco != "k":
            reco = input(select_word + ' (j/k)\n')

            if reco == "k":
                know = "k"
        print(select_word_cn, '\n')
        while know != "j" and know != "k":
            know = input('是否和释义一致？(j/k)\n')

    # determine weight
        if reco == 'j' and know == 'j':
            word_dict_weight = both_know(select_word, word_dict_weight)
        elif reco == 'j' and know == 'k':
            word_dict_weight = misunderstand(select_word, word_dict_weight)
        elif reco == 'k' and know == 'k':
            word_dict_weight = dont_know(select_word, word_dict_weight)

        print('weight: ', word_dict_weight[select_word], '\n')
    json.dump(word_dict_weight, open('weight.json', 'w+'))
    print('保存成功！')


if __name__ == '__main__':
    main()
