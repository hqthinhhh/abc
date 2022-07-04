import re
def Conditional_Tests():
    car = input("Tên: ").lower()
    if car == 'subaru':
        print(f'Is car == {car}? | I predict True')
    if car == 'audi':
        print(f'Is car == {car}? | I predict False')
    if car == 'suzuki':
        print(f'Is car == {car}? | I predict True')
    if car == 'yamaha':
        print(f'Is car == {car}? | I predict False')
    if car == 'honda':
        print(f'Is car == {car}? | I predict True')
    if car == 'toyota':
        print(f'Is car == {car}? | I predict False')
    if car == 'mazda':
        print(f'Is car == {car}? | I predict True')
    if car == 'kia':
        print(f'Is car == {car}? | I predict False')
    if car == 'fox':
        print(f'Is car == {car}? | I predict True')
    if car == 'subaru':
        print(f'Is car == {car}? | I predict False')
    if car == 'hyundai':
        print(f'Is car == {car}? | I predict True')

def More_Conditionali_Tests():
    name1 = 'anh'
    name2 = 'kim'
    print(name1 == name2)
    print(name1.lower() == 'anh')
    num1 = 9
    num2 = 9.5
    print(num1 == num2)
    print(num1 != num2)
    print(num1 > num2)
    print(num1 < num2)
    print(num1 >= num2)
    print(num1 <= num2)
    if name1 == 'anh' and name2 == 'anh':
        print('True')
    else:
        print('False')
    if name1 == 'an' or name2 == 'an':
        print('True')
    else:
        print('False')
    name_list = ['anh', 'an', 'kim', 'vu']
    if name1 in name_list:
        print('name1 is in the list')
    if name2 not in name_list:
        print('name2 is not in the list')

def Alien_Colors_1():
    alien_color=['green', 'yellow', 'red']
    if 'green' in alien_color:
        print('player just earned 5 points')
    else:
        print('no output')

def Alien_Colors_2():
    alien_color=['green', 'yellow', 'red']
    if 'green' in alien_color:
        print('player just earned 5 points')
    else:
        print('player just earned 10 points')

def Alien_Colors_3():
    alien_color=['green', 'yellow', 'red']
    if 'green' in alien_color:
        print('player just earned 5 points')
    elif 'red' in alien_color:
        print('player just earned 10 points')
    else:
        print('player just earned 15 points')

def Stages_of_Life():
    print("Tuổi: ", end="")
    age = int(input())
    if age>=65:
        print('elder')
    elif age>=20:
        print('adult')
    elif age>=13:
        print('teenager')
    elif age>=4:
        print('kid')
    elif age>=2:
        print('toddler')
    else:
        print('baby')

def Favorite_Fruit():
    favorite_fruit=['bananas', 'apples', 'oranges']
    if 'pineapples' in favorite_fruit:
        print('You really like pineapples!')
    if 'bananas' in favorite_fruit:
        print('You really like bananas!')
    if 'peaches' in favorite_fruit:
        print('You really like peaches!')
    if 'oranges' in favorite_fruit:
        print('You really like oranges!')
    if 'apples' in favorite_fruit:
        print('You really like apples!')

def Hello_Admin():
    usernames = ['nam', 'an', 'admin', 'binh', 'anh']
    for username in usernames:
        if username == 'admin':
            print("Do you want to see the status report?")
        else:
            print(f'Hi {username}, Thanks for signing in.')

def No_User():
    usernames = []
    if usernames:
        for username in usernames:
            if username == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print("Hello " + username + ", thank you for logging in again!")
    else:
        print("We need to find some users!")

def Checking_Usernames():
    current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
    new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
    current_users_lower = [user.lower() for user in current_users]
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("Sorry " + new_user + ", that name is taken.")
        else:
            print("Great, " + new_user + " is still available.")

def Ordinal_Numbers():
    numbers = [i for i in range(1,10)]
    for number in numbers:
        if number == 1:
            print("1st")
        elif number == 2:
            print("2nd")
        elif number == 3:
            print("3rd")
        else:
            print(str(number) + "th")

def Person():
    person = {
        'first_name': 'Quoc Thinh',
        'last_name': 'Hoang',
        'age': 21,
        'city': 'Ha Noi',
    }
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])

