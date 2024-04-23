# Import
import time, random, pygame

# Sounds
pygame.mixer.init()
rotate = pygame.mixer.Sound('Rotate.wav')
move = pygame.mixer.Sound('Move.wav')
line = pygame.mixer.Sound('Line.wav')
gameover = pygame.mixer.Sound('GameOver.wav')
blocked = pygame.mixer.Sound('Blocked.wav')

# Screen
WINDOW_WIDTH, WINDOW_HEIGHT = 300, 550
BOARD_WIDTH , BOARD_HEIGHT  = 12, 22
BOX_SIZE                    = 25
BLANK                       = '.'

# Colors  ((R)    (G)    (B))
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)
ORANGE      = (255, 165,   0)
LIGHTORANGE = (255, 140,   0)
PURPLE      = (148,   0, 211)
LIGHTPURPLE = (153,  50, 204)

# Groups
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW,      ORANGE,      PURPLE)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW, LIGHTORANGE, LIGHTPURPLE)

# Shapes
S_SHAPE = [['.00', '00.',], ['0.', '00', '.0',]]
Z_SHAPE = [['00.', '.00',], ['.0', '00', '0.',]]
I_SHAPE = [['0', '0', '0', '0'], ['0000']]
O_SHAPE = [['00', '00']]
J_SHAPE = [['0..', '000'], ['00', '0.', '0.'], ['000', '..0'], ['.0', '.0',  '00']]
L_SHAPE = [['..0', '000'], ['0.', '0.', '00'], ['000', '0..'], ['00', '.O', '.0.']]
T_SHAPE = [['.0.', '00O'], ['0.', '00', '0.'], ['000', '.0.'], ['.0', '00',  '.O']]

SHAPES = {'S': S_SHAPE,'Z': Z_SHAPE,'J': J_SHAPE,'L': L_SHAPE,'I': I_SHAPE,'O': O_SHAPE,'T': T_SHAPE}

