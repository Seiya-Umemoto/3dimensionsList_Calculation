#
# 실습과제
# 학번 : 
# 이름 : 
#
def prepareDataList(DAYS, HOURS):
  data =[]
  for i in range(HOURS):
      data.append([])
      for j in range(DAYS):
          data[i].append([])
          data[i][j].append(0)
          data[i][j].append(0)
  return data

def readFile(fileName, data):   
    f = open(fileName, "r")
    lines = f.readlines()

    for line in lines:
        temp = line.strip().split()
        day = eval(temp[0])
        hour = ______________________
        t = __________________
        h = __________________
        data[________][_________][_________] = t
        data[________][_________][_________] = h
    return data

def compute(data):
    result = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    
    
    
    
    
    
    
    
    
    return result

def printResult(data):
    for i in ______________________________:        
        print(str(format(i, "2d")) + "일의 평균온도는 "
              + ________________________________ + " 이고, 평균습도는 "
              + ________________________________ + " 입니다.")
    t = 0
    h = 0
    for i in ___________________________:
        ___________________________
        ___________________________
    ave_t = ____________________________
    ave_h = ____________________________
    print("10일간의 평균온도 : " ___________________)
    print("10일간의 평균습도 : " ___________________)    
    
##------- main ----------##    
DAYS = 10
HOURS = 24    
data = prepareDataList(DAYS, HOURS)
printResult(compute(readFile("weather.txt", data)))    