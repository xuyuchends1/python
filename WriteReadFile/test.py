import os
import random


def getState():
    list = {}
    with open("unit.txt") as fs:
        for line in fs:
            l = line.split(',')
            list[l[0].strip()] = l[1].strip()
    return list


capitals = getState()

for quizNum in range(35):
    try:
        # create the quiz and answer key files
        quizFile = open('capitalquiz%s.txt' % (quizNum + 1), 'w')
        answerFile = open('capitalquiz_answer%s.txt' % (quizNum + 1), 'w')

        # TODO: write out the header
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(' '*20+ 'State capitals Quiz(Form %s)'%(quizNum+1))
        quizFile.write('\n\n')
        state=list(capitals.keys())
        random.shuffle(state)

        # todo: shuffle the order the state
        for quesionNum in range(50):
            answer_key=state[quesionNum]
            answer_value=capitals[state[quesionNum]]
            wrong_answer=list(capitals.values())
            del wrong_answer[wrong_answer.index(answer_value)]
            wrong_answer =random.sample(wrong_answer,3)
            answer_option=wrong_answer+[answer_value]
            random.shuffle(answer_option)
            quizFile.write('%s. the question is the captioal of %s?\n'%((quesionNum+1),answer_key))
            for i in range(4):
                quizFile.write('%s. %s\n' %('ABCD'[i],answer_option[i]))
            quizFile.write('\n')
            answerFile.write('%s. %s\n'%((quesionNum+1),'ABCD'[answer_option.index(answer_value)]))
    except:
        raise Exception
    finally:
        # todo: loop the 50 state ,make a question for each
        quizFile.close()
        answerFile.close()
    pass
