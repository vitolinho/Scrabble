# Fonction qui permet de récupérer 3 mots parmi n'importe qu'elle liste.
from random import randint
def choose_words(Liste):
# ça choisit 3 mots aléatoirement et les injecte dans une nouvelle liste.
  firstword = Liste[randint(0,len(Liste)-1)]
  guess_list = []
  guess_list.append(firstword)
  Liste.remove(firstword)
  secondword = Liste[randint(0,len(Liste)-1)]
  guess_list.append(secondword)
  Liste.remove(secondword)
  lastword = Liste[randint(0,len(Liste)-1)]
  guess_list.append(lastword)
  return guess_list

# Fonction qui permet de mélanger les mots sélectionné de la fonction d'au dessus,et de retirer les doublons.
from random import shuffle
def fusion(Liste):
  string = ""
  for L in Liste:
    string += L
  Liste_fusion = list(dict.fromkeys(list(string)))
  shuffle(Liste_fusion)
  return Liste_fusion

# Fonction avec les manches, les points, et les différentes actions du joueur possibles.
def play(round):
  # Liste avec des mots de 4 lettres
  Liste_base1 = ["chat","mots","nuit","lune","jour","velo","noir","tour"]
  # Liste avec des mots de 6 lettres
  Liste_base2 = ["ananas","chaton","ballon","aviron", "bonbon",]
  # Liste avec des mots de 8 lettres 
  Liste_base3 = ["elephant","pingouin","montagne","question","albatros"]
  points = 0
# Tout ce qui va se passer pour le round 1:  
  if round == 1:
    three_words_liste1 = choose_words(Liste_base1)
    final_list = fusion(three_words_liste1)
    print("Voici le mélange des lettres des trois mots à trouver: \x1b[1m\x1b[34;49m" , "".join(final_list))
    print("\x1b[33;49m-----MANCHE 1-----\x1b[0m")
    
# Boucle avec un compteur de points par manche, et permettant 3 essais de retrouver les 3 mots de cette manche et il y a aussi
# le quit qui permet d'abandonner la manche en cours.
    points_counter1 = 0
    i = 0
    while i < 3:
      answer_player = input("\x1b[3mSaissisez un mot (si vous voullez passer a la manche suivante tapez [skip]) : \x1b[0m")
      if answer_player == three_words_liste1[0] or answer_player == three_words_liste1[1] or answer_player == three_words_liste1[2] :
        points_counter1 = points_counter1 + 1
        print(f"\x1b[32;49mBravo! Vous avez trouvé {points_counter1}/3 des bonnes réponses. \x1b[0m")
        points += 1
      elif answer_player == "skip" or answer_player == "Skip":
        print("\x1b[1mManche terminée\x1b[0m")
        break
      else:
        print("\x1b[1m\x1b[31;49mMauvaise réponse ...\x1b[0m")  
      i = i + 1
    
    
    print(f"\x1b[35;49mVous avez remportez {points_counter1} points cette manche.\x1b[0m")
    print("-" * 50)
    
    
  
# Tout ce qui va se passer pour le round 1: 
  elif round == 2:
    
    three_words_liste2 = choose_words(Liste_base2)
    final_list = fusion(three_words_liste2)
    print("Voici le mélange des lettres des trois mots à trouver: \x1b[1m\x1b[34;49m" , "".join(final_list))
    print("\x1b[33;49m-----MANCHE 2-----\x1b[0m")
    
