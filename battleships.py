# gonna do pygame later
# gonna get battleships working first

# clear terminal
def clear():
  print("\033[2J\033[H", end="") # weird ansi escape thing

# create 2 empty 10 x 10 boards
board1 = board2 = [[" " for i in range(10)] for i in range(10)]

# let players place piees 
def initBoard():
  p1coords = p2coords = []
  clear()
  # loop through piece types
  for i in [(5, "C"), (4, "B"), (3, "D"), (3, "S"), (2, "P")]:
    # validation loop
    while True:
      # reset tempCoords
      tempCoords = []
      try:
        # ask for start coordinate
        coordStart = input("Player 1, where would you like your "+str(i[0])+"-long piece to start E.G (A1)?\n>>> ")
        print(int(coordStart[1:])-1) # num section of coords a「3」
        print(ord(coordStart[0].lower()) - 97) # letter section of coords「a」3
        # mCoordStart = board1[int(coordStart[1:])-1][ord(coordStart[0].lower()) - 97], for copy and paste
        # get end coord
        coordEnd = input("\nPlayer 1, where would you like your "+str(i[0])+"-long piece to end E.G (A1)?\n>>> ")
        # calculate points between start and end
        if int(coordStart[1:])-1 == int(coordEnd[1:])-1:
          # get minimum coord
          minCoord = min(ord(coordStart[0].lower()) - 97, ord(coordEnd[0].lower()) - 97)
          # loop through midpoints
          for j in range(i[0]):
            # add to list to deny overlaps
            tempCoords.append([int(coordStart[1:])-1, j + minCoord])
          # check if ship is vertical
        else:
          # get minimum coord
          minCoord = min(int(coordStart[1:])-1, int(coordEnd[1:])-1)
          # loop through midpoints
          for j in range(i[0]):
            tempCoords.append([j + minCoord, ord(coordStart[0].lower()) - 97])
        # check if they are i apart and not already taken
        if (((int(coordStart[1:])-1) + (i[0] - 1) == (int(coordEnd[1:])-1) and (ord(coordStart[0].lower()) - 97) == (ord(coordEnd[0].lower()) - 97)) or ((int(coordStart[1:])-1) - (i[0] - 1) == (int(coordEnd[1:])-1) and (ord(coordStart[0].lower()) - 97) == (ord(coordEnd[0].lower()) - 97)) or ((int(coordStart[1:])-1) == (int(coordEnd[1:])-1) and (ord(coordStart[0].lower()) - 97) + (i[0] - 1) == (ord(coordEnd[0].lower()) - 97)) or ((int(coordStart[1:])-1) == (int(coordEnd[1:])-1) and (ord(coordStart[0].lower()) - 97) - (i[0] - 1) == (ord(coordEnd[0].lower()) - 97))) and any(coord in p1coords for coord in tempCoords) == False:
          # reset tempCoords
          # check if ship is horizontal
          if int(coordStart[1:])-1 == int(coordEnd[1:])-1:
            print("is horizontal")
            # get minimum coord
            minCoord = min(ord(coordStart[0].lower()) - 97, ord(coordEnd[0].lower()) - 97)
            # loop through midpoints
            for j in range(i[0]):
              # add to list to deny overlaps
              p1coords.append([int(coordStart[1:])-1, j + minCoord])
              # assign values to ship type
              board1[int(coordStart[1:])-1][j + minCoord] = i[1]
          # check if ship is vertical
          else:
            # get minimum coord
            minCoord = min(int(coordStart[1:])-1, int(coordEnd[1:])-1)
            # loop through midpoints
            for j in range(i[0]):
              p1coords.append([j + minCoord, ord(coordStart[0].lower()) - 97])
              # assign values to current ship length
              board1[j + minCoord][ord(coordStart[0].lower()) - 97] = i[1]
            
          # format and print board
          for j in range(len(board1)):
            print("|", end="")
            for k in range(len(board1[j])):
              print(str(board1[j][k]) + "|", end="")
            print("")
          print("")
          # go to next iteration if input is allowed
          break
        # deny if not accepted coord
        else:
          print("no")
      except:
        print("nah")
initBoard()
