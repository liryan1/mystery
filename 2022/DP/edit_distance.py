def editDistance(word1: str, word2: str) -> int:
    ''' Dynamic Programming 
    horse, ros -> 3
    intention, execution -> 5

    initialize a table of length of both words + 1
    the first row and column are the same as the index:
        we can edit the word by replacing every single char

    after filling the first row and first column, the rest of
    the table (i, j) are filled using the allowed operations:
        1. insert a character: 1 + tab[i-1][j]
        2. delete a character: 1 + tab[i][j-1]
        3. replace a character: 1 + tab[i-1][j-1]
    Take the minimum and fill each slot in the table.
    '''
    m, n = len(word1), len(word2)
    tab = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            # covers 0th row and column
            if not i or not j:
                tab[i][j] = i or j
                continue

            if word1[i-1] == word2[j-1]:
                tab[i][j] = tab[i-1][j-1]

            else:
                tab[i][j] = 1 + min(tab[i-1][j-1],
                                    tab[i-1][j], tab[i][j-1])

    return tab[-1][-1]
