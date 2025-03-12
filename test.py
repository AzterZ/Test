print("Hello World!)
n = int(input())
print(n)

var1 = 25
def ile_dzielnikow(a):
  sum = 0
  for i in range(1,a+1):
    if a%i == 0:
      sum += 1
  print(sum)
ile_dzielnikow(var1)
