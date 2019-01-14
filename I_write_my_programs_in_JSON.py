import json


def get_numbers(data, numbers):
    try:
        for k, v in data.items():
            if type(v) == dict or type(v) == list:
                get_numbers(v, numbers)
            elif type(v) == int:
                numbers.append(v)
    except AttributeError:
        for v in data:
            if type(v) == list or type(v) == dict:
                get_numbers(v, numbers)
            elif type(v) == int:
                numbers.append(v)
    return numbers

def main():
    file = open('skychallenge_accounting_input.json', 'r')
    data = json.load(file)
    numbers = []
    numbers_sum = sum(get_numbers(data, numbers))
    print(numbers_sum)
    return numbers_sum

if __name__ == '__main__':
    main()
