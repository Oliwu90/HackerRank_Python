n_eng = int(input())
eng_sub = set(map(int, input().split()))
print(eng_sub)

n_fren = int(input())  
fren_sub = set(map(int, input().split()))
print(fren_sub)

unique_sub = eng_sub.union(fren_sub)

print(unique_sub)
print(len(unique_sub))
