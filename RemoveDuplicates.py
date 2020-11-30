#random sequence generator
import random

def _random_seq(length):
    seq = []
    for _ in range(length):
        seq.append(random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ))
    return seq

#remove duplicates from list without losing order
def remove_duplicates():
    seq = _random_seq(1000)
    checked = []
    [checked.append(i) for i in seq if not checked.count(i)]
    return checked