def Favarite_Number():
    favorite_numbers = {
        'anh': 10,
        'nam': 5,
        'nguyen': 1,
        'thanh': 9999,
        'dang': 2,
    }
    num = favorite_numbers['anh']
    print("Gus's favorite number is " + str(num) + ".")

    num = favorite_numbers['nam']
    print("Micah's favorite number is " + str(num) + ".")

    num = favorite_numbers['nguyen']
    print("Mandy's favorite number is " + str(num) + ".")

    num = favorite_numbers['thanh']
    print("Maggie's favorite number is " + str(num) + ".")

    num = favorite_numbers['dang']
    print("Hank's favorite number is " + str(num) + ".")

def Glossary():
    glossary = {
        'string': 'A series of characters.',
        'comment': 'A note in a program that the Python interpreter ignores.',
        'list': 'A collection of items in a particular order.',
        'loop': 'Work through a collection of items, one at a time.',
        'dictionary': "A collection of key-value pairs.",
    }
    word = 'string'
    print("\n" + word.title() + ": " + glossary[word])

    word = 'comment'
    print("\n" + word.title() + ": " + glossary[word])

    word = 'list'
    print("\n" + word.title() + ": " + glossary[word])

    word = 'loop'
    print("\n" + word.title() + ": " + glossary[word])

    word = 'dictionary'
    print("\n" + word.title() + ": " + glossary[word])

def Glossary2():
    glossary = {
        'string': 'A series of characters.',
        'comment': 'A note in a program that the Python interpreter ignores.',
        'list': 'A collection of items in a particular order.',
        'loop': 'Work through a collection of items, one at a time.',
        'dictionary': "A collection of key-value pairs.",
        'key': 'The first item in a key-value pair in a dictionary.',
        'value': 'An item associated with a key in a dictionary.',
        'conditional test': 'A comparison between two values.',
        'float': 'A numerical value with a decimal component.',
        'boolean expression': 'An expression that evaluates to True or False.',
    }

    for word, definition in glossary.items():
        print("\n" + word.title() + ": " + definition)

def Rivers():
    rivers = {
        'nile': 'egypt',
        'mississippi': 'united states',
        'fraser': 'canada',
        'kuskokwim': 'alaska',
        'yangtze': 'china',
    }

    for river, country in rivers.items():
        print("The " + river.title() + " flows through " + country.title() + ".")

    print("\nThe following rivers are included in this data set:")
    for river in rivers.keys():
        print("- " + river.title())

    print("\nThe following countries are included in this data set:")
    for country in rivers.values():
        print("- " + country.title())

def Polling():
    favorite_languages = {
        'anh': 'python',
        'an': 'c',
        'nam': 'ruby',
        'dang': 'python',
    }

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " +
              language.title() + ".")

    print("\n")

    coders = ['anh', 'thanh', 'quang', 'nam', 'dang', 'an', 'vu']
    for coder in coders:
        if coder in favorite_languages.keys():
            print("Thank you for taking the poll, " + coder.title() + "!")
        else:
            print(coder.title() + ", what's your favorite programming language?")


def People():
    people = []
    person = {
        'first_name': 'Quoc Thinh',
        'last_name': 'Hoang',
        'age': 21,
        'city': 'Ha Noi',
    }
    people.append(person)
    person = {
        'first_name': 'Van Anhk',
        'last_name': 'Pham',
        'age': 21,
        'city': 'Ha Noi',
    }
    people.append(person)
    person = {
        'first_name': 'nam',
        'last_name': 'tran van',
        'age': 21,
        'city': 'ho chi minh',
    }
    people.append(person)
    for person in people:
        name = person['first_name'].title() + " " + person['last_name'].title()
        age = str(person['age'])
        city = person['city'].title()
        print(name + ", of " + city + ", is " + age + " years old.")

def Pets():
    pets = []
    pet = {
        'loai dong vat': 'cho',
        'ten': 'husky',
        'chu so huu': 'anh'
    }
    pets.append(pet)
    pet = {
        'loai dong vat': 'meo',
        'ten': 'miu',
        'chu so huu': 'an'
    }
    pets.append(pet)
    pet = {
        'loai dong vat': 'meo',
        'ten': 'ti',
        'chu so huu': 'hanh'
    }
    pets.append(pet)
    for pet in pets:
        for key, value in pet.items():
            print("\t" + key + ": " + str(value))
        print()

