# 구구단 계산 프로그램
import time, random

def printAllTimeTable(time) :  # 주어진 숫자부터 9단까지 출력
    for start in range(time, 10) : 
        for multiply in range(10) : 
            print('%d x %d = %d' % (time, start, time*start))

def printTimeTable(time) :    # 주어진 숫자의 단만 출력
    for i in range(10) : 
        print('%d x %d = %d' % (time, i, time*i))

