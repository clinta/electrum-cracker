import itertools
import electrum
import unicodedata

words = u"tribe lady provide usual disagree small end hurt place genre neutral wagon"
pub = "xpub661MyMwAqRbcFMdvbfzf2JcUvVZPxa1eqWNKwgp9QkNNJvj5tr6Gt86FkvpL4ooUvyMrEHY2fUusdULFxpp9ej46aESgWQzJmEB8xdi2Fj1"

s = open('/home/clint/src/github.com/spesmilo/electrum/lib/wordlist/english.txt').read().strip()
s = unicodedata.normalize('NFKD', s.decode('utf8'))
lines = s.split('\n')
wordlist = []
for line in lines:
    line = line.split('#')[0]
    line = line.strip(' \r')
    assert ' ' not in line
    if line:
        wordlist.append(line)

i = 0
z = len(words.split())
while i <= z:
  s = electrum.WalletStorage('/home/clint/.electrum/wallets/smart-cr-tst')
  arr = words.split()
  for w in wordlist:
    seed = " ".join(arr[:i] + [w] + arr[i:])
    print seed
    try:
      w = electrum.Wallet.from_text(seed, None, s)
      if w.get_master_public_key() == pub:
        print 'success'
        break
    except BaseException:
      pass
  i += 1
