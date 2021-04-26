x = ["big" , "small" , "light" , "heavy"]
y = ["silver" , "gold" , "granite" , "platinum"]

a=0
b=0

for i in x:
    for j in y:
        print(x[a],y[b])
        b += 1
    a += 1
    b = 0
