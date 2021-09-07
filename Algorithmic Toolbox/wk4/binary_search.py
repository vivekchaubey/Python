def search(a,l,r,q):
    if r<l:
        return -1

    mid=int(l+(r-l)/2)
    if q==a[mid]:
        return mid
    elif q<a[mid]:
        return search(a,l,mid-1,q)
    else:
        return search(a,mid+1,r,q)


def binary_search(keys, query):
    # write your code here
    srch = search(keys, 0, len(keys)-1, query)
    return srch


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
