import sys

import report
from company import collect_from_file

if __name__ == '__main__':

    data = []
    for path in sys.argv[1:]:
        data.append(collect_from_file(path))

    report.clean_data(data)

    print('Summary by companies:\n')

    report.summary_by_companies(data)

    print('Fav answers by questions:')

    report.fav_answer_by_question(data)
