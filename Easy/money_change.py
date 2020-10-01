'''
  Change your money with the min poaaible set of coins

'''

def money_change(money, coins):
  if money == 0:
    return 0;
  min_coins = float("inf")
  for coin in coins:
    if money >= coin:
      num_coins = money_change(money - coin, coins)
      min_coins = min(num_coins + 1 , min_coins)
  return min_coins

coins = [20,25,50]

print(money_change(100, coins))
