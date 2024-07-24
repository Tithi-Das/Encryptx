#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def get_user_choice():
  choice = input("Enter your choice (rock, paper, scissors): ").lower()
  if choice in ["rock", "paper", "scissors"]:
    return choice
  else:
    print("Invalid choice!")
    return get_user_choice()


# In[3]:


def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)


# In[4]:


def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "tie"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
    return "user"
  else:
    return "computer"


# In[5]:


def display_result(user_choice, computer_choice, winner):
  print(f"User chose {user_choice}")
  print(f"Computer chose {computer_choice}")
  if winner == "user":
    print("User wins!")
  elif winner == "computer":
    print("Computer wins!")
  else:
    print("It's a tie!")


# In[6]:


def main():
  user_score = 0
  computer_score = 0

  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    if winner == "user":
      user_score += 1
    elif winner == "computer":
      computer_score += 1
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")
    play_again = input("Do you want to play again (yes/no)? ").lower()
    if play_again != "yes":
      break


# In[ ]:


if __name__ == "__main__":
  main()


# In[ ]:




