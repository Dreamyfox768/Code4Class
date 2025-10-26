class Grade:
    def __init__(self):
        self.grade_component = ''
        self.percentage = ''
        self.sum_total = ''
        self.level = ''
        self.ask = ''
        self.num_components = ''

    def grade_calculator(self):
        self.ask = input("Do you wish to proceed? (Y/N): ")
        while self.ask == 'Y' or self.ask == 'y':
            self.level = int(input("How many components is the grading divided into: "))
            self.sum_total = 0
            self.num_components = 0
            while 0 < self.level:
                self.num_components += 1
                self.grade_component = int(input(f"Enter grade number {self.num_components}: "))
                self.percentage = int(input("Enter percentage: "))
                math = (self.grade_component * self.percentage) / 100
                self.sum_total += math
                self.level -= 1
            self.ask = input("Do you wish to proceed? (Y/N): ")

    def __str__(self):
        return f'Your final grade is: {str(self.sum_total)}'


def main():
    grade1 = Grade()
    grade1.grade_calculator()
    print(grade1)


if __name__ == '__main__':
    main()
