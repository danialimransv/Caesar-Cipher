def countingdown(x):
  if x > 0:
    print(x)
    countingdown(x - 1)
  else:
    print(x)

def countingwhiledown(x):
  while x > 0:
    print(x)
    x -= 1

x = 12
countingwhiledown(x)
