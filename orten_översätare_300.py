#imports
#Klasser

class GoodOrBad: #Jag kom på att jag har glömt hur klasseer fungerar
    def __init__(self, good, bad):
        self.good = good
        self.bad = bad
        
class Emotion:
    pass

class Gramor: #Vokaler consonanter n shit
    pass

#Funktioner
"""
Ha med en docstring som förklarar complexa saker 

https://www.swedishnomad.com/sv/orten-slang/ 
https://www.gp.se/nyheter/sverige/35-ord-som-bara-%C3%A4kta-ortenbarn-f%C3%B6rst%C3%A5r-1.2586616
"""
def convert_orten_word_to_list():
    all_orten_words = []
    with open("orten_ordlista.txt", "r", encoding="utf8") as word:
        all_orten_words = word.readlines()
    return all_orten_words

def convert_svenne_word_to_list():
    all_svenne_words = []
    with open("svenne_ordlista.txt", "r", encoding="utf8") as word:
        all_svenne_words = word.readlines()
    return all_svenne_words

def convert_orten_sentences_to_list():
    all_orten_meningar = []
    with open("orten_meninglista.txt", "r", encoding="utf8") as mening:
        all_orten_meningar = mening.readlines()
    return all_orten_meningar

def convert_svenne_sentences_to_list():
    all_svenne_meningar = []
    with open("svenne_meningslista.txt", "r", encoding="utf8") as mening:
        all_svenne_meningar = mening.readlines()
    return all_svenne_meningar


def make_list_better(any_words_or_sentenses_list : list()):
    new_any_words_or_sentenses_list = []
    for item in any_words_or_sentenses_list:
        new_any_words_or_sentenses_list.append(str(item).strip("\n").lower()) #lower fungerar inte om det inte står str typ
    return new_any_words_or_sentenses_list


def translate(sentence : int):
    orten_word_list = make_list_better(convert_orten_word_to_list())
    orten_sentence_list = make_list_better(convert_orten_sentences_to_list())
    svenne_word_list = make_list_better(convert_svenne_word_to_list())
    svenne_sentence_list = make_list_better(convert_svenne_sentences_to_list())

    sentence_index = -1
    is_sentence = False
    sentence = sentence.lower()

    for item in svenne_sentence_list:
        sentence_index += 1
        if item == sentence:
            print(orten_sentence_list[sentence_index])
            is_sentence = True
            break
        
    if is_sentence == False:
        word_index = -1
        sentence_list = list(sentence.split(" "))

        abo = 0

        for word in sentence_list:
            word_index += 1
            orten_index = -1
            for item in orten_word_list:
                orten_index += 1
                if word in item:
                    sentence_list[word_index] = svenne_word_list[orten_index] #denna är wack
                    abo += 1

        print(sentence_list)



    #for word in sentence_list:
        #for equel in svenne 
        #if word ==





 

#Huvudfunktion 
def main(): 

    while True: 
        print("Wellcome to main.")
        print('Press 1 for "Orten Translator" Press 2 for "Svenne Translator" Press 3 to end the program.')
        choise = int(input("- "))

        if choise == 1:
            print("Whrite your sentence")
            sentence = input("- ")
            #print(orten_word_list)
            #print(orten_senctence_list)
            translate(sentence)

        elif choise == 2:
            print("comming soon")

        elif choise == 3:
            break


if __name__ == "__main__":
    main()

#Kom ihåg att converta till lower case
#Sen ta bort alla svenska ord och ändra till English
#Böjningar shono/shonon blir kille/killen
# shona/shonan blir tjej/tjejen
# katt/kattig blir snygg/snygg

#Skriv in dessa i listan med / 

#Har alternativa översätningar i svenne ord lista
#Kom ihåg plural form 

#Aanvänd klasser för att hitta känsla eller ton i meningen

#läg till mer orten ord