def displayGrades():
    print()

def averageScore(scores):
    sum = 0
    for i in scores:
        sum += i

    return sum / len(scores)

def getGrades(file):
    return file