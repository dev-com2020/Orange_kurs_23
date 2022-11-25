def multi(a, b):
    try:
        return int(a) * int(b)
    except TypeError as e:
        print("Źle dobrane parametry, zwracam 0")
        print("Wystąpił błąd:", e.args)
        return 0
    except ValueError as e:
        print("Źle dobrane parametry, zwracam 1")
        print("Wystąpił błąd:", e.args)
        return 1


def multi2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError) as e:
        print("Źle dobrane parametry, zwracam 0")
        print("Wystąpił błąd:", e.args)
        return 0


def multi3(a, b):
    try:
        return int(a) * int(b)
    except Exception as e:
        print("Źle dobrane parametry, zwracam 0")
        print("Wystąpił błąd:", e.args)
        return 0


# print(multi(4, 5))
# print(multi("4", 5))
# print(multi("4", "5"))
# print(multi("A", "b"))
# print("Kolejne czynności...")
# print(multi2("A", "b"))
# print(multi3("A", "b"))

valid_data = [{'name': 'Jan', 'age': '10'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]
invalid_data = [{'name': 'Jan', 'age': 'age'}, {'name': 'Dawid', 'age': '25'}, {'name': 'Marcin', 'age': '23'}]


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            user_age = int(user['age'])
        except KeyError:
            print('Niepoprawne dane: {}'.format(user))
        except ValueError:
            print('Niepoprawny wiek: {}'.format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("{} -> {}".format(i, user))
    return count


check_age(valid_data, 11)
check_age(invalid_data, 11)
