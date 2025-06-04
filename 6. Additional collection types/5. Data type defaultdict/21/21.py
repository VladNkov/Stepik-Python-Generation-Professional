from collections import defaultdict


def wins(pair):
    pairs_dict = defaultdict(set)
    for winner, loser in pair:
        pairs_dict[winner].add(loser)
    return pairs_dict


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))