import sys

from company import collect_from_file
from report import Report

if __name__ == '__main__':

    data = []
    for path in sys.argv[1:]:
        data.append(collect_from_file(path))

    report = Report(data)

    print('Summary by companies:\n')

    report.show_summary_by_companies()

    # print('Fav answers by questions:')
    #
    # report.fav_answer_by_question()
