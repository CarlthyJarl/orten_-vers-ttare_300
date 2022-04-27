#imports
#Klasser

class GoodOrBad: #Jag kom på att jag har glömt hur klasseer fungerar
    def __init__(self, good, bad):
        self.good = good
        self.bad = bad
        
class Meaning:
    pass

#Funktioner
"""
Ha med en docstring

https://www.swedishnomad.com/sv/orten-slang/ 
https://www.gp.se/nyheter/sverige/35-ord-som-bara-%C3%A4kta-ortenbarn-f%C3%B6rst%C3%A5r-1.2586616
"""
def convert_word_to_list(): 
    all_orten_words = []
    with open("orten_ordlista.txt", "r", encoding="utf8") as word:
        all_orten_words = word.readlines()
    #print(all_orten_words)
    return all_orten_words
#convert_word_to_list()

def convert_sentences_to_list():
    all_orten_meningar = []
    with open("orten_meninglista.txt", "r", encoding="utf8") as mening:
        all_orten_meningar = mening.readlines()
    #print(all_orten_meningar)
    return all_orten_meningar


def make_list_better(sentence_list : list(), word_list : list()):
    new_word_list = []
    new_sentence_list = []
    new_new_word_list = []
    new_new_sentence_list = []

    for i in word_list:
        new_word_list.append(str(i).strip("\n"))
    for i in sentence_list:
        new_sentence_list.append(str(i).strip("\n"))
        
    for i in new_word_list:
        new_new_word_list.append(str(i).lower())
    for i in new_sentence_list:
        new_new_sentence_list.append(str(i).lower())
    # print(new_word_list)
    # print(new_sentence_list)
    return new_new_word_list, new_new_sentence_list


def convert_svenne_words_to_list():
    pass # är här nu




        


#Huvudfunktion 
def main(orten_list : list()): 
    while True: 
        print("Wellcome to main.")
        print('Press 1 for "Orten Translator" Press 2 for "Svenne Translator" Press 3 to end the program.')
        choise = int(input("- "))

        if choise == 1:
            print(orten_list)

        elif choise == 2:
            print("comming soon")

        elif choise == 3:
            break


if __name__ == "__main__":
    #Här ligger alla importerade ordoch meningr i var sin lista i main
    main(make_list_better(convert_sentences_to_list(), convert_word_to_list()))

#Kom ihåg att converta till lower case
#Sen ta bort alla svenska ord och ändra till English
#Böjningar shono/shonon blir kille/killen
# shona/shonan blir tjej/tjejen
# katt/kattig blir snygg/snygg

#Skriv in dessa i listan med / 

#Har alternativa översätningar i svenne ord lista