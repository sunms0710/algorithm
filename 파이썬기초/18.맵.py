# %%
'''map'''

a = [1,2,3,4,5]
b = [1,4,9,16,25]

c = [*map(lambda x : x*x, a)]
print(c)
print([x*x for x in a])