sum = 0
for i in [3,6,9]:
    sum = sum + i
print(sum)

mix = '쌀씰쌀쌀씰쌀씰쌀씰쌀쌀씰쌀씰쌀씰쌀쌀씰쌀씰쌀씰쌀쌀씰쌀씰쌀씰쌀씰쌀씰쌀쌀씰쌀씰쌀씰쌀쌀씰쌀씰쌀씰쌀쌀씰쌀씰'
count = 0
for i in mix:
    if i == '쌀' :
        count = count + i
print(count)