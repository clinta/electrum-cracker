import itertools
from electrum import bitcoin
from unicodedata import normalize

words = u"cargo series gloom wing normal velvet sock acid fat view wing rib"

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
    #self.add_master_public_key(name, xpub)

for subset in itertools.permutations(words.split()):
  seed = " ".join(subset)
  if bitcoin.is_new_seed(seed):
    print(seed)
    print(xpub_from_seed(seed))

