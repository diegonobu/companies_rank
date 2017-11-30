class Report:
    def __init__(self, companies=[]):
        self.companies = clean_data(companies)

    def summary_by_companies(self):
        for company in self.companies:
            print(company.name)
            result = organize_values(company.data)
            for key, item in result.items():
                fav, neutral, unfav = percentage_results(item)
                print('{}: {}% fav, {}% neutral, {}% unfav'.format(key, fav, neutral, unfav))

            print('')


def clean_data(data):
    for company in data:
        company.data = company.clean_data()
    return data


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


def percentage(qtd, total):
    return int((100 * qtd) / total)


def percentage_results(item):
    fav = percentage(item['fav'], item['total'])
    neutral = percentage(item['neutral'], item['total'])
    unfav = percentage(item['unfav'], item['total'])
    return fav, neutral, unfav


def fav_answer_by_question(data):
    pass
