import random


# Mesaj de primire + reguli
print('Welcome to our childhood game: \"Rock, Paper, Scissors\" ')
print("Let's start the game!")
print(''' Rules:
          First rule: 1 means Rock.
          Second rule: 2 means Paper.
          Third rule: 3 means Scissors
''')

# Numar incercari: 9
# 1r = 1r
# 1r = 2p
# 1r = 3f
#
# 2p = 1r
# 2p = 2p
# 2p = 3f
#
# 3f = 1r
# 3f = 2p
# 3f = 3f

# Selectare piatra, hartie, foarfeca
select = int(input('Select: '))

# Selectare random a computerului
rand_number = random.randint(1,3)
print(f'Computer chose {rand_number}')

# Conditii
if select == 1 and rand_number == 1:
    print('We are equal. Try again!')
elif select == 1 and rand_number == 2:
    print('Paper beats rock! Computer won this round!')
elif select == 1 and rand_number == 3:
    print('Rock beats scissors! You won this round.')
elif select == 2 and rand_number == 1:
    print('Paper beats rock. You win.')
elif select == 2 and rand_number == 2:
    print('Hmm, paper equals paper. We are even.')
elif select == 2 and rand_number == 3:
    print('Scissors beats paper. Computer won this round.')
elif select == 3 and rand_number == 1:
    print('Rock beats scissors. Computer win')
elif select == 3 and rand_number == 2:
    print('Scissors beat paper. You won!')
elif select == 3 and rand_number == 3:
    print('We are equal, scissors versus scissors.')
