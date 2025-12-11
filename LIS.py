class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(arr, index):
# membuat tree dari arr[index] dengan children = elemen yang lebih besar di kanan
    root = Node(arr[index])

    for next_index in range(index + 1, len(arr)):
        if arr[next_index] > arr[index]:
            child = build_tree(arr, next_index)
            root.children.append(child)

    return root


def find_all_LIS_from_node(node, current_seq):
# mengumpulkan semua subsequence terpanjang dari node tertentu
    current_seq.append(node.value)

    if not node.children:
        return [current_seq.copy()]

    all_seqs = []
    max_len = 0

    for child in node.children:
        child_seqs = find_all_LIS_from_node(child, current_seq.copy())

        for seq in child_seqs:
            if len(seq) > max_len:
                max_len = len(seq)
                all_seqs = [seq]
            elif len(seq) == max_len:
                all_seqs.append(seq)

    return all_seqs


def find_all_LIS(arr):
# Membuat tree dari setiap root lalu ambil semua LIS yang panjangnya maksimum
    global_best = []
    global_len = 0

    for i in range(len(arr)):
        root = build_tree(arr, i)
        sequences = find_all_LIS_from_node(root, [])

        for seq in sequences:
            if len(seq) > global_len:
                global_len = len(seq)
                global_best = [seq]
            elif len(seq) == global_len:
                global_best.append(seq)

    unique = []
    for seq in global_best:
        if seq not in unique:
            unique.append(seq)

    return unique

# Main Program

arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("Input array:", arr)

result = find_all_LIS(arr)

print("\n=== SEMUA Largest Monotonically Increasing Subsequences ===")
for seq in result:
    print(seq)
