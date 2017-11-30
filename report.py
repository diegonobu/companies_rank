class Report:
    def __init__(self, companies=None):
        if companies is None:
            companies = []
        self.companies = clean_data(companies)
        self.summary = {}
        self.valid_answer = {}

    def summary_by_companies(self):
        for company in self.companies:
            if company.name not in self.summary:
                self.summary[company.name] = {}
            result = organize_values(company.data)
            for key, item in result.items():
                fav, neutral, unfav = percentage_results(item)
                self.summary[company.name][key] = {
                    'fav': fav, 'neutral': neutral, 'unfav': unfav
                }
        return self.summary

    def show_summary_by_companies(self):
        if not self.summary:
            self.summary_by_companies()
        for company, data in self.summary.items():
            print('\n{}'.format(company))
            for key, item in data.items():
                print('{}: {}% fav, {}% neutral, {}% unfav'
                      .format(key, item['fav'], item['neutral'], item['unfav']))

    # def fav_answer_by_question(self):
    #     if not self.summary:
    #         self.summary_by_companies()
    #     result =
    #     for company, data in self.summary.items():
    #         for key, item in data.items():
    #             result.append()

    def show_valid_answers(self):
        for company in self.companies:
            print('{}: {}'.format(company.name, len(company.data)))

    def show_invalid_answers(self):
        for company in self.companies:
            print('{}: {}'.format(company.name, company.invalid_answers))


def clean_data(data):
    for company in data:
        company.data, company.invalid_answers = company.clean_data()
    return data


def is_fav(answer):
    return answer == 0 or answer == 1


def is_unfav(answer):
    return answer == 3 or answer == 4


def organize_values(data):
    result = {}
    for id, answer in data:
        if id not in result:
            result[id] = {'fav': 0, 'neutral': 0, 'unfav': 0, 'total': 0}
        if is_fav(answer):
            result[id]['fav'] += 1
        elif is_unfav(answer):
            result[id]['unfav'] += 1
        else:
            result[id]['neutral'] += 1
        result[id]['total'] += 1
    return result


def percentage(qtd, total):
    return int((100 * qtd) / total)


def percentage_results(item):
    fav = percentage(item['fav'], item['total'])
    neutral = percentage(item['neutral'], item['total'])
    unfav = percentage(item['unfav'], item['total'])
    return fav, neutral, unfav
