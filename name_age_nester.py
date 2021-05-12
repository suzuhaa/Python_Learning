Dict_ages = {}
while True:
    while True:
        print('Please enter your name.')
        name = input()
        if not name.replace(' ','').isalpha():
            print('Please enter your name in alphabetic letters.')
            continue
        name = name.title()
        print(f"Your name is {name}, correct?\n(if True,enter 't', if False, enter 'f'. )")
        feedback_1 = input()
        if feedback_1 == 't':
            break
        else:
            continue
        name = name.title()
        print(name)

    while True:
        print('Please enter your age here. ')
        age = input()
        try:
            age = int(age)
        except:
            print('Please enter numeric digits. ')
            continue
        if age < 1:
            print('Please enter a positive number.')
            continue
        print(f"Your name is {age}, correct?\n(if True,enter 't', if False, enter 'f'. )")
        feedback_2 = input()
        if feedback_2 == 't':
            break
        else:
            continue
    Dict_ages[name]=age
    print(f"Now we have collected age data of {len(Dict_ages)}, continue?"
          f"\n(if True,enter 't', if False, enter 'f'.")
    feedback_3=input()
    if feedback_3=='t':
        continue
    else:
        break
print(Dict_ages)
for item in Dict_ages.items():
    print(item[0]+"'s age is "+str(item[1]))

