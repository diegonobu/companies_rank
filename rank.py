import sys

from company import Company


def collect_data(f):
    lines = []
    with open(f) as file:
        lines = file.readlines()
    return Company(lines[0].strip(), lines[1:])


def percentage(qtd, total):
    return int((100 * qtd) / total)


def percentage_results(item):
    fav = percentage(item['fav'], item['total'])
    neutral = percentage(item['neutral'], item['total'])
    unfav = percentage(item['unfav'], item['total'])
    return fav, neutral, unfav


def organize_values(data):
    result = {}
    for id, answer in data:
        if id not in result:
            result[id] = {'fav': 0, 'neutral': 0, 'unfav': 0, 'total': 0}
        if answer == 0 or answer == 1:
            result[id]['fav'] += 1
        elif answer == 2:
            result[id]['neutral'] += 1
        else:
            result[id]['unfav'] += 1
        result[id]['total'] += 1
    return result


if __name__ == '__main__':

    data = []
    for path in sys.argv[1:]:
        data.append(collect_data(path))

    print('Summary by companies:\n')

    for company in data:
        print(company.name)

        clean_data = company.clean_data()
        result = organize_values(clean_data)

        for key, item in result.items():
            fav, neutral, unfav = percentage_results(item)
            print('{}: {}% fav, {}% neutral, {}% unfav'.format(key, fav, neutral, unfav))

        print('')
