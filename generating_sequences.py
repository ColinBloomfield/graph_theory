# split up into a program that looks at permutations
# and a program that looks at candidate labelings

import math
# seq = [int(x) for x in input("enter integers separated by spaces: ").split()]
# n = int(input("Enter Value for n: "))
# k = int(input("Enter Value for k: "))

# metric on cyclic graphs
def dist(v1, v2, n):
    return min(abs(v1-v2), n-(abs(v1-v2)))


def get_label(gen_seq, n, k):
    label = [0 for x in range(n)]
    for x in range(1, len(gen_seq)):
        k_vals = []
        for y in range(x):
            k_vals.append(k+1+label[gen_seq[y]]-dist(gen_seq[y], gen_seq[x], n))
        label[gen_seq[x]] = max(k_vals)
    return label


def get_lb(n, k):
    phi = math.ceil((3*k-n+3)/2)
    if n % 2 == 0:
        return ((n/2)-1)*phi+k+1-n/2
    else:
        return ((n-1)/2)*phi



def print_seq(gen_seq, seq, labeling, Rkn, n, k):
    print("Seqence: ", seq)
    print("Generating Sequence: ", gen_seq)
    print("Ratio: ", len(gen_seq), ' ', n)
    if len(labeling) == n:
        print("Labeling: ", labeling)
        print("Rkn: ", Rkn)
    print()


# this code block generates the jump sequence
# if the sequence is a permutation it passes the
# sequence to get_label.
def generate(seq, n, k):
    gen_seq = []
    gen_seq.append(0)
    for iter in range(n):
        gen_seq.append((gen_seq[iter] + seq[iter % len(seq)]) % n)
        for y in range(len(gen_seq)-1):
            if gen_seq[y] == gen_seq[-1]:
                del gen_seq[-1]
                break
        else:
            continue  # executed if the loop ended normally (no break)
        break
    labeling = []
    Rkn = math.inf
    if len(gen_seq) == n:
        labeling = get_label(gen_seq, n, k)
        Rkn = max(labeling)
    seq_data = [gen_seq, seq, labeling, Rkn, n, k]
    return seq_data


if __name__ == '__main__':

    # USER INPUT!!!
    q = 7
    m = 1

    # Determined by user input.
    n = 4*q
    k = 2*q + 2*m + 1
    d = 0
    if n % 2 == 0:
        d = int(n/2)
    else:
        d = int((n-1)/2)

    # USER INPUT!!! Data contains generating sequences.
    data = [[x, y] for x in range(q, n-q) for y in range(q, n-q)]
    #data = [[x1, x2, x3, x4, x5, x6] for x1 in range(q, d+q) for x2 in range(q, d+q)
            # for x3 in range(q, d+q) for x4 in range(q, d+q) for x5 in range(q, d+q) for x6 in range(q, d+q)]

    gen_list = []
    for seq in data:
        gen_list.append(generate(seq, n, k))

    min_Rkn = min([ seq_data[3] for seq_data in gen_list])
    for seq_data in gen_list:
        if seq_data[3] == min_Rkn:
            print_seq(*seq_data)

    print(get_lb(n, k))