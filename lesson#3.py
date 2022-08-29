secret_code1 = "NATO"
secret_code2 = "EU"
answer = input("what is the secret code?")

if answer == secret_code1 or answer == secret_code2:
    print("correct!")
    if answer == secret_code2:
        print("legend!")
else:
    print("try again!")
