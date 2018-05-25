# coding: utf-8
from vis.models.indexed_piece import Importer
import sys
import pprint as pp


horiz_setts = {
    'quality': True,
    'simple or compound': 'simple',
    'directed': True
}


vert_setts = {
    'quality': True,
    'simple or compound': 'compound',
    'directed': True,
}


ngram_setts = {
    'n': 2,
    'vertical': 'all',
    'horizontal': 'all'
}


def get_vertical_combinations(partlist):
    return [[('{},{}'.format(upper, lower),)]
            for idx, lower in enumerate(partlist)
            for upper in partlist[idx+1:]]


def get_horizontal_combinations(partlist):
    return [[(lower, upper), ]
            for idx, lower in enumerate(partlist)
            for upper in partlist[idx+1:]]


def get_part_combinations(partlist):
    vertical = get_vertical_combinations(partlist)
    horizontal = get_horizontal_combinations(partlist)
    return list(zip(vertical, horizontal))


def run_analysis(filename):
    s = Importer(filename)
    v = s.get_data('vertical_interval', vert_setts)
    h = s.get_data('horizontal_interval', horiz_setts)
    parts = [x for x in s._metadata['parts']]
    # Assuming parts come from higher to lower and reversing
    parts = list(reversed(parts))
    combinations = get_part_combinations(parts)
    for vertical, horizontal in combinations:
        ngram_setts['vertical'] = vertical
        ngram_setts['horizontal'] = horizontal
        ngram = s.get_data('ngram', data=[v, h], settings=ngram_setts)
        for k1, v1 in ngram.to_dict().items():
            for k2, v2 in v1.items():
                print('{}: {}'.format(k2, v2))


if __name__ == '__main__':
    filename = sys.argv[1]
    run_analysis(filename)
