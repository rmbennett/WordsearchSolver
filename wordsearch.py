

def traverse(words, grid):
 	print words
 	print grid


def parse():
 	pass

def setup_grid():
	with open("grid") as gridFile:
		grid = [line.split() for line in gridFile]
	# print grid
	return grid

def setup_word_list():
	with open("wordlist") as wordFile:
		words = wordFile.read().splitlines()  
	# print words
	return words

if __name__ == '__main__':
	grid = setup_grid()
	if not grid[0][0] == 'N':
		raise AssertionError("The first letter of the grid should be N")
	if not grid[14][15] == 'D':
		raise AssertionError("D Test failed")
	
	words = setup_word_list()
	if not words[0] == 'amazon':
		raise AssertionError("Word list read in incorrectly")
	
	traverse(words, grid)