# Boucle avec un compteur de points par manche, et permettant 3 essais de retrouver les 3 mots de cette manche et il y a aussi
# le quit qui permet d'abandonner la manche en cours.
    points_counter2 = 0
    i = 0
    while i < 3:
      answer_player = input("\x1b[3mSaissisez un mot (si vous voullez passer a la manche suivante tapez [skip]) : \x1b[0m")
      if answer_player == three_words_liste2[0] or answer_player == three_words_liste2[1] or answer_player == three_words_liste2[2] :
        points_counter2 = points_counter2 + 1
        print(f"\x1b[32;49mBravo! Vous avez trouvé {points_counter2}/3 des bonnes réponses. \x1b[0m")
        points += 1
      elif answer_player == "Skip" or answer_player == "skip" :
        print("\x1b[1mManche terminée\x1b[0m")
        break
      else:
        print("\x1b[1m\x1b[31;49mMauvaise réponse ...\x1b[0m")  
      i = i + 1
    
    print(f"\x1b[35;49mVous avez remportez {points_counter2} points cette manche.\x1b[0m")
    print("-" * 50)

# Tout ce qui va se passer pour le round 1:
  else:
    three_words_liste3 = choose_words(Liste_base3)
    final_list = fusion(three_words_liste3)
    print("Voici le mélange des lettres des trois mots à trouver: \x1b[1m\x1b[34;49m" , "".join(final_list))
    print("\x1b[33;49m-----MANCHE 3-----\x1b[0m")
    
# Boucle avec un compteur de points par manche, et permettant 3 essais de retrouver les 3 mots de cette manche et il y a aussi
# le quit qui permet d'abandonner la manche en cours.
    points_counter3 = 0
    i = 0
    while i < 3:
      answer_player = input("\x1b[3mSaissisez un mot (si vous voullez passer a la manche suivante tapez [skip]) : \x1b[0m")
      if answer_player == three_words_liste3[0] or answer_player == three_words_liste3[1] or answer_player == three_words_liste3[2] :
        points_counter3 = points_counter3 + 1
        print(f"\x1b[32;49mBravo! Vous avez trouvé {points_counter3}/3 des bonnes réponses. \x1b[0m")
        points += 1
      elif answer_player == "Skip" or answer_player == "skip":
        print("\x1b[1mManche terminée\x1b[0m")
        break
      else:
        print("\x1b[1m\x1b[31;49mMauvaise réponse ...\x1b[0m")  
      i = i + 1
    
    print(f"\x1b[35;49mVous avez remportez {points_counter3} points cette manche.\x1b[0m")
  return points

# c'est le jeu.
def mix_words_GAME():

# Boucle avec un compteur de rounds pour pouvoir utilisé la fonction play() et aussi un compteur de points totaux 
  rounds = 0
  points = 0
  while rounds < 3 : 
    if rounds == 0:
      points += play(1) 
    elif rounds == 1:
      points += play(2)
    else:
      points += play(3)
    rounds = rounds + 1 
  print("-" * 50)
  print(f"\x1b[1m\x1b[35;49mFélicitations, vous avez gagné {points} points sur 9 au total.\x1b[0m")
  print("\x1b[1mA LA PROCHAINE ...")
  print("FIN DU JEU\x1b[0m")

#fonction menu du jeu
def menu():
  print("""\x1b[1m

███████  ██████ ██████   █████  ██████  ██████  ██      ███████ 
██      ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      
███████ ██      ██████  ███████ ██████  ██████  ██      █████   
     ██ ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      
███████  ██████ ██   ██ ██   ██ ██████  ██████  ███████ ███████
  \x1b[0m""")
  
  print("""\x1b[1m\x1b[35;49m
  1 - Lancer la partie
  2 - Crédits
  3 - Quitter le jeu
  \x1b[0m""")
  menu_choice = input("\x1b[3mEntrez la valeur 1 ou 2: \x1b[0m")
  if menu_choice == "1":
    print("")
    print("")
    mix_words_GAME()
  
  elif menu_choice == "2":
    print("Le créateur de ce jeu est \x1b[1mVitomir LACES\x1b[0m")
    input("\x1b[3mTapez sur Entrez pour quitter les crédits\x1b[0m")
    menu()
  elif menu_choice == "3":
    print("\x1b[1m\x1b[31;49mVous avez quittez le jeu")
    print("Au revoir \x1b[0m")
    return

menu()
