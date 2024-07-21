from collections import defaultdict

def group(strs):
    angram = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        angram[sorted_str].append(s)
    
    return list(angram.values())

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group(arr)
print(output)
