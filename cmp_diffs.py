import sys


def read(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [l[:-1] for l in lines
             if l[:2] not in ['@@', '++', '--', '\n']]
    return lines


def parseIndex(index):
    diff = 1 if index[0] not in ['+', '-'] else 0
    indstr = index[1:]
    m, o = indstr.split(':')
    offset = ((float(m) - 1) * 3.0) + float(o)
    return offset, diff


def comp(filename):
    d = dict()
    lines = read(filename)
    for l in lines:
        lsplit = l.split(',')
        index = lsplit[0]
        offset, diff = parseIndex(index)
        d[offset] = diff
    return d


if __name__ == '__main__':
    filename = sys.argv[1]
    d = comp(filename)
    for k, v in d.items():
        print('{}\t{}'.format(k, v))
