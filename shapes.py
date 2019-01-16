
def empty():
    empty_array = []
    empty_array.append(  "----------") # top of the card

    i = 1
    while i < 10:
        empty_array.append("|" + " " * 8 + "|")
        i += 1

    empty_array.append(empty_array[0])
    return empty_array

def check_card_not_equal_10(card):
    if card != "10":
        return "|    {}   |".format(card)
    else:
        return "|   {}   |".format(card)

def diamond(card):
    diamond_array = []
    diamond_array.append(  "----------") # top of the card
    diamond_array.append(  "|  *" + " " * 5 + "|")
    diamond_array.append(  "| * *" + " "* 4 + "|")
    diamond_array.append(  "|  *" + " " * 5 + "|")

    diamond_array.append("|" + " " * 8 + "|")
    diamond_array.append(check_card_not_equal_10(card))
    diamond_array.append("|        |")

    for i in range (1, 4):
        temp = diamond_array[i][::-1]
        diamond_array.append(temp)

    diamond_array.append(diamond_array[0])
    return diamond_array
    # Insert at index 5 whatever you want to insert in the array

def heart(card):
    hearts_array = []
    hearts_array.append("----------")
    hearts_array.append("|_  _    |")
    hearts_array.append("|\\\\//    |")
    hearts_array.append("| \\/     |")

    hearts_array.append("|        |")
    hearts_array.append(check_card_not_equal_10(card))
    hearts_array.append("|        |")

    hearts_array.append("|    _  _|")
    hearts_array.append("|    \\\\//|")
    hearts_array.append("|     \\/ |")
    hearts_array.append(hearts_array[0])
    return hearts_array
    
    # Insert at index 5

def spade(card):
    spades_array = []
    spades_array.append("----------")
    spades_array.append("| **     |")
    spades_array.append("|*__*    |")
    spades_array.append("| ||     |")

    spades_array.append("|        |")
    spades_array.append(check_card_not_equal_10(card))
    spades_array.append("|        |")

    spades_array.append("|     ** |")
    spades_array.append("|    *__*|")
    spades_array.append("|     || |")
    
    spades_array.append(spades_array[0])
    return spades_array

def club(card):
    clubs_array = []
    clubs_array.append("----------")
    clubs_array.append("| ()     |")
    clubs_array.append("|()()    |")
    clubs_array.append("| ||     |")

    clubs_array.append("|        |")
    clubs_array.append(check_card_not_equal_10(card))
    clubs_array.append("|        |")

    clubs_array.append("|     () |")
    clubs_array.append("|    ()()|")
    clubs_array.append("|     || |")
    
    clubs_array.append(clubs_array[0])
    return clubs_array


if __name__ == "__main__":
    for emp, diamond, heart, spade, club in zip(empty(), diamond("A"), heart("A"), spade("A"), club("A")):
        
        print(emp + " " + diamond + " " + heart + " " + spade + " " + club)

    

