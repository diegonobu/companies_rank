class Company:
    def __init__(self, name, data=None):
        if data is None:
            data = []
        self.name = name
        self.data = data
        self.invalid_answers = 0

    def clean_data(self):
        result = []
        invalid_answers = 0
        for line in self.data:
            question_id, answer = line.strip().split()
            if verify_valid_answer(int(answer)):
                result.append((question_id, int(answer)))
            else:
                invalid_answers += 1
        return result, invalid_answers


def verify_valid_answer(answer):
    return 0 <= answer < 5


def collect_from_file(f):
    with open(f) as file:
        lines = file.readlines()
    data = [i.strip() for i in lines[1:]]
    return Company(lines[0].strip(), data)
