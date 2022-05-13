# Imports
# Classes
class Responce: # In development
    pass
        
class Emotion: # In development
    pass

# Funktions
def convert_orten_word_to_list():
    all_orten_words = []
    with open("orten_word_list.txt", "r", encoding="utf8") as word:
        all_orten_words = word.readlines()
    return all_orten_words

def convert_swedish_word_to_list():
    all_swedish_words = []
    with open("swedish_word_list.txt", "r", encoding="utf8") as word:
        all_swedish_words = word.readlines()
    return all_swedish_words

def convert_orten_sentences_to_list():
    all_orten_meningar = []
    with open("orten_sentence_list.txt", "r", encoding="utf8") as mening:
        all_orten_meningar = mening.readlines()
    return all_orten_meningar

def convert_swedish_sentences_to_list():
    all_swedish_meningar = []
    with open("svenne_sentence_list.txt", "r", encoding="utf8") as mening:
        all_swedish_meningar = mening.readlines()
    return all_swedish_meningar

def make_list_better(any_words_or_sentenses_list : list()):
    new_any_words_or_sentenses_list = []
    for item in any_words_or_sentenses_list:
        new_any_words_or_sentenses_list.append(str(item).strip("\n").lower()) # lower only works when it says str for som reason
    return new_any_words_or_sentenses_list 
    # Returns a more useble string

def make_list_sentence(sentence_list): # Make list string
    sentence = " "
    return sentence.join(sentence_list)

def find_vowel(sentence : int):
    number_of_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in vowels:
        number_of_vowels += sentence.count(letter)
    return number_of_vowels

def find_consonant(sentence : int):
    number_of_consonants = 0
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    for letter in consonants:
        number_of_consonants += sentence.count(letter)
    return number_of_consonants

def translate(sentence : str):
    """skriv

    Args:
        sentence (str): The sentence that the user wrights in main.

    The funkktion starts by taking in all the lists with the translate words. 
    the first for loop cheacks if the senteance can be translated direktly. 
    otherwise it gowes on to translate the words. 


    """
    # Lists with the translate words and sentenses are defined.
    orten_word_list = make_list_better(convert_orten_word_to_list())
    orten_sentence_list = make_list_better(convert_orten_sentences_to_list())
    swedish_word_list = make_list_better(convert_swedish_word_to_list())
    swedish_sentence_list = make_list_better(convert_swedish_sentences_to_list())

    sentence_index = -1 
    is_sentence = False
    sentence = sentence.lower()

    # Tryes to transklate sentence direktly. 
    for item in swedish_sentence_list:
        sentence_index += 1
        if item == sentence:
            print(orten_sentence_list[sentence_index])
            is_sentence = True
            break
    # Translates word for word 
    if not is_sentence:
        word_index = -1
        sentence_list = list(sentence.split(" "))

        for word in sentence_list:
            word_index += 1
            orten_index = -1
            for item in orten_word_list:
                orten_index += 1
                if word == item:
                    sentence_list[word_index] = swedish_word_list[orten_index] 

                elif word in item and "/" in item:
                    sentence_list[word_index] = swedish_word_list[orten_index]
        
        new_sentence_list = []
        alternate_translation = False
        for word in sentence_list:
            if "/" in word:
                difrent_words = word.split("/")
                new_sentence_list.append(difrent_words[0])
                alternate_translation = True
                
            else:
                new_sentence_list.append(word)
        # Makes prosesed list ready to print
        new_new_sentence_list = make_list_sentence(new_sentence_list)
        print(f"\n{new_new_sentence_list}")
        if alternate_translation == True:
            print(f"Alternate translation(s) {make_list_sentence(sentence_list)}")
        print(f"number of vowels: {find_vowel(new_new_sentence_list)}")
        print(f"number of consonants: {find_consonant(new_new_sentence_list)}")
 

# Main Funktion
def main(): 

    while True: 
        print("Wellcome to main.")
        print('Press 1 for "Orten Translator" Press 2 for " Translator" Press 3 to end the program.')
        choise = (input("- "))

        if choise == "1":
            print("Write your sentence")
            sentence = input("- ")
            translate(sentence)
            print("\n")

        elif choise == "2":
            print("comming soon")

        elif choise == "3":
            break


if __name__ == "__main__":
    main()


