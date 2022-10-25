secret_code1 = "nato"
secret_code2 = "eu"
answer = input("What is the secret code?")

if answer == secret_code1:
    print("Correct!")
    #elif = else/if
elif answer == secret_code2:
    print("Legend!")
    secret_number =int(input("What is the secret number?"))
    if secret_number %4 == 0:
        print("Welcome!")
    else:
        print("Goodbye!")
else:
    print("Try again!")

    #if dividable by 4 then leap yr
    #if divisible by 100 then not leap yr
    #if also divisible by 400 then leap yr
    #if the remainder is 0 then the number is divisible
