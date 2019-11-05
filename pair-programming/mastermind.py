# master mind game pairing with Angela and waj.

colors = [1,2,3,4,5,6]
code = [2,1,4,3]


def make_guess(code):
  print("Please guess")
  guess = list(map(int, list(input())))
  return guess


def check_right_spots(guess, codecopy):
  right_spot = 0
  for i in range(len(guess)):
    if guess[i] == codecopy[i]:
      right_spot += 1
      guess[i] = 0
      codecopy[i] = 0
  return right_spot


def check_right_color(guess, codecopy):
  right_color = 0
  for i in range(len(guess)):
    if guess[i] == 0:
      continue
    if guess[i] in codecopy:
      right_color += 1
      codecopy.remove(guess[i])
  return right_color


def move():
  guess = make_guess(code)
  codecopy = code.copy()
  right_spots = check_right_spots(guess, codecopy)
  right_color = check_right_color(guess, codecopy)
  print("You had ", right_spots, " right spots and ", right_color, " right colors")
  return right_spots

moves = 0
while moves < 10:
  print('you have',10-moves,'moves remaining')
  moves += 1

  right_spots = move()

  if right_spots == 4:
    print('you did it!')
    break

  
