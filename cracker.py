import itertools
import electrum
import unicodedata

words = u'cargo series gloom wing normal velvet view sock wing rib fat acid'
pub = "xpub661MyMwAqRbcFdEFzAGcVaokv2MXeRTFRjZVUu5eNusyYYkcmV4HWBCjuodH82WhmRytEyHLQSRsNSuNo8DjtzDoYk69o7pfHwi9N5gTqa7"

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

for word in wordlist:
  for i in range(0, len(words.split())):
    s = electrum.WalletStorage('/home/clint/.electrum/wallets/smart-cr-tst')
    arr = words.split()
    seed = " ".join(arr[:i] + [word] + arr[i:])
    try:
      w = electrum.Wallet.from_text(seed, None, s)
      if w.get_master_public_key() == pub:
        print seed
        print 'success'
        break
    except BaseException:
      pass
    i += 1
