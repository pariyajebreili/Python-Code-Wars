# https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python
'''
Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]
 
The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.
'''
# 1
DENSITY = {'H': 1.36, 'W': 1, 'A': 0.87, 'O': 0.8}

def separate_liquids(glass):
    if not glass:
        return []
    column = len(glass[0])
    liquids = sorted((b for a in glass for b in a), key=lambda c: DENSITY[c])
    return [liquids[d:d + column] for d in range(0, len(liquids), column)]

print(separate_liquids([['A','A','O','H'],['A', 'H', 'W', 'O'],['W','W','A','W'],['H','H','O','O']]))

# 2
def separate_liquids(glass):
    chain = sorted(sum(glass, []), key = 'HWAO'.index)
    return [[chain.pop() for c in ro] for ro in glass]