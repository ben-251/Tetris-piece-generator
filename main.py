
import random

#make class for pieces
class piece():
	def __init__(self,dot_positions):
		self.dot_positions = dot_positions

#generate a random piece
def generate():
	x_values = [0]*4
	y_values = [0]*4
	dot_positions = [0]*4

	for i in range(4):
		x_values[i] = random.randint(1, 4)
		y_values[i] = random.randint(1,4)
		dot_positions[i] = [x_values[i],y_values[i]]
	return dot_positions

#display pieces in a "tui"
def display_piece(piece):
	x_values = [0]*4
	y_values = [0]*4

	for i in range(4):
		x_values[i] = piece[i][0]
		y_values[i] = piece[i][1]
	#not complete

def is_compact(piece):
	#return true if every dot in the piece as at least one other that it makes contact with
	return True #Just for the program to work for now
	
	states = [False]*4
	x_values = [0]*4
	y_values = [0]*4

	for i in range(4):
		x_values[i] = piece[i][0]
		y_values[i] = piece[i][1]

	def check_delta(coordinate,current_dot,other_dot):
		#returns true if the other coordinate as a difference of 1, otherwise false
		if abs(coordinate[current_dot] - coordinate[other_dot]) == 1:
			return True
		else:
			return False

	#check if one x or y value matches any others
	for current_dot_position in range(len(x_values)):
		current_dot = x_values[i]
		for other_dot_position in x_values:
			other_dot = x_values[j]
			if other_dot == current_dot:
				check_delta(y_values,current_dot_position,other_dot_position)

	for current_dot_position in range(len(y_values)):
		current_dot = y_values[current_dot_position]
		for other_dot_position in y_values:
			other_dot = y_values[other_dot_position]
			if other_dot == current_dot:
				if not check_delta(x_values,current_dot_position,other_dot_position):
					return False #problem is that it shouldnt return false yet cuz there could be one match later or something. Tricky to work around.
				#if no falses after everything, then return true
		
			
		
def rotate(piece,num):
	#rotate the piece "num" times clockwise
	pass

def make_pieces(number):
	#make "number" pieces. They will be objects
	pieces = [0]*number
	for i in range(number):
		pieces[i] = piece(generate())

		if not is_compact(pieces[i]):
			make_pieces(number)
	return pieces

def get_positions(pieces): 
	#get the positions of the pieces
	positions = []
	for i in pieces:
		positions.append(i.dot_positions)
	return positions

#testing that pieces are being made properly
piece_positions = get_positions(make_pieces(5))
for i in piece_positions:
	print(i)

		