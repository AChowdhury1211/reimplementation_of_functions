import random

class Bob_Card:
    def __init__(self, lst, num):
        self.lst = lst
        self.num = num
        
    def initial_len(self):
        self.len1 = len(self.lst)
        print(self.len1)
        
    def Cards(self):
        self.lst.sort(reverse=True)
        r = random.randint(0, len(self.lst) - 1)
        if self.num == self.lst[r]:
            l_final = len(self.lst)
            turn = self.len1 - l_final
            print(f"On the {turn} turn: Bob wins")
        else:
            self.lst.pop(r)
            self.Cards()
    
cards = [3, 1, 4, 1, 5, 9, 2, 6, 5,10]
num = 4
bob_card = Bob_Card(cards, num)
bob_card.initial_len()
bob_card.Cards()