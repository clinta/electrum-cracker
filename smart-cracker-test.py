import itertools
import electrum

words = u"tribe lady provide usual disagree small end hurt place genre neutral able wagon"
pub = "xpub661MyMwAqRbcFMdvbfzf2JcUvVZPxa1eqWNKwgp9QkNNJvj5tr6Gt86FkvpL4ooUvyMrEHY2fUusdULFxpp9ej46aESgWQzJmEB8xdi2Fj1"

i = 0
while i < 12:
  s = electrum.WalletStorage('/home/clint/.electrum/wallets/smart-cr-tst')
  arr = words.split()
  print len(arr)
  arr[i], arr[i+1] = arr[i+1], arr[i]
  seed = " ".join(arr)
  try:
    w = electrum.Wallet.from_text(seed, None, s)
    print seed
    if w.get_master_public_key() == pub:
      print 'success'
      break
  except BaseException:
    pass
  i += 1
