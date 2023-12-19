cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH',
         '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',
         '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',
         '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS']

cards_model = {'2H': 100, '3H': 101, '4H': 102, '5H': 103, '6H': 104, '7H': 105, '8H': 106, '9H': 107, 'TH': 108,
               'JH': 109, 'QH': 110, 'KH': 111, 'AH': 112,
               '2D': 300, '3D': 301, '4D': 302, '5D': 303, '6D': 304, '7D': 305, '8D': 306, '9D': 307, 'TD': 308,
               'JD': 309, 'QD': 310, 'KD': 311, 'AD': 312,
               '2C': 500, '3C': 501, '4C': 502, '5C': 503, '6C': 504, '7C': 505, '8C': 506, '9C': 507, 'TC': 508,
               'JC': 509, 'QC': 510, 'KC': 511, 'AC': 512,
               '2S': 700, '3S': 701, '4S': 702, '5S': 703, '6S': 704, '7S': 705, '8S': 706, '9S': 707, 'TS': 708,
               'JS': 709, 'QS': 710, 'KS': 711, 'AS': 712}

combinations = {
    9: 'Royal_Flush',
    8: 'Straight_Flush',
    7: 'Four_of_a_Kind',
    6: 'Full_House',
    5: 'Flush',
    4: 'Straight',
    3: 'Three_of_a_Kind',
    2: 'Two_Pair',
    1: 'One_Pair',
    0: 'High_Card'
}
