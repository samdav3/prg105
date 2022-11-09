

class Question:
    def __init__(self, question, ans_1, ans_2, ans_3, ans_4, correct):
        self.__question = question
        self.__answer1 = ans_1
        self.__answer2 = ans_2
        self.__answer3 = ans_3
        self.__answer4 = ans_4
        self.__correct = correct

    def set_question(self, question):
        self.__question = question

    def set_answer1(self, ans_1):
        self.__answer1 = ans_1

    def set_answer2(self, ans_2):
        self.__answer2 = ans_2

    def set_answer3(self, ans_3):
        self.__answer3 = ans_3

    def set_answer4(self, ans_4):
        self.__answer4 = ans_4

    def set_correct(self, correct):
        self.__correct = correct

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct(self):
        return self.__correct


def main():

    q1 = Question('What is the name of the tallest mountain in the world?', 'A. Mount Olympus', 'B. K2',
                  'C. Nanga Parbat', 'D. Mount Everest', "D")
    q2 = Question('Which country has the largest population in the world?', 'A. Russia', 'B. United States',
                  'C. China', 'D. Australia', "C")
    q3 = Question('What is the name of the longest river in Africa?', 'A. The Nile River', 'B. Congo River',
                  'C. Niger River', 'D. Zambezi River', "A")
    q4 = Question('What American city is the Golden Gate Bridge located in?', 'A. New York City', 'B. San Francisco',
                  'C. Chicago', 'D. Miami', "B")
    q5 = Question('What is the capital of Mexico?', 'A. Oaxaca', 'B. Merida', 'C. Mexico City', 'D. Cancun',
                  "C")
    q6 = Question('What is the name of the largest country in the world?', 'A. China', 'B. Australia', 'C. United Stated',
                  'D. Russia', "D")
    q7 = Question('What U.S. state is home to no poisonous snakes?', 'A. Washington', 'B. Alaska', 'C. Maine',
                  'D. Idaho', "B")
    q8 = Question('What is the capital of Canada?', 'A. Ottawa', 'B. Toronto', 'C. Montreal', 'D. Quebec City',
                  "A")
    q9 = Question('What is the name of the largest ocean in the world?', 'A. Atlantic Ocean', 'B. Indian Ocean',
                  'C. Arctic Ocean', 'D. Pacific Ocean', "D")
    q10 = Question('What country are the Great Pyramids of Giza located in?', 'A. Libya', 'B. Egypt', 'C. Sudan',
                   'D. Chad', "B")
    player1 = 0
    player2 = 0
    set_1 = [q1, q2, q3, q4, q5]
    set_2 = [q6, q7, q8, q9, q10]

    print('Player 1: ')
    for query in set_1:
        print('\n')
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input('Please enter the letter of the correct answer: ')
        if guess.upper() == query.get_correct():
            print('That is the correct answer!')
            player1 += 1
        else:
            print(f'That is incorrect, the letter of the correct answer is {query.get_correct()}.')
    print('\n')
    print(f'Player 1 earned {str(player1)} points!')

    print('\n\n')
    print('Player 2: ')
    for query in set_2:
        print('\n')
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input('Please enter the letter of the correct answer: ')
        if guess.upper() == query.get_correct():
            print('That is the correct answer!')
            player2 += 1
        else:
            print(f'That is Incorrect, the letter of the correct answer is {query.get_correct()}.')
    print('\n')
    print(f'Player 2 earned {str(player2)} points!')


main()
