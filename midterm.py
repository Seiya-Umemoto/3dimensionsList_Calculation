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
        data[hour-1][day-1][0] = t #인덱스 i가 시간-1, j가 날짜-1, 첫번째 온도
        data[hour-1][day-1][1] = h #두번째 습도
    return data

def compute(data):
    result = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # for i in range(len(result)):
    #     for j in range(HOURS*DAYS):
    #         sum_t = 0
    #         sum_h = 0
    #         sum_t += data[len(data[j])][i][0]
    #         sum_h += data[len(data[j])][i][1]
    #         result[0] = sum_t
    #         result[1] = sum_h
    for i in range(len(data[0])):
        sum_t = 0
        sum_h = 0
        for j in range(len(data)):
            sum_t += data[j][i][0]
            sum_h += data[j][i][1]
        result[0][i] = sum_t
        result[1][i] = sum_h
    return result

def printResult(result):
    for i in range(DAYS, 0, -1):
        print(str(format(i, "2d")) + "일의 평균온도는 " + str(format(result[0][i-1]/len(data), ".5f")) + " 이고, 평균습도는 " + str(format(result[1][i-1]/len(data), ".5f")) + " 입니다.")
    t = 0
    h = 0
    for i in result:
        if t == 0 and h == 0: t = sum(i)
        else: h = sum(i)
    print(t)
    print(h)
    ave_t = t/(len(data)*len(data[0]))
    ave_h = h /(len(data) * len(data[0]))
    print("10일간의 평균온도 : ", format(ave_t, ".15f"))
    print("10일간의 평균습도 : ", format(ave_h, ".15f"))

'''  "2d" 는 앞에 공백주는 역할

def printResult(data):

    for i in range(DAYS, 0, -1):        

        print(str(format(i, "2d")) + "일의 평균온도는 " + str(format(results[0]),".6f") + " 이고, 평균습도는 " + str(format(results[1]),".6f") + " 입니다.")

    t = 0

    h = 0

    for i in range(DAYS):

        t += results[0][i]

        h += results[1][i]

    ave_t = t/len(DAYS)

    ave_h = h/len(DAYS)

    print("10일간의 평균온도 : ", format(ave_t,".15f"))

    print("10일간의 평균습도 : ", format(ave_h,".15f"))

'''

##------- main ----------##    

DAYS = 10
HOURS = 24
data = prepareDataList(DAYS, HOURS)
printResult(compute(readFile("weather.txt", data)))
