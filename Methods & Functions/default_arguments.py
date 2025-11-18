def net_price(price, discount=0, tax=0.05):
    return price * (1 - discount) * (1 + tax)


x = net_price(500)
y = net_price(500, 0.1)
print(x)  # 525.0
print(y)  # 472.5
