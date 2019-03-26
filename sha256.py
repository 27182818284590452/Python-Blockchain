# small script to the hashfunction used!
# import sha256
from hashlib import sha256

# text to hash
text = "This is the hashcode!"
hash_result = sha256(text.encode()).hexdigest()

# print result
print(hash_result)