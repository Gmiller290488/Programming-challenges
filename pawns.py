# Given a list of positions of pawns on a chess board
# return a count of how many pawns are safe
# safe in this sense meaning that a differing pawn could take any piece that attacks a pawn

def safe_pawns(pawns):
    # sets are used for unordered collections of unique elements
    pawns_indexes = set()
    # for each pawn in the list
    for p in pawns:
        #convert the number to a row coordinate
        row = int(p[1]) - 1
        # use ord to find the number that correspondes to the letter for coordinate
        col = ord(p[0]) - 97
        # add each coord to the set
        pawns_indexes.add((row, col))
    print(pawns_indexes)
    count = 0

    #for each coord in the pawns_indexes...
    for row, col in pawns_indexes:
        # check if there is a pawn behind and to either side.
        is_safe = ((row-1, col-1) in pawns_indexes) or ((row-1, col+1) in pawns_indexes)
        # if there is...
        if is_safe:
            #increase count
            count += 1

    return count
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})