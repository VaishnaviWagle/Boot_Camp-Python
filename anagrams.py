def anagrams_pgm(strings):
    dictionary = {}
    for w in strings:
        sorted_w = ''.join(sorted(w))
        print(sorted_w)
        
        if sorted_w in dictionary:
            dictionary[sorted_w].append(w)
        else:
            dictionary[sorted_w] = [w]
    return list(dictionary.values())


strings = ['eat', 'ant', 'tan','ate',  'tea']
ans = anagrams_pgm(strings)
print(ans)
























    
# from collections import defaultdict

# def anagrams_pgm(strings):
#     groups = defaultdict(list) 
#     for s in strings:
#         key = ''.join(sorted(s)) 
#         groups[key].append(s)     
#     return groups.values()