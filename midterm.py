def prepareDataList(DAYS, HOURS):
    data = []
    for i in range(HOURS):
        data.append([])
        for j in range(DAYS):
            data[i].append([])
            data[i][j].append(0)
            data[i][j].append(0)
    return data

def readFile(weather, data):
    f = open("weather.txt", "r")
    lines = f.readlines()

    for line in lines:
        temp = line.strip().split()
        day = eval(temp[0])
        hour = eval(temp[1])
        t = eval(temp[2])
        h = eval(temp[3])
        data[hour-1][day-1][0] = t
        data[hour-1][day-1][1] = h
    return data

def compute(data):
    result = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(DAYS):
        sum_t = 0
        sum_h = 0
        for j in range(HOURS):
            sum_t += data[j][i][0]
            sum_h += data[j][i][1]
        result[0][i] = sum_t
        result[1][i] = sum_h
    return result

def printResult(data):
    for i in range(DAYS, 0, -1):
        print(str(format(i, "2d")) + "일의 평균온도는 " + str(format(data[0][i-1]/HOURS, ".5f")) + " 이고, 평균습도는 " + str(format(data[1][i-1]/HOURS, ".5f")) + " 입니다.")
    t = 0
    h = 0
    for i in range(DAYS):
        t += data[0][i]
        h += data[1][i]
    ave_t = t/(DAYS*HOURS)
    ave_h = h /(DAYS*HOURS)
    print("10일간의 평균온도 : ", format(ave_t, ".15f"))
    print("10일간의 평균습도 : ", format(ave_h, ".15f"))

##------- main ----------##
DAYS = 10
HOURS = 24
data = prepareDataList(DAYS, HOURS)
printResult(compute(readFile("weather.txt", data)))