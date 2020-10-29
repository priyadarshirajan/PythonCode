secure = (("a", "@"), ("i", "!"), ("s", "5"))
def SecurePassword(password):
    for a,b in secure:
        password = password.replace(a,b)
    return password

_password = input("Enter any password here ")
res = SecurePassword(_password)
print(res)