def Favorite_Places():
    favorite_places = {
        'anh': ['Hà Nội', 'Thái Bình', 'ho chi minh'],
        'an': ['ha nam', 'nam dinh'],
        'nam': ['ninh binh', 'quang ninh', 'hai phong']
    }

    for name, places in favorite_places.items():
        print("\n" + name.title() + " likes the following places:")
        for place in places:
            print("- " + place.title())

def Favorite_Numbers():
    favorite_numbers = {
        'anh': [10, 15, 20],
        'nam': [20, 12, 4, 5, 6],
        'nguyen': [1, 2, 3, 4, 5],
        'thanh': [99, 100],
        'dang': [0, 1, 2],
    }

    for ten, dayso in favorite_numbers.items():
        print(f'{ten.title()} numbers:')
        for so in dayso:
            print(so)

def Cities():
    cities={
        'Hà Nội':{
            'Quốc gia': 'Việt Nam',
            'Dân số': '10m người',
            'Thông tin khác': 'thủ đô'
        },
        'Hồ Chí Minh':{
            'Quốc gia': 'Việt Nam',
            'Dân số': '10m người',
            'Thông tin khác': 'thành phố trực thuộc trung ương'
        },
        'da nang':{
            'Quốc gia': 'Việt Nam',
            'Dân số': '5m người',
            'Thông tin khác': 'thành phố trực thuộc trung ương'
        }
    }
    for key, value in cities.items():
        print(f'thông tin về thành phố{str(key).title()}:')
        for thongtink, thongtinv in value.items():
            print(thongtink, thongtinv)
        print()

def Extensions():
    string = "PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022! \n \
                Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT \n \
                voi muc ho tro 500000 dong/sinh vien PTIT."
    directory = {}
    line = ''
    list = re.findall('[a-z0-9]+', string)
    for i in list:
        if i not in directory:
            directory[i] = 1
        else:
            directory[i] = int(directory[i]) + 1
    ds = sorted(directory.items(), key=lambda x: (-x[1], x[0]))
    for i in ds:
        print(i[0], i[1])
if __name__=='__main__':
    dictionary = {
        1: Conditional_Tests,
        2: More_Conditionali_Tests,
        3: Alien_Colors_1,
        4: Alien_Colors_2,
        5: Alien_Colors_3,
        6: Stages_of_Life,
        7: Favorite_Fruit,
        8: Hello_Admin,
        9: No_User,
        10: Checking_Usernames,
        11: Ordinal_Numbers,
        12: Person,
        13: Favarite_Number,
        14: Glossary,
        15: Glossary2,
        16: Rivers,
        17: Polling,
        18: People,
        19: Pets,
        20: Favorite_Places,
        21: Favorite_Numbers,
        22: Cities,
        23: Extensions
    }
    while True:
        print("---------------------------MENU-----------------------")
        print("Num 1. Conditional_Tests")
        print("Num 2. More_Conditionali_Tests")
        print("Num 3. Alien_Colors_1")
        print("Num 4. Alien_Colors_2")
        print("Num 5. Alien_Colors_3")
        print("Num 6. Stages_of_Life")
        print("Num 7. Favorite_Fruit")
        print("Num 8. Hello_Admin")
        print("Num 9. No_User")
        print("Num 10. Checking_Usernames")
        print("Num 11. Ordinal_Numbers")
        print("Num 12. Person")
        print("Num 13. Favarite_Number")
        print("Num 14. Glossary")
        print("Num 15. Glossary2")
        print("Num 16. Rivers")
        print("Num 17. Polling")
        print("Num 18. People")
        print("Num 19. Pets")
        print("Num 20. Favorite_Places")
        print("Num 21. Favorite_Numbers")
        print("Num 22. Cities")
        print("Num 23. Extensions")
        print("Num 0. Dừng!")
        print("------------------------------------------------------")
        print("Choose a Number: ", end="")
        try:
            x = int(input())
            if x == 0:
                print("Bye!")
                break
            dictionary[x]()
        except Exception as e:
            print("Không có bài đó!")