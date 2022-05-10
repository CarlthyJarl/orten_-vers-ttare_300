#imports
#Classes

class Responce: #Jag kom på att jag har glömt hur klasseer fungerar
    pass
        
class Emotion:
    pass

class Gramor: #Vokaler consonanter n shit
    def __init__(self, vowels, consonants):
        self.vowels =  vowels
        self.consonants = consonants

#Funktioner
"""
Ha med en docstring som förklarar complexa saker 

https://www.swedishnomad.com/sv/orten-slang/ 
https://www.gp.se/nyheter/sverige/35-ord-som-bara-%C3%A4kta-ortenbarn-f%C3%B6rst%C3%A5r-1.2586616
"""
# def difrent_letters():
#     vowels = ["a", "e", "i", "o", "u"]
#     consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
#     # letters = Gramor(["a", "e", "i", "o", "u"], ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"])
#     return_letters = Gramor(vowels, consonants)
#     return return_letters

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

def make_list_sentence(sentence_list):
    sentence = " "
    return sentence.join(sentence_list)

def find_vowel(sentence : int):
    number_of_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels[0]: #knas
        number_of_vowels += sentence.count(i)
    return number_of_vowels

def find_consonant(sentence : int):
    number_of_consonants = 0
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    for i in consonants:
        number_of_consonants += sentence.count(i)
    return number_of_consonants






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

        for word in sentence_list:
            word_index += 1
            orten_index = -1
            for item in orten_word_list:
                orten_index += 1
                if word == item:
                    sentence_list[word_index] = svenne_word_list[orten_index] 

                elif word in item and "/" in item:
                    sentence_list[word_index] = svenne_word_list[orten_index]
        
        new_sentence_list = []
        alternate_translation = False
        for word in sentence_list:
            if "/" in word:
                difrent_words = word.split("/")
                new_sentence_list.append(difrent_words[0])
                alternate_translation = True
                
            else:
                new_sentence_list.append(word)
        new_new_sentence_list = make_list_sentence(new_sentence_list)
        print(new_new_sentence_list)
        if alternate_translation == True:
            print(f"Alternate translation(s) {make_list_sentence(sentence_list)}")
        print(f"number of vowels: {find_vowel(new_new_sentence_list)}")
        print(f"number of consonants: {find_consonant(new_new_sentence_list)}")


                


        # words = sentence_list.index(difrent_words)

        # sentence_index = -1 #allt under är abo knas
        # for word in sentence_list:
        #     if "/" in word:
        #         #sentence_index += 1
        #         difrent_words = word.split("/")
        #         for num in len(difrent_words):
        #             word = word.replace(word, difrent_words[num])
        #             sentence_list.append(word)
        #             print(sentence_list)

        # print(sentence_list)



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
            translate(sentence)

        elif choise == 2:
            print("comming soon")

        elif choise == 3:
            break


if __name__ == "__main__":
    main()


#Aanvänd klasser för att hitta känsla eller ton i meningen

