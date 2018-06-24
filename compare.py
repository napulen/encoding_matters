# coding: utf-8
import music21
import sys


def make_offset_dictionary(t1p):
    t1d = dict()
    for x in t1p:
        li = t1d.get(x.offset, [])
        li.append(x)
        t1d[x.offset] = li
    return t1d


def find_onsets(encoding, translation):
    e = music21.converter.parse(encoding)
    t1 = music21.converter.parse(translation)
    e_parts = e.parts
    match = []
    discrepancy = []
    missing = []
    total = []
    for i in range(len(e_parts)):
        t1d = {}
        e_notes = e_parts[i].flat.getElementsByClass([
            music21.note.Note,
            music21.note.Rest,
            music21.chord.Chord])
        t1p = t1.parts[i].flat.getElementsByClass([
            music21.note.Note,
            music21.note.Rest,
            music21.chord.Chord])
        t1d = make_offset_dictionary(t1p)
        for n in e_notes:
            total.append(n)
            if n.offset not in t1d:
                missing.append(n)
                continue
            identical = False
            for x in t1d[n.offset]:
                if x == n:
                    identical = True
                    break
            match.append(n) if identical else discrepancy.append(n)
    return len(total), len(match), len(discrepancy), len(missing)


if __name__ == '__main__':
    encoding = sys.argv[1]
    translation = sys.argv[2]
    summary = find_onsets(encoding, translation)
    tot, ok, disc, miss = summary
    oneperc = 100 / tot
    okperc = ok * oneperc
    discperc = disc * oneperc
    missperc = miss * oneperc
    print('''
        Total notes:{}
        Matches:{}, {:.2f}%
        Discrepancies:{}, {:.2f}%
        Missing:{}, {:.2f}%
        '''.format(tot, ok, okperc, disc, discperc, miss, missperc))
