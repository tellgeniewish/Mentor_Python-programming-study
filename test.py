class Student:
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score

    def get_total(self):
        return self.mid_score + self.final_score

    def check_pass(self):
        total = self.get_total()
        if 160 <= total:
            result = "합격"
        else: result = "불합격"
        print("학생: %s, 총점: %d, 결과: %s" % (self.name, total, result))

st1 = Student("genie", 90, 80)
st2 = Student("alex", 80, 70)

st1.check_pass()
st2.check_pass()