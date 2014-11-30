# coding: utf-8

'''
    magi.utils
    ~~~~~~~~~~

    Utilities.
'''


def chunks(seq, chunk_size):
    '''Chunk a sequence.

    :param seq: sequence.
    :param chunk_size: chunk size.
    '''
    for i in range(0, len(seq), chunk_size):
        yield seq[i:i + chunk_size]
