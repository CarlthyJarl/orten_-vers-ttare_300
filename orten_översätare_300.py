#imports
#Klasser
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
convert_word_to_list()

def convert_sentences_to_list():
    all_orten_meningar = []
    with open("orten_meninglista.txt", "r", encoding="utf8") as mening:
        all_orten_meningar = mening.readlines()
    #print(all_orten_meningar)
    return all_orten_meningar 


def make_list_better(sentence_list : list(), word_list : list()):
    new_word_list = []
    new_sentence_list = []
    for i in word_list:
        new_word_list.append(str(i).strip("\n"))
    for i in sentence_list:
        new_sentence_list.append(str(i).strip("\n"))
    # print(new_word_list)
    # print(new_sentence_list)
    return new_word_list, new_sentence_list

make_list_better(convert_sentences_to_list(), convert_word_to_list())

        


#Huvudfunktion 


#Kom ihåg att converta till lower case