# Game Loop
class Board(object):
    # Initialize Board
    def __init__(self):
        self.m_array = [[BLANK] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

    # Add Piece to the Board
    def addToBoard(self, piece):
        shape =  SHAPES[piece.getShapeIndex()][piece.getRotation()]
        height = len(shape)
        width =  len(shape[0])

        for y in range(height):
            for x in range(width):
                if shape[y][x] != BLANK:
                    self.m_array[y + int(piece.getPosY() / BOX_SIZE)][x + int(piece.getPosX() / BOX_SIZE)] = piece.getColor()

    # Draw Piece on the Board
    def draw(self, screen):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.m_array[y][x] != BLANK:
                    pygame.draw.rect(screen, COLORS[int(self.m_array[y][x])], (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                    pygame.draw.rect(screen, LIGHTCOLORS[int(self.m_array[y][x])], (x * BOX_SIZE + 1, y * BOX_SIZE + 1, BOX_SIZE - 2, BOX_SIZE - 2))

    # Checking if Line is Full
    def isCompleteLine(self, y):
        for x in range(BOARD_WIDTH):
            if self.m_array[y][x] == BLANK: return False
        return True

    # Removing the Line if Filled
    def removeCompleteLines(self):
        y =   BOARD_HEIGHT - 1
        numOfCompleteLines = 0

        while y >= 0:
            if self.isCompleteLine(y):
                numOfCompleteLines += 1
                for pullDownY in range(y, 0, -1):
                    for x in range(BOARD_WIDTH):
                        self.m_array[pullDownY][x] = self.m_array[pullDownY - 1][x]

                for x in range(BOARD_WIDTH):
                    self.m_array[0][x] = BLANK
            else:
                y -= 1
        return numOfCompleteLines

    # Return the (x, y) Position of the Piece
    def get(self, x, y):
        return self.m_array[y][x]

class Piece(object):
    # Initialize Piece
    def __init__(self):
        self.m_shapeIndex = random.choice(list(SHAPES.keys()))
        self.m_position = {'x' : int(WINDOW_WIDTH + 0.5 * WINDOW_WIDTH) - 35, 'y' : WINDOW_HEIGHT / 3.5}
        self.m_color = random.randint(0, len(COLORS) - 1)
        self.m_rotation = random.randint(0, len(SHAPES[self.m_shapeIndex]) - 1)
        self.m_shape = SHAPES[self.m_shapeIndex][self.m_rotation]
        self.m_shapeHeight = len(self.m_shape)
        self.m_shapeWidth = len(self.m_shape[0])

    # Return Piece Information
    def getShapeIndex(self): 
        return self.m_shapeIndex
    def getRotation(self): 
        return self.m_rotation
    def getPosX(self): 
        return self.m_position['x']
    def getPosY(self): 
        return self.m_position['y']
    def getColor(self): 
        return self.m_color
    
    # Set Piece Information
    def setPos(self, x, y):
        self.m_position['x'] = x
        self.m_position['y'] = y
    def setRotation(self, rotation):
        self.rotation = rotation

    # Move Piece
    def move(self, x, y, board):
        if self.isValidPosition(x, y, board):
            self.m_position['x'] += x
            self.m_position['y'] += y
            return True
        else: return False

    # Determine if Piece Position makes sense
    def isValidPosition(self, additionX, additionY, board):
        for y in range(self.m_shapeHeight):
            for x in range(self.m_shapeWidth):
                if self.m_shape[y][x] == BLANK: continue

                xPos = x + int((self.m_position['x'] + additionX) / BOX_SIZE)
                yPos = y + int((self.m_position['y'] + additionY) / BOX_SIZE)

                if xPos < 0 or xPos >= BOARD_WIDTH or yPos >= BOARD_HEIGHT: return False
                if board.get(xPos, yPos) != BLANK: return False
        return True

    # Rotation of the Pieces
    def rotate(self, board):
        shape = SHAPES[self.m_shapeIndex][(self.m_rotation + 1) % len(SHAPES[self.m_shapeIndex])]
        width = len(shape[0])

        rotation =       self.m_rotation
        shape =             self.m_shape
        shapeHeight = self.m_shapeHeight
        shapeWidth =   self.m_shapeWidth

        self.m_rotation = (self.m_rotation + 1) % len(SHAPES[self.m_shapeIndex])
        self.m_shape = SHAPES[self.m_shapeIndex][self.m_rotation]
        self.m_shapeHeight = len(self.m_shape)
        self.m_shapeWidth = len(self.m_shape[0])

        if (self.m_position['x'] + width * BOX_SIZE) <= WINDOW_WIDTH and self.isValidPosition(0, 0, board):
            pass
        else:
            self.m_rotation =       rotation
            self.m_shape =             shape
            self.m_shapeWidth =   shapeWidth
            self.m_shapeHeight = shapeHeight
            pygame.mixer.Sound.play(blocked) 

    # Drawing of the Pieces
    def draw(self, screen):
        for y in range(self.m_shapeHeight):
            for x in range(self.m_shapeWidth):
                if self.m_shape[y][x] != BLANK:
                    pygame.draw.rect(screen, COLORS[self.m_color], (self.m_position['x'] + x * BOX_SIZE, self.m_position['y'] + y * BOX_SIZE, BOX_SIZE, BOX_SIZE))
                    pygame.draw.rect(screen, LIGHTCOLORS[self.m_color], (self.m_position['x'] + x * BOX_SIZE + 1, self.m_position['y'] + y * BOX_SIZE + 1, BOX_SIZE - 2, BOX_SIZE - 2))

class RunGame(object):
    # Initialize Game
    def __init__(self):
        self.m_board = Board()
        self.m_currPiece = None
        self.m_nextPiece = Piece()
        self.m_pieceFalling = False
        self.m_gameOver = False
        self.m_direction = {'left' : False, 'right' : False, 'down' : False}
        self.m_rotate = False
        self.m_lastFallTime = time.time()
        self.m_lastMoveTime = time.time()
        self.m_score = 0

        pygame.init()
        self.m_screen = pygame.display.set_mode((WINDOW_WIDTH * 2, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')

    # Piece Moving Logic
    def logic(self):
        if time.time() - self.m_lastMoveTime > 0.1:
            if self.m_direction['left'] == True:    
                self.m_currPiece.move(-BOX_SIZE, 0, self.m_board)
            elif self.m_direction['right'] == True: 
                self.m_currPiece.move(BOX_SIZE, 0 , self.m_board)
            elif self.m_direction['down'] == True:  
                self.m_currPiece.move(0 , BOX_SIZE, self.m_board)
            self.m_lastMoveTime = time.time()
        elif self.m_rotate:
            self.m_currPiece.rotate(self.m_board)
            self.m_rotate = False

    # Draw the Matrix Lines
    def drawLines(self):
        for i in range(BOARD_WIDTH + 1):
            pygame.draw.line(self.m_screen, GRAY, (i * BOX_SIZE, 0), (i * BOX_SIZE, WINDOW_HEIGHT))
        for j in range(BOARD_HEIGHT):
            pygame.draw.line(self.m_screen, GRAY, (0 , j * BOX_SIZE), (WINDOW_WIDTH, j * BOX_SIZE))

    # Define the Text
    def textObjects(self, text, font):
        textSurface = font.render(text, True, GRAY)
        return textSurface, textSurface.get_rect()

    # Define the Score Display 
    def displayScore(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        textSurf, textRect = self.textObjects('Score: '  + str(self.m_score), font)
        textRect.center = (WINDOW_WIDTH + 0.5 * WINDOW_WIDTH , WINDOW_HEIGHT / 1.5)
        textSurf2, textRect2 = self.textObjects('Next Piece:', font)
        textRect2.center = (WINDOW_WIDTH + 0.5 * WINDOW_WIDTH  , WINDOW_HEIGHT / 6)
        self.m_screen.blit(textSurf,   textRect)
        self.m_screen.blit(textSurf2, textRect2)

    # Draw the Board and Pieces
    def draw(self):
        if self.m_gameOver: return
        self.m_screen.fill(BLACK)
        self.drawLines()
        self.m_board.draw(self.m_screen)
        self.m_currPiece.draw(self.m_screen)
        self.m_nextPiece.draw(self.m_screen)
        self.displayScore()
        pygame.display.update()

    # Player Inputs
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.m_gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:     
                    self.m_direction['left'] =   True
                    pygame.mixer.Sound.play(move)
                elif event.key == pygame.K_RIGHT:  
                    self.m_direction['right'] =  True
                    pygame.mixer.Sound.play(move)
                elif event.key == pygame.K_DOWN:   
                    self.m_direction['down'] =   True
                    pygame.mixer.Sound.play(move)
                elif event.key == pygame.K_SPACE:
                    self.m_rotate =              True
                    pygame.mixer.Sound.play(rotate)  
                elif event.key == pygame.K_ESCAPE: 
                    self.m_gameOver =            True
                    pygame.mixer.Sound.play(gameover)  

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:     
                    self.m_direction['left'] =  False
                elif event.key == pygame.K_RIGHT:  
                    self.m_direction['right'] = False
                elif event.key == pygame.K_DOWN:   
                    self.m_direction['down'] =  False

    # Piece Updates
    def update(self):
        if time.time() - self.m_lastFallTime > 1:
            if self.m_pieceFalling:
                if self.m_currPiece.move(0, BOX_SIZE, self.m_board): 
                    pass
                else:
                    self.m_pieceFalling = False
                    self.m_board.addToBoard(self.m_currPiece)
                    self.m_score += self.m_board.removeCompleteLines() * 100
                    pygame.mixer.Sound.play(line)  

                self.m_lastFallTime = time.time()

        if not self.m_pieceFalling:
            self.m_currPiece = self.m_nextPiece
            self.m_nextPiece = Piece()
            self.m_currPiece.setPos(int(WINDOW_WIDTH / 2) - 50, 0)
            self.m_pieceFalling = True
            if not self.m_currPiece.isValidPosition(0, 0, self.m_board): 
                self.m_gameOver = True

    def runGame(self):
        while not self.m_gameOver:
            self.update()
            self.input()
            self.logic()
            self.draw()

c = RunGame()
c.runGame()
pygame.quit()