def compare(version_a: str, version_b: str) -> int:
    list_A = version_a.split('.')
    list_B = version_b.split('.')

    for i in range(min(len(list_A), len(list_B))):
        if int(list_A[i]) == int(list_B[i]):
            continue
        else:
            return -1 if int(list_A[i]) < int(list_B[i]) else 1

    if len(list_A) == len(list_B):
        return 0
    else:
        return -1 if len(list_A) < len(list_B) else 1


