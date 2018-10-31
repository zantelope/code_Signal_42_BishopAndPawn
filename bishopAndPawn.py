def bishopAndPawn(b, p):

    ## change input values into integers that corerspond to their position on a chessboard
    ## ord() function changes input to a string representing it's ascii value
    ## change both values to ints
    b = [int(ord(b[0]) - 96), int(b[1])]
    p = [int(ord(p[0]) - 96), int(p[1])]

    ## if x values are equal to zero, return False (cannot divide by 0)
    if p[0] - b[0] == 0:
        return False
    
    ## absolute value of the slope (y2 - y1 / x2 - x1) will be equal to 1 if pawn is on bishop's potential paths
    if abs((p[1] - b[1]) / (p[0] - b[0])) == 1:
      return True
    ## if slope is not 1, return false
    else:
      return False
