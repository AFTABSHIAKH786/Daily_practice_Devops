str1 = "devOps ENgineer"

print(str1.title())

uppr = "Python"
lowr = "pYTHON"


if uppr.lower() == lowr.lower() :
    print("Equal")
else:
    print("Not Equal")

print()


extra_space = "   Automation Rocks! "

print(extra_space.lstrip(' '))


fun = "DevOps is hard"

print(fun.replace("hard", "fun"))


sent = "Ansible and Azure are amazing tools"

print(sent.lower().count('a'))

#  Intermediate

mail = "john.doe@company.com"

domain = mail.split("@")

print(domain[1])

isalpha = "Python3"

if isalpha.isalpha() == False :
    print("Contains numbers, not purely alphabetic")
else :
    print("Is aplhabatic")

revers = "learn python daily"

split_words = revers.split()

reversed_words = [word[::-1] for word in split_words]

print(' '.join(reversed_words))


service = "nginx"
status = "running"

print(f"Service : {service.upper()} | Status : {status.upper()}")

