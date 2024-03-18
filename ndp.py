import itertools

def get_binary_number(number):
    return bin(number)[2:].zfill(3)

def append_to_negative_db(negative_db, number):
    binary = bin(number)[2:].zfill(3)
    negative_db.append(binary)

def calc_all_ndb(negative_db):
    result = []
    count = 0
    for nat in negative_db:
        value = int(nat, 2)
        if value != count:
            append_to_negative_db(result, value)
        count += 1
    return result

def calc_all_boolean(input):
    results = []
    generate_expressions(input, 0, [''] * len(input), results)
    return results

def generate_expressions(input, index, current_expr, results):
    if index == len(input):
        results.append(''.join(current_expr))
        return

    if input[index] == '*':
        current_expr[index] = '0'
        generate_expressions(input, index + 1, current_expr, results)
        current_expr[index] = '1'
        generate_expressions(input, index + 1, current_expr, results)
    else:
        current_expr[index] = input[index]
        generate_expressions(input, index + 1, current_expr, results)

def is_found_in_negative_db(input, negative_db):
    return input in negative_db

def compress2(str1, str2):
    result = []
    counter = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            counter += 1
            result.append(str1[i])
        else:
            result.append('*')

    if counter >= 2:
        return ''.join(result)
    else:
        return None

def compress(data):
    results = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            resstr = compress2(data[i], data[j])
            if resstr is None:
                continue
            if not any(e == resstr for e in results):
                results.append(resstr)

    ignored_exists = False
    for i in range(len(data)):
        for j in range(len(results)):
            if data[i] != results[j]:
                ignored_exists = True
            else:
                ignored_exists = False
                break
        if ignored_exists:
            results.append(data[i])
            ignored_exists = False

    return results

negative_db = ['***']

while True:
    print("Hi User You Can Choose One Of this Process To Test DataBase :")
    print("*************************************************************\n")
    option = input("1)Insert\n2)Search For Item In NDB\n3)To Retrieve all NDB\n")

    if option == "1":
        existing_negative_database = []
        decimal_value = input("Enter Your Number From 0 to 7 To store In DataBase : ")
        try:
            decimal_value = int(decimal_value)
            if decimal_value < 0 or decimal_value > 7:
                print("Please Enter Number From 0 To 7...\n")
                continue
        except ValueError:
            print("Please Enter a Valid Integer...\n")
            continue

        value = get_binary_number(decimal_value)
        for item in negative_db:
            values = calc_all_boolean(item)
            existing_negative_database.extend(values)
        existing_negative_database2 = [item for item in existing_negative_database if item != value]
        negative_db = compress(existing_negative_database2)
        print("Status Code : 200")

    elif option == "2":
        existing_negative_database = []
        decimal_value = input("Enter Your Search Number To Search on Negative DataBase : ")
        try:
            decimal_value = int(decimal_value)
        except ValueError:
            print("Please Enter a Valid Integer...\n")
            continue

        value = get_binary_number(decimal_value)
        for item in negative_db:
            values = calc_all_boolean(item)
            existing_negative_database.extend(values)
        if value in existing_negative_database:
            print("Your Data Exists in Negative DataBase")
        else:
            print("Sorry, Your Data Is not in NDB\n")
            print("***************************************\n")

    elif option == "3":
        if not negative_db:
            print("Your NDB is Empty...")
        else:
            for item in negative_db:
                print(item)

    else:
        print("please choose correct option...\n")
