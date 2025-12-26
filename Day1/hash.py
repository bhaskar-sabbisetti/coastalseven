import bcrypt
password="bhaskar_6281"
salt=bcrypt.gensalt()
pas='bhaskar_6281'
hashed=bcrypt.hashpw(password.encode(),salt)
print(bcrypt.checkpw(pas.encode(),hashed))