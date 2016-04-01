import itertools
import random
from electrum import bitcoin
from unicodedata import normalize

words = u"cargo series gloom wing normal velvet sock acid fat view wing rib"
pub = "xpub661MyMwAqRbcFdEFzAGcVaokv2MXeRTFRjZVUu5eNusyYYkcmV4HWBCjuodH82WhmRytEyHLQSRsNSuNo8DjtzDoYk69o7pfHwi9N5gTqa7"


root_derivation = "m/"

def normalize_passphrase(passphrase):
    return normalize('NFKD', unicode(passphrase or ''))

def mnemonic_to_seed(mnemonic, passphrase):
    # See BIP39
    import pbkdf2, hashlib, hmac
    PBKDF2_ROUNDS = 2048
    mnemonic = normalize('NFKD', ' '.join(mnemonic.split()))
    passphrase = normalize_passphrase(passphrase)
    return pbkdf2.PBKDF2(mnemonic, 'mnemonic' + passphrase,
                         iterations = PBKDF2_ROUNDS, macmodule = hmac,
                         digestmodule = hashlib.sha512).read(64)

def xpub_from_seed(seed):
    # store only master xpub
    xprv, xpub = bitcoin.bip32_root(mnemonic_to_seed(seed,''))
    xprv, xpub = bitcoin.bip32_private_derivation(xprv, "m/", root_derivation)
    return xpub

def xprv_from_seed(seed):
    # we don't store the seed, only the master xpriv
    xprv, xpub = bitcoin.bip32_root(mnemonic_to_seed(seed, ''))
    xprv, xpub = bitcoin.bip32_private_derivation(xprv, "m/", root_derivation)
    return xprv

arr = words.split()
while True:
  random.shuffle(arr)
  seed = " ".join(arr)
  if bitcoin.is_new_seed(seed):
    #print xpub_from_seed(seed)
    if str(xpub_from_seed(seed)) == str(pub):
      print(seed)
      print(xprv_from_seed(seed))
      break
