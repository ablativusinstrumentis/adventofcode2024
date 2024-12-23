file = open("input.txt","r").readlines()
## this code is too long but do i care i was tired
reports = [[int(j) for j in file[i].split()] for i in range(len(file))]

def areyousurebro(report):
    for i in range(len(report)):
        newreport = [report[j] for j in range(len(report)) if j!=i]
        if areyousafe(newreport):
            return True
    return False

def areyousafe(report):
    if report[0]<report[1]:
        for i in range(1,len(report)):
            if report[i]-report[i-1]>3 or report[i]-report[i-1]<1:
                return False
    else:
        for i in range(1,len(report)):
            if report[i]-report[i-1]<(-3) or report[i]-report[i-1]>(-1):
                return False
    return True

def safe(report):
    if report[0]<report[1]:
        for i in range(1,len(report)):
            if report[i]-report[i-1]>3 or report[i]-report[i-1]<1:
                return areyousurebro(report)
    else:
        for i in range(1,len(report)):
            if report[i]-report[i-1]<(-3) or report[i]-report[i-1]>(-1):
                return areyousurebro(report)
    return True
    
savesss = 0
for i in range(len(reports)):
    if safe(reports[i]):
        savesss+=1
print(savesss)
