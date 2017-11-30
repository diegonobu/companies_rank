class Company:
    def __init__(self, name, data=[]):
        self.name = name
        self.data = data

    def clean_data(self):
        result = []
        for line in self.data:
            question_id, answer = line.strip().split()
            if verify_valid_answer(int(answer)):
                result.append((question_id, int(answer)))
        return result


def verify_valid_answer(answer):
    return 0 <= answer < 5