import random


class rock_paper_scissors:
    def ai_choose(self):
        self.options = ["rock", "paper", "scissors"]
        self.dict = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        # Computer Choice
        choice_idx = random.randint(0,2)
        comp_choice = self.options[choice_idx]
        print("AI's choice: ", comp_choice)
        return comp_choice
        
    def user1_choose(self):
    
        human_choice1 = input("User1 enter your choice: ").lower()
        if human_choice1 == "scissor":
            human_choice1 = "scissors"
        elif human_choice1 not in self.options:
            print("Invalid choice. Please choose from rock, paper, scissors")
            human_choice1 = input("User1 enter your choice: ").lower()
        elif human_choice1 == ["exit", "quit", "q"]:
            print("Exiting the game")
            exit()
        return human_choice1
            
    def user2_choose(self):
            
        human_choice2 = input("User2 enter your choice: ").lower()
        if human_choice2 == "scissor":
            human_choice2 = "scissors"
        elif human_choice2 not in self.options:
            print("Invalid choice. Please choose from rock, paper, scissors")
            human_choice1 = input("User2 enter your choice: ").lower()
        elif human_choice2 ==  ["exit", "quit", "q"]:
            print("Exiting the game")
            exit()   
        return human_choice2
    
    def check_who_wins_among_3_players(self, comp_choice, human_choice1, human_choice2):
        
        # check if tie
        if comp_choice == human_choice1 == human_choice2:
            print(f"All three players chose {comp_choice}. It's a tie!")
        
        # when both humans pick the same option
        elif human_choice1 == human_choice2:
            if self.dict[human_choice1] == comp_choice:
                print("User1 and User2 wins")
                self.check_who_wins_among_2_humans()
            else:
                print("AI wins")
                
        # when user1 and computer pick the same option
        elif comp_choice == human_choice1:
            if self.dict[comp_choice] == human_choice2:
                print("User1 and AI wins")
                self.check_who_wins_among_user1_ai()
            else:
                print("User2 wins")
              
        # when user2 and computer pick the same option
        elif  comp_choice == human_choice2:
            if self.dict[comp_choice] == human_choice1:
                print("User2 and AI wins")
                self.check_who_wins_among_user2_ai()
            else:
                print("User1 wins")
                
        else:
            print("Try Again")
        
        
    def check_who_wins_among_user1_ai(self):
        comp_choice = self.ai_choose()
        human_choice1 = self.user1_choose()
        if self.dict[comp_choice] == human_choice1:
            print("AI wins")
        else:
            print("User1 wins")
        
            
    def check_who_wins_among_user2_ai(self):
        comp_choice = self.ai_choose()
        human_choice2 = self.user2_choose()
        if self.dict[comp_choice] == human_choice2:
            print("AI wins")
        else:
            print("User2 wins")
    
    def check_who_wins_among_2_humans(self):
        human_choice1 = self.user1_choose()
        human_choice2 = self.user2_choose()
        if self.dict[human_choice1] == human_choice2:
            print("User1 wins")
        else:
            print("User2 wins")
        
            
    def play(self):
        comp_choice = self.ai_choose()
        human_choice1 = self.user1_choose()
        human_choice2 = self.user2_choose()
        self.check_who_wins_among_3_players(comp_choice, human_choice1, human_choice2)
        

obj = rock_paper_scissors()
obj.play()
        