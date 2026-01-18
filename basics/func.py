def hello_func(name):
    print("hello world")
    profile = {
        'name' : 'parth chauhan',
        'age' : 23,
        'email' : '09parthchauhan'
    }

    for keys, values in profile.items():
        print(f'{keys} : {values}')

    return f"hello {name}"
print(hello_func('parth').upper())

