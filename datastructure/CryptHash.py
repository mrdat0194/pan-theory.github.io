#!/usr/bin/env python
# coding: utf-8

# # Chapter 12 - Cryptography
#
# @ Copyright Imran Ahmad
#

# ## 1 Substitution Ciphers
#

# ### 1.1 Caesar Cipher
#
# In Caesar cipher the substitution mapping is created by replacing each character by the third character to the right.

# In[16]:


import string
key = 3
P = 'CALM'; C=''
for letter in P:
   C = C+ (chr(ord(letter) + key))
print(C)


# ### 1.2 ROT13 Cipher

# In[17]:


import codecs
P = 'CALM'
C=''
C=codecs.encode(P, 'rot_13')
print(C)


# In[18]:


import codecs
my_bytes = b"Algorithms are great"
codecs.encode(my_bytes, "base64")


# In[19]:


my_bytes


# # 2 Hashing
#

# ### 2.1 MD5
# In Python, we can generate the MD5 hash as follows:

# In[20]:


get_ipython().system('pip install passlib')


# In[21]:


from passlib.hash import md5_crypt


# In[22]:


myHash = md5_crypt.hash("myPassword")


# In[23]:


myHash


# In[24]:


md5_crypt.verify("myPassword", myHash)


# In[25]:


md5_crypt.verify("myPassword2", myHash)


# ### 2.2 SHA
# Let us see how we can use Python to create a hash using SHA algorithm:

# In[26]:


get_ipython().system('pip install passlib')
import hashlib


# In[27]:


from passlib.hash import sha512_crypt


# In[28]:


myHash =sha512_crypt.using(salt = "qIo0foX5",rounds=5000).hash("myPassword")


# In[29]:


myHash


# ## 3 Symmetic Encrption
# Now, let us look into how we can use symmetric encryption using Python.
# Now, let us look into how we can use symmetric encryption using Python.

# In[30]:


get_ipython().system('pip install cryptography')
import cryptography as crypt
from cryptography.fernet import Fernet


# Let us generate the key:

# In[31]:


key = Fernet.generate_key()
print(key)


# In[32]:


file = open('mykey.key', 'wb')
file.write(key)
file.close()


# In[33]:


file = open('mykey.key', 'rb')
key = file.read()
file.close()


# In[34]:


from cryptography.fernet import Fernet
message = "Ottawa is really cold".encode()

f = Fernet(key)
encrypted = f.encrypt(message)


# In[35]:


decrypted = f.decrypt(encrypted)


# In[36]:


print(decrypted)


# In[37]:


get_ipython().system('ls')


# In[ ]:




