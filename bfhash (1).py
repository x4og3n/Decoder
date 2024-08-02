import hashlib
import base64

def decode_hash(hash_to_decode, wordlist):
    with open(wordlist, 'r', errors='ignore') as f:
        for line in f:
            word = line.strip()
            md5_hash = hashlib.md5(word.encode()).hexdigest()
            sha1_hash = hashlib.sha1(word.encode()).hexdigest()
            sha256_hash = hashlib.sha256(word.encode()).hexdigest()
            sha512_hash = hashlib.sha512(word.encode()).hexdigest()
            base64_encode = base64.b64encode(word.encode()).decode()

            if md5_hash == hash_to_decode:
                print("MD5 hash qırıldı! Parol:", word)
                return
            elif sha1_hash == hash_to_decode:
                print("SHA-1 hash qırıldı! Parol:", word)
                return
            elif sha256_hash == hash_to_decode:
                print("SHA-256 hash qırıldı! Parol:", word)
                return
            elif sha512_hash == hash_to_decode:
                print("SHA-512 hash qırıldı! Parol:", word)
                return
            elif base64_encode == hash_to_decode:
                print("Base64 hash qırıldı! Parol:", word)
                return

    print("Bu wordlist ilə hash qırıla bilmədi.")

# 'hash_to_decode' - Qırmak istədiyiniz hashi bu ilə əvəz edin
hash_to_decode = "sizin_hashiniz"
# 'rockyou.txt' - Wordlistinizin yolu ilə əvəz edin
wordlist = "rockyou.txt"

decode_hash(hash_to_decode, wordlist)
