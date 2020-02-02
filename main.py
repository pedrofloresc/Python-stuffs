

def numbers(num):
    count = 0
    for i in range(10):
        if num.count(str(i)) > 0:
            count += count + num.count(str(i))
    if count > 1:
        return True
    return False


def has_special(spec):
    specialcharlist = ['!', '@', '#', '$', '%', '&', '*']
    count = 0
    for i in specialcharlist:
        if spec.count(i) > 0:
            count += count + spec.count(i)
    if count > 1:
        print("hasspecial True")
        return True
    print("hasspecial False")
    return False


def IsValid(passw):
    if len(passw) > 6 and numbers(passw) and has_special(passw):
        return True
    return False


def Validate_Password(password):
    if IsValid(password):
        print("Strong")
    else:
        print("Weak")


if __name__ == "__main__":
    Validate_Password(input("enter your pass"))
