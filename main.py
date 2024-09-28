import pygame
pygame.init()
def game():
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    black =195,155,119
    brown =195,155,119

    screen.fill(black)
    fps = pygame.time.Clock()


    class Checkers():
        """"  This class is useful to setup up the pieces on the board.
      Methods: setup-green: which sets up the green pieces on the board
      setup: which sets up the other pieces that are on the other side
      info render: which renders which player's turn it is """

        def __init__(self):
            self.red_image = "red_piece-removebg-preview.png"
            self.green_image = "white_piece-removebg-preview.png"
            self.yellow_image = "1200px-Yellow_icon.svg-removebg-preview.png"

        def setup(self, position):
            red_check = pygame.image.load(self.red_image).convert_alpha()
            red_check = pygame.transform.scale(red_check, (60, 60))
            self.red_rect = red_check.get_rect()
            self.red_rect.centerx = position[0]
            self.red_rect.centery = position[1]
            screen.blit(red_check, self.red_rect)

        def setup_green(self, position):
            white_piece = pygame.image.load(self.green_image).convert_alpha()
            white_piece = pygame.transform.scale(white_piece, (60, 60))
            white_rect  = white_piece.get_rect()
            white_rect.centerx = position[0]
            white_rect.centery = position[1]
            screen.blit(white_piece,white_rect)
        #this is just useful to render the player's turn
        def info_render(self,player):
            black = 0,0,0
            font  = pygame.font.SysFont("Script",44)
            font_image = font.render("Checkers",black,True)
            font_rect = font_image.get_rect()
            font_rect.centerx = 837
            font_rect.centery = 42
            screen.blit(font_image,font_rect)

            font2 = pygame.font.SysFont("Script",44)
            if player == 1:
                font2_image = font2.render("Player 1", black, True)
                font2_rect = font_image.get_rect()
                font2_rect.centerx = 800
                font2_rect.centery = 140
                screen.blit(font2_image, font2_rect)
                white_piece = pygame.image.load(self.green_image).convert_alpha()
                white_piece = pygame.transform.scale(white_piece, (60, 60))
                white_rect = white_piece.get_rect()
                white_rect.centerx = 910
                white_rect.centery = 140
                screen.blit(white_piece, white_rect)
            elif player == 2:
                font2_image = font2.render("Player 2",black, True)
                font2_rect = font_image.get_rect()
                font2_rect.centerx = 800
                font2_rect.centery = 140
                screen.blit(font2_image, font2_rect)
                red_check = pygame.image.load(self.red_image).convert_alpha()
                red_check = pygame.transform.scale(red_check, (60, 60))
                red_rect = red_check.get_rect()
                red_rect.centerx = 910
                red_rect.centery = 140
                screen.blit(red_check,red_rect)









    class Movement():
        """
       Class for blocking illegal movements and making a piece king.
       Methods: init(self,location_list), locator(self)
       properties: row and columns
       """

        def __init__(self, initial_loc, location, piece_list):
            self.location = location
            self.piece_list = piece_list
            self.initial_loc = initial_loc

        def locator(self):
            """
           this function is useful just to check if the desired position
           is empty or not.
           if empty :return:  True
           """
            rows = [79, 150, 225, 299, 374, 448, 523, 598]
            columns = [88, 176, 262, 350, 437, 524, 609, 697]
            # row detection
            for i in range(8):
                if self.location[1] <= rows[i]:
                    row = i
                    break
            # column detection
            for i in range(8):
                if self.location[0] <= columns[i]:
                    column = i
                    break
            for i in range(8):
                if self.initial_loc[1] <= rows[i]:
                    row2 = i
                    break
                # column detection
            for i in range(8):
                if self.initial_loc[0] <= columns[i]:
                    column2 = i
                    break
            # zero represents an empty space in the grid, so if it is
            # zero, return true and I used the True value to confirm the move while in the loop
            if self.piece_list[row][column] == 0:
                return True

        # this function updates the piece_list(rows and columns)
        def update(self, initial_location, new_location, piece_list,player,piece1_loc,piece2_loc):
            """ This function updates the piece list, so we can keep
           track of the pieces position, using this we can detect if the jump is possible"""
            #this are the rows and columns measurement
            rows = [79, 150, 225, 299, 374, 448, 523, 598]
            columns = [88, 176, 262, 350, 437, 524, 609, 697]
            p = 0
            # row detection
            for i in range(8):
                if new_location[1] <= rows[i]:
                    row = i
                    break
            #column detection
            for x in range(8):
                if new_location[0] <= columns[x]:
                    column = x
                    break
            #row detection
            for i in range(8):
                if initial_location[1] <= rows[i]:
                    row2 = i
                    break
            #column detection
            for x in range(8):
                if initial_location[0] <= columns[x]:
                    column2 = x
                    break
            #this detects if a piece has become a king
            if player == 1:
                if row == 7:
                    p = 1

            elif player == 2:
                if row == 0:
                   p = 2


            #this checks if the player is playing the correct piece, the [0,0] in the return value is used later.

            if player == 1:
                   if piece_list[row2][column2] == 2 or piece_list[row2][column2] == 5:
                        return [2,[0,0]]
            #if player 2 is playing and the piece is assigned 1, this function will stop.
            if player == 2:
                    if piece_list[row2][column2] == 1 or piece_list[row2][column2] == 4:
                        return [2,[0,0]]
            #this blocks any piece that is trying to move backwards while its not a king
            if not (piece_list[row2][column2] == 4 or piece_list[row2][column2] == 5 or p == 1 or p == 2):
             if player == 1:
                if row2 > row:
                    return [2,[0,0]]
             if player == 2:
                    if row2 < row:
                        return [2,[0,0]]
            #if a player is moving a king piece, we want to update the piece_list and keep the piece a king
            # 4 and 5 represents kings, 4 for player 1 and 5 for player 2
            if piece_list[row2][column2] == 4:
                  replace = 4
            elif p == 1:
                replace = 4
            elif piece_list[row2][column2] == 5:
                  replace = 5
            elif p == 2:
                replace = 5
            #if its not a king then we just replace it by the player's turn(1 and 2)
            else:
                replace = player
                # so if player 2 is playing, the piece being jumped should be player 1's piece and vice versa
            if player == 2:
                jump = 1
            else:
                jump = 2

            #these statements just updates the piece_list when the piece is moved normally no jump
            #these are pattern i figured out for the normal movements
            #if either of these are not a match, then the player is trying to move it to a illegal position, nothing will happen unless the user is trying to jump
            #because nothing will be returned to change the locations
            if [row2 + 1, column2 - 1] == [row, column]:
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[0,0]]
            elif [row2 + 1, column2 + 1] == [row, column]:
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[0,0]]
            elif [row2 - 1, column2 + 1] == [row, column]:
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[0,0]]
            elif [row2 - 1, column2 - 1] == [row, column]:
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[0,0]]
            #jumps check
            #this checks if the player is jumping in the correct position and also if there is a piece in between
            #these are just patterns I figured out for the jump.
            #the jump + 3 checks if a king is being jumped, because in the piece_list kings are represented by 4 and 5
            elif [row2 + 2,column2 +2] == [row,column] and (piece_list[row2+1][column2+1] == jump or piece_list[row2+1][column2+1] == jump+3) :
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                #this return value are used to remove the piece that is jumped, used this values on another function
                return [1,[row2+1,column2+1]]
            elif [row2+2,column2-2] == [row,column] and (piece_list[row2+1][column2-1] == jump or piece_list[row2+1][column2-1]== jump+3):
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1, [row2+1,column2-1]]
            elif [row2-2,column2-2] == [row,column] and (piece_list[row2-1][column2-1] == jump or piece_list[row2-1][column2-1] == jump+3) :
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[row2-1,column2-1]]
            elif [row2-2,column2+2] == [row,column] and (piece_list[row2-1][column2+1] == jump or piece_list[row2-1][column2+1] == jump+3):
                piece_list[row][column] = replace
                piece_list[row2][column2] = 0
                return [1,[row2-1,column2+1]]
            #if nothing is a match nothing will happen, returned this value just to confirm it while in the game loop
            else:
                return[2,[0,0]]





    # this function finds the location of the click and replaces the new position on the list
    def detection(location, piece_loc,x):
        #x represents which player is playing.
        #I added + 20 and - 20 because the user click won't exactly match the location so we just take to closest match
        if x == 1:
            for i in range(len(piece1_loc)):
                if (piece_loc[i][0] - 20) <= location[0][0] <= (piece_loc[i][0] + 20):
                    if (piece_loc[i][1] - 20) <= location[0][1] <= (piece_loc[i][1] + 20):
                        piece_loc[i] = location[1]
                        break


        if x==2:
            for i in range(len(piece2_loc)):
                if (piece_loc[i][0] - 20) <= location[0][0] <= (piece_loc[i][0] + 20):
                    if (piece_loc[i][1] - 20) <= location[0][1] <= (piece_loc[i][1] + 20):
                        piece_loc[i] = location[1]
                        break



    def location_held(location, piece_loc, piece_2loc):
        """

        this function is just useful to make the piece stay exactly where is it, if the position the user
        wants to move it to is already taken. So this is just a function for robustness
        :param location:
        :param piece_loc and piece_2loc:
        :return: piece_loc or piece2_loc, depends on the given value
        """
        for i in range(len(piece1_loc)):
            if (piece_loc[i][0] - 20) <= location[0] <= (piece_loc[i][0] + 20):
                if (piece_loc[i][1] - 20) <= location[1] <= (piece_loc[i][1] + 20):
                    return piece_loc[i]
            # Checking the piece 2 location , if the piece 1 location is not a match
        for i in range(len(piece2_loc)):
            if (piece2_loc[i][0] - 20) <= location[0] <= (piece2_loc[i][0] + 20):
                if (piece2_loc[i][1] - 20) <= location[1] <= (piece2_loc[i][1] + 20):
                    return piece2_loc[i]





    def crown(piece_list):
        """

        :param piece_list:
        this is just a function that blits the crown on the king pieces
        """
        x = 0
        rows = [79, 150, 225, 299, 374, 448, 523, 598]
        columns = [88, 176, 262, 350, 437, 524, 609, 697]
        location_list10 = []
        #go over the piece_list, if 4 or 5 is detected then blit the crown on the piece
        for i in range(8):
            for x in range(8):
                if piece_list[i][x] == 4 or piece_list[i][x] == 5:
                    location_list10.append([i,x])
                    x += 1
        #blitting the crown, its x >= 1 because we need to make sure at-least one king is detected, then it won't crash
        if x >= 1:
            for i in range(len(location_list10)):
                crown_image = "king_crown-removebg-preview.png"
                crown = pygame.image.load(crown_image).convert_alpha()
                crown = pygame.transform.scale(crown, (30,30))
                crown_rect = crown.get_rect()
                crown_rect. centerx = columns[location_list10[i][1]] - 50
                crown_rect.centery = rows[location_list10[i][0]]  - 40
                screen.blit(crown, crown_rect)
        else:
            pass



    def robust(location,piece_list):
        """
        This is a function that prevents the game from crashing if the player clicks an empty space.
        :param:location and piece_list
        """
        #this is just checking if the players first  click is 0 in the piece list. if it is it returns False and we use this value in the while loop.
        rows = [79, 150, 225, 299, 374, 448, 523, 598]
        columns = [88, 176, 262, 350, 437, 524, 609, 697]
        for i in range(8):
            if location[0][1] <= rows[i]:
                row2 = i
                break
        # column detection
        for x in range(8):
            if location[0][0] <= columns[x]:
                column2 = x
                break
        for i in range(8):
            if location[1][1] <= rows[i]:
                row = i
                break
            # column detection
        for x in range(8):
            if location[1][0] <= columns[x]:
                column = x
                break
        #if either the click is 0 or the second click is not 0. we return False.
        #0 represents an empty space so if the first click is an empty space, the user didn't choose a piece
        #if the second click is not a 0, the user is trying to move it to another taken place.


        if piece_list[row2][column2] == 0 and piece_list[row][column] != 0:
            return False
        else:
            return True



    def removal(piece1_loc,piece2_loc,rocol,player,piece_list):
        """
        This method just removes a jumped piece
        :param piece1_loc:
        :param piece2_loc:
        :param rocol: is rows and columns we use this to detect which piece is jumped and we remove it from its location
        :return:
        """
        #these are the row and column measurements
        rows = [79, 150, 225, 299, 374, 448, 523, 598]
        columns = [88, 176, 262, 350, 437, 524, 609, 697]
        #this is useful to check if the user is trying to jump
        #on the previous class I returned a value [0,0] if the desired move is not jump
        #so here if it is not jump this function will not run
        if not(rocol[1] == [0,0]):
            #rocol = rows and columns
            #I also returned the row and column of the piece that is being jumped
            #using this value we can detect the location and remove it from the list.
            row = rocol[1][0]
            column = rocol[1][1]
            row2 = rows[row]
            column2 = columns[column]
            piece_list[rocol[1][0]][rocol[1][1]] = 0
            location = [row2,column2]

            #if player 2 is playing we remove the location from player 1's list
            if player == 2:
                #this goes over the entire list, it will remove a location if the clicked location is close to one of the location
                #that is found in the list, that's why i added +100 and - 100, because the user click will not get the
                #exact position
                for i in range(len(piece1_loc)):
                        if (piece1_loc[i][0]) <= location[1] <= (piece1_loc[i][0]+ 80):
                            if (piece1_loc[i][1]) <= location[0] <= (piece1_loc[i][1]+80):
                                piece1_loc.remove(piece1_loc[i])
                                break
            elif player == 1:
                for i in range(len(piece2_loc)):
                    if (piece2_loc[i][0]) <= location[1] <= (piece2_loc[i][0] + 80):
                        if (piece2_loc[i][1]) <= location[0] <= (piece2_loc[i][1] + 80):
                            piece2_loc.remove(piece2_loc[i])
                            break
        else:
            pass



    def winner(piece1_loc,piece2_loc):
        """
        this function just counts the length of the location, if either of them  is 0, then we've got a winner.
        """
        if len(piece1_loc) == 0:
            winner = 1
        elif len(piece2_loc) == 0:
            winner = 2
        else:
            winner = 0
        #its greater than or equal too one because we need to make sure a winner is detected before this runs
        if winner >= 1:
                font2 = pygame.font.SysFont("Script", 30)
                font2_image = font2.render(f"Player {winner} is the winner", (55,118,171), True)
                font2_rect = font2_image.get_rect()
                font2_rect.centerx = 840
                font2_rect.centery =  250
                screen.blit(font2_image, font2_rect)
                return True













    # __________________________________________________________________________________________________ main program
    # this lists keeps track of where the pieces are
    piece_list = [[1, 3, 1, 3, 1, 3, 1, 3], [3, 1, 3, 1, 3, 1, 3, 1], [1, 3, 1, 3, 1, 3, 1, 3], [3, 0, 3, 0, 3, 0, 3, 0]
        , [0, 3, 0, 3, 0, 3, 0, 3], [3, 2, 3, 2, 3, 2, 3, 2], [2, 3, 2, 3, 2, 3, 2, 3], [3, 2, 3, 2, 3, 2, 3, 2]]
    #these are the initial locations for piece one
    piece1_loc = [(217, 41), (53, 40), (388, 44), (563, 41), (132, 118), (305, 118), (473, 120), (658, 122),
                (566, 195), (394, 189), (220, 193), (41, 189)]
    #these are the initial locations for piece 2
    piece2_loc = [
        (126, 556), (307, 569), (481, 570), (657, 563), (573, 477), (384, 492),
        (220, 483), (29, 484), (302, 409), (478, 410), (651, 407), (130, 416)]
    removal_list =[]
    board = pygame.image.load("checkers game board2.png").convert_alpha()

    board = pygame.transform.scale(board, (700, 600))
    board_rect = board.get_rect()
    location_list = []
    counter = 0
    #this  variables keeps track of which player is playing.
    player = 0
    turn = 0
    game = True
    while game:
        screen.fill(brown, (0, 0, screen.get_width(), screen.get_height()))
        screen.blit(board, board_rect)
        location3 = [(0, 0), (0, 0)]
        setup_game = Checkers()
        #this just blits the player turn on the screen
        if turn % 2 == 0:
            setup_game.info_render(2)
        else:
            setup_game.info_render(1)
        #counter must be greater than two because both locations are needed initial and new, so if counter == 2, we can confirm we have both location to continue through
        if counter >= 2:
            #this determines which player is playing.
            if turn % 2 == 0:
                player = 1
            else:
                player = 2
            print(player)
             #taking the last 2 appended items, which determines both location(initial and new)
            location3[1] = location_list[-1]
            location3[0] = location_list[-2]
            # this checks if the users clicked location is taken or not, if it is
            # the piece stays where is it
            if (robust(location3,piece_list)== True):
                movement = Movement(location3[0], location3[1], piece_list)
                if not (movement.locator() == True):
                    # if the position is  not vacant or the position desired is illegal position(white space on the grid),
                    # the piece stays where is it.
                    location3[1] = location_held(location3[0], piece1_loc, piece2_loc)
                counter = 0
                # value represents the return value of the update method.
                value = movement.update(location3[0], location3[1], piece_list,player,piece1_loc,piece2_loc)
                #if value's first index is not one, then the movement is illegal, the piece stays where it is
                if (value)[0] != 1:
                    location3[1] = (location_held(location3[0], piece1_loc, piece2_loc))
                    counter = 0
                else:
                    #this only increases if the player is moving the right piece. So unless the player moves the right piece, the player's turn won't change
                    turn += 1
                    #setup_game.info_render(player)
                #here if the jump method is applied we remove the piece, if not nothing will happen
                removal(piece1_loc,piece2_loc,value,player,piece_list)
            else:
                pass
        #this stops the while loop if a winner is detected
        if (winner(piece1_loc,piece2_loc)== True):
            game = False
        # this displays the pieces and everytime the location changes depending on the players click.
        for i in range(len(piece1_loc)):
            detection(location3, piece1_loc,1)
            setup_game.setup((piece1_loc)[i])
        # white piece set up, using the checkers class
        for i in range(len(piece2_loc)):
            detection(location3, piece2_loc,2)
            setup_game.setup_green((piece2_loc)[i])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                counter += 1
                #appending the  mouse location to the list
                location_list.append(location)
        crown(piece_list)
        pygame.display.flip()
        fps.tick(50)
        changer = 0

    #freezing the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


game()

