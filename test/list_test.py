# 列表操作
squares = [x**2 for x in range(0, 11)]
print(squares)

lm = [(x, y) for x in [1, 3, 4] for y in [2, 3, 5] if x != y]
print(lm)

a = [1, 2, 3]
z = [x + 1 for x in [x**2 for x in a]]
print(z)

x, y = divmod(15, 2)
print('x : {}, y : {}'.format(x, y))
print(type(z))

basket = {'123', '222', '123'}
print(basket)

a = set('sdssdcdfg')
b = set('fesdeaxcsffd')
print(a)
print(a - b)
print(b - a)
print(a | b)
print(a & b)
# a | b and not a & b
print(a ^ b)