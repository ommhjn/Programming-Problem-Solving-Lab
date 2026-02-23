set_a=set(map(int,input("Set A: ").split()))
set_b=set(map(int,input("Set B: ").split()))
union=set_a | set_b
print("Union:",union)
intersection= set_a & set_b
print("Intersection:",intersection)
difference=set_a-set_b
print("Difference:",difference)