def countingdown:
  if x > 0:
    print(x)
    countingdown(x - 1)
  else:
    print(x)

x = 3
countingdown(x)
