# url 编码
from urllib import parse

quote = parse.quote("你好！")
print(quote)

unquote = parse.unquote(quote)
print(unquote)


# base64 编码
import base64

encode = base64.b64encode(b'Hello Cyberist')
print(encode)

decode = base64.b64decode(encode)
print(decode)


# md5 不可逆 基本上没有重复 做文件名 比较文件是否相同
# message-digest algorithm 5  信息摘要算法
import hashlib

md = hashlib.md5()
md.update("你好！".encode('utf-8'))  # unicode-objects must be encoded before hashing
print(md.hexdigest())

md_2 = hashlib.md5(bytes("abc", encoding='utf-8'))  # 加了参数之后就是在原来的加密基础上再加密一层
md_2.update(bytes("admin", encoding='utf-8'))
print(md_2.hexdigest())


# sha1 加密
# Secure Hash Algorithm 安全哈希算法
sha1 = hashlib.sha1("你好".encode('utf-8')).hexdigest()
print(sha1)

# sha256 加密  hashlib中间还有许多类似的加密
sha256 = hashlib.sha256("你好！".encode("utf-8")).hexdigest()
print(sha256)


# DES
from Crypto.Cipher import DES
text = 'Cyberist'

key = b'Edgar123'  # 8 位
des = DES.new(key, DES.MODE_ECB)
encode = des.encrypt(text.encode("utf-8"))
print(encode)


# AES  advanced encryption standard
from Crypto.Cipher import AES
from Crypto import Random

data = "你好"
# key's length must be 16(AES-128) 24(AES-192) 21(AES-256)
key = b'this is a 16 key'

# 生成长度为AES块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须是16的倍数，如果长度不为16的倍数，需补足
# 将iv加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode("utf-8"))
print("AES encode: ", ciphertext)

# 解密 AES
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
decrypttext = mydecrypt.decrypt(ciphertext[16:])
print(decrypttext.decode())


# RSA 加密
import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(pubkey, privkey)
data = 'Cyberist'.encode()
crypto = rsa.encrypt(data, pubkey)
print("crypto: ", crypto)
decode = rsa.decrypt(crypto, privkey)
print(decode)

