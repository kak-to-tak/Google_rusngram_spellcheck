import sys
from functools import reduce
# from typing import List, Tuple, Dict, Set, Union
# import torch
# import torch.nn as nn
# import torch.nn.utils
# import torch.nn.functional as F
# from torch.nn.utils.rnn import pad_packed_sequence, pack_padded_sequence

def char_probs(model, dataset, vocab):
    for i in range(10):
        x, y, word_len = dataset[i]
        x = x.to(device)
        y = y.to(device)
        y_pred = model(x)[0]
        probs = []
        output = vocab.transform_vec(y[:word_len])
        for char_idx in range(1,word_len[0]):
            char = output[char_idx]
            if char=='<':
                break
            idx = vocab.char2idx[char]
#             print(output[char_idx])
#             print()
#             print(y_pred[char_idx][idx])
            probs.append(y_pred[char_idx][idx])
            multiplication = reduce(lambda x, y: x*y, probs)
        return multiplication/(word_len-1)