#imports
#Klasser
#Funktioner
"""
Ha med en docstring

https://www.swedishnomad.com/sv/orten-slang/ 
https://www.gp.se/nyheter/sverige/35-ord-som-bara-%C3%A4kta-ortenbarn-f%C3%B6rst%C3%A5r-1.2586616
"""
def convert_to_list(): 
    all_orten_words = []
    with open("orten_ordlista.txt", "r", encoding="utf8") as word:
        all_orten_words = word.readlines()
    print(all_orten_words)

convert_to_list()
        


#Huvudfunktion 


#Kom ihåg att converta till lower case