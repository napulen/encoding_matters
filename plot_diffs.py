# coding: utf-8
from vis.models.indexed_piece import Importer
import matplotlib.pyplot as plt
import numpy as np

lower_limit = 0
upper_limit = -1

if __name__ == '__main__':
    parts = ['Violin I', 'Violin II', 'Viola', 'Violoncello']
    a = Importer('encodings/a.musicxml')
    b = Importer('encodings/b.musicxml')
    c = Importer('encodings/c.musicxml')
    an = a.get_data('noterest')
    bn = b.get_data('noterest')
    cn = c.get_data('noterest')
    index = an.index.union(bn.index.union(cn.index))
    an = an.reindex(index).fillna('tie')
    bn = bn.reindex(index).fillna('tie')
    cn = cn.reindex(index).fillna('tie')
    ab = an == bn
    bc = bn == cn
    ca = cn == an
    abm = ab.values[lower_limit:upper_limit].T
    bcm = bc.values[lower_limit:upper_limit].T
    cam = ca.values[lower_limit:upper_limit].T
    index = index[:upper_limit]
    measureoffsets = np.arange(0, len(index[lower_limit:upper_limit]), 3.0)
    fig, ax = plt.subplots(3, sharex=True)
    ax[0].imshow(abm, cmap='gray_r', aspect='auto')
    ax[0].set_title('Encoding A vs Encoding B', loc='right')
    # ax[0].set_xticks(index[:limit])
    # ax[0].set_xticklabels(index)
    ax[0].set_yticks(np.arange(len(parts)))
    ax[0].set_yticklabels(parts)
    ax[1].imshow(bcm, cmap='gray_r', aspect='auto')
    ax[1].set_title('Encoding B vs Encoding C', loc='right')
    # ax[1].set_xticks(np.arange(len(measureoffsets)))
    # ax[1].set_xticklabels(index)
    ax[1].set_yticks(np.arange(len(parts)))
    ax[1].set_yticklabels(parts)
    ax[2].imshow(cam, cmap='gray_r', aspect='auto')
    ax[2].set_title('Encoding C vs Encoding A', loc='right')
    # ax[2].set_xticks(index[:limit])
    # ax[2].set_xticklabels(measureoffsets)
    ax[2].set_xlabel('Attack number')
    ax[2].set_yticks(np.arange(len(parts)))
    ax[2].set_yticklabels(parts)
    # ax[2].set_xtitle('Attack')

    plt.show()
