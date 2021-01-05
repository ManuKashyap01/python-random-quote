import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=14
  rd=random.randint(0,last)
  print(quotes[rd],end='')
  print(quotes[random.randint(0,rd)],end='')
  print(quotes[random.randint(0,rd)],end='')


if __name__== "__main__":
  primary()
