from vis.models.indexed_piece import Importer
import sys


def run_analysis(filename):
    s = Importer(filename)
    nr = s.get_data('noterest')
    lines = [' '.join(l.split()) for l in nr.to_string().split('\n')]
    for line in lines[2:]:
        ind, b, t, a, s = line.split(' ')
        print('{}:{}, {}, {}, {}, {}'.format(int(float(ind) / 3) + 1, float(ind) % 3, b, t, a, s))


if __name__ == '__main__':
    filename = sys.argv[1]
    run_analysis(filename)
