# WordsearchSolver

### Problem: 
Given a 2D board of reasonably small size (5000x5000) and a gigantic list of words (think petabytes, not all the words in the dictionary exist in the grid), find out which words exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally, vertically, or diagonally neighbouring.

### Initial Thoughts 

1. The grid is much smaller than the list of words.
2. Therefore we should probably iterate over the list of words once due to memory access times, and the grid once per word.
3. Unfortunately words could be "subwords" so we can't discount starting locations and directions once we've found one word there.
4. Edges and Corners of the grid are edge cases so we want to handle those slightly differently.
5. I should just start writing and stop theorising.  
