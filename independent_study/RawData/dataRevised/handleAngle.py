import re
data = open('E:\CS799\RawData\dataRevised\MPU9250RawData_3.dat','r')
dataline = data.readlines()
qarternion = []
tmpqart = []
for i in range(len(dataline)):
    line = dataline[i]
    sear = re.search('Yaw, Pitch, Roll: (.+), (.+), (.+)', line)
    if sear != None:
        for i in range(3):
            tmpqart.append(sear.groups()[i])
        qarternion.append(tmpqart)
    tmpqart = []
data.close()


with open('E:\CS799\RawData\dataRevised\oriEulerAngle.dat', 'w') as wrFile:
    for j in range(len(qarternion)):
        outline = qarternion[j]
        for num in outline:
            wrFile.write(num)
            wrFile.write(' ')
        wrFile.write('\r')
        print('Line %s is processd' % str(j))
