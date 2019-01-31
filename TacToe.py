#Tic Tac Toe: 
#Author: Lebohang Clifford Mohale

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http:#www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# =========================
# The Piece class
# =========================
class Piece(object):
    '''
	This is a Piece class : Piece is chosen prints instructions, and then makes a move,
	whereby on each move the Board gets updated and a Win condition is checked
	''' 
    def __init__(self, boardStructure, values):
        self.board = ['A','B','C','D','E','F','G','H','I'] #Default bogus values
        self.moves = [1,2,3,4,5,6,7,8,9]
        self.boardStructure = boardStructure
        self.values = values
        self.pieceOptions = []

        self.printInstrucions()
        self.selectPiece()
        self.makeMove()
	
    def printInstrucions(self):
        '\tPrints the Game\'s instructions and valid moves'
        print("\n Tic Tac Toe Game by Lebohang Clifford Mohale \n", self.boardStructure\
          		% (self.moves[0],self.moves[1],self.moves[2],\
				   self.moves[3],self.moves[4],self.moves[5],\
				   self.moves[6],self.moves[7],self.moves[8]))

    def selectPiece(self):
        '\tSelects a piece from the availabe options'
        while len(self.pieceOptions) != 2:
            selection = input("Choose piece : X or O\n").upper()
            if selection == 'X':
                self.pieceOptions.append('X')
                self.pieceOptions.append('O')
            elif selection == 'O':
                self.pieceOptions.append('O')
                self.pieceOptions.append('X')
            else:
                print("Incorrect Selection !")
	
    def makeMove(self):
        '\tenables each piece to make a move.On each move a Board is updated and a Win is Validated'
        while len(self.moves) != 0:
            for option in self.pieceOptions:
                if len(self.moves) == 0: break

                currentPlayer = option 
                print("\nPlayer %s Select your Move Amougst : " % (currentPlayer), self.moves) 				
                move = int(input())
                
                if move not in self.moves:
                    self.makeMove()
                    break	
				#Bug Here : The currentPlayer variable should not be Updated on Error Move 
                    
                self.updateBoard(move, currentPlayer)
                self.checkWin(currentPlayer)
                self.moves.remove(move)
				
    def updateBoard(self, move, val):
            '- Updates the Board & structure on Move'
            if move == 1:
                self.values[0] = val
                self.board[0]= val				
            elif move == 2:
                self.values[1] = val
                self.board[1]= val				
            elif move == 3:
                self.values[2] = val
                self.board[2]= val				
            elif move == 4:
                self.values[3] = val
                self.board[3]= val				
            elif move == 5:
                self.values[4] = val
                self.board[4]= val
            elif move == 6:
                self.values[5] = val
                self.board[5]= val
            elif move == 7:
                self.values[6] = val
                self.board[6]= val
            elif move == 8:
                self.values[7] = val
                self.board[7]= val				
            elif move == 9:
                self.values[8] = val
                self.board[8] = val
		
            print(self.__str__())
            return 

    #Check whether the Playing piece has Won?
    def checkWin(self,currentPlayer):
        'Checks whether the current move/turn has resulted in a Win'
        if self.board[0] == self.board[1] == self.board[2]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[3] == self.board[4] == self.board[5]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[6] == self.board[7] == self.board[8]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[0] == self.board[3] == self.board[6]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[1] == self.board[4] == self.board[7]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[2] == self.board[5] == self.board[8]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[0] == self.board[4] == self.board[8]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
        elif self.board[2] == self.board[4] == self.board[6]:
            print("Player %s Has Won!" %(currentPlayer))
            return sys.exit(0)
					
    def __str__(self):
        '- Python method overriding to return the Console represantation of the Board'
        return	self.boardStructure % (self.values[0],self.values[1],self.values[2],\
					                   self.values[3],self.values[4],self.values[5],\
									   self.values[6],self.values[7],self.values[8])
									   
# =========================
# The TicTacToeBoard class
# =========================

class TicTacToeBoard(object):
    '''
	This is a Board class, this class Draws a Board and Puts (Instantiates), Pieces on that Board
	'''			 
    def __init__(self):

        self.values = [' '] * 9 
        self.boardStructure = '''
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
       '''
        piece = Piece(self.boardStructure, self.values)
        print('\n Game draw no winner \n')
		
#PLAY
game = TicTacToeBoard()
		
		
       	          


