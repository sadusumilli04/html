user_1 = raw_input("Enter rock, paper, or scissors :")
user_2 = raw_input("Enter rock, paper, or scissors :")
if user_1 == 'rock' and user_2 == 'paper':
  print "User 2 wins!!!"
if user_1 == 'rock' and user_2 == 'scissors':
  print "User 1 wins!!!"
if user_1 == 'rock' and user_2 == 'rock':
  print "It's a tie!!!"
if user_1 == 'paper' and user_2 == 'rock':
  print "User 1 wins!!!"
if user_1 == 'paper' and user_2 == 'scissors':
  print "User 2 wins!!!"
if user_1 == 'paper' and user_2 == 'paper':
  print "It's a tie!!!"
if user_1 == 'scissors' and user_2 == 'paper':
  print "User 1 wins!!!"
if user_1 == 'scissors' and user_2 == 'rock':
  print "User 2 wins!!!"
if user_1 == 'scissors' and user_2 == 'scissors':
  print "It's a tie!!!"
