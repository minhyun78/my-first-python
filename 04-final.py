train = ['성진', '찬경', '준영']
train.append('주아')
print(train)

train.insert(0, '동빈')
print(train)

train.sort()
print(train)

fruits = ['바나나', '두리안', '망고']
if '딸기' in fruits :
    fruits.remove('딸기')
    print(fruits)
else :
    print('"딸기"는 fruits 안에 없습니다.')