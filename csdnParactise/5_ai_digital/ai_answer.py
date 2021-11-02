




if __name__ == '__main__':
    while (True):
        question = input()
        answer = question.replace('吗', '呢').replace('你','我').replace('我','你')
        answer = answer.replace('？', '！')
        print(answer)