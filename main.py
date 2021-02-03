import numpy
import cv2 as cv
import math
import keyboard as kb

#
#   TODO
#       GUI TO FIGURE OUT WHICH BUTTON IS WHERE

cap = cv.VideoCapture('videoplayback.mp4')
width = cap.get(3)
height = cap.get(4)
start_pos = []
end_pos = []
quadrants = numpy.array(([1, 1], [2, 1], [3, 1],
                         [1, 2], [2, 2], [3, 2],
                         [1, 3], [2, 3], [3, 3]))
currentframe = 0
keys = numpy.array(('l', 'w', 'k', 'a', 's', 'd', 'l', 'enter', 'k'))
lower_green = numpy.array([50, 110, 50])
upper_green = numpy.array([130, 255, 255])


def getquadrantsstart():
    for i in range(0, 3):
        xpos = math.ceil(width / 3 * i)
        for j in range(0, 3):
            ypos = math.ceil(height / 3 * j)
            temppos = [xpos, ypos]
            start_pos.append(temppos)
    return start_pos


def getquadrantsend():
    for i in range(0, 3):
        xpos = math.ceil(width / 3 * (i + 1))
        for j in range(0, 3):
            ypos = math.ceil(height / 3 * (j + 1))
            temppos = [xpos, ypos]
            end_pos.append(temppos)
    return end_pos


def drawquads():
    for j in range(0, 9):
        cv.rectangle(frame, tuple(start_pos[j]), tuple(end_pos[j]), (255, 0, 0), 5)


getquadrantsstart()
getquadrantsend()


def fishgaming():
    if cv.countNonZero(mask) > 0:
        pixlist = numpy.array(cv.findNonZero(mask))

        fishpos = numpy.squeeze((pixlist.mean(axis=0)).astype(int), axis=0)
        cv.circle(frame, tuple(fishpos), 20, (0, 255, 0), -1)

        # print("fishpos",fishpos)

        fishquad = numpy.array((math.ceil(fishpos[0] / width * 3), math.ceil(fishpos[1] / height * 3)))

        fishindex = 8
        # print("fishquad: ", fishQuad)
        for i in range(0, 8):
            if fishquad[0] == quadrants[i][0]:
                if fishquad[1] == quadrants[i][1]:
                    fishindex = i

        if currentframe % 30 == 0:
            print(keys[fishindex])
            kb.send(keys[fishindex])

        if currentframe % 300 == 0:
            numpy.random.shuffle(keys)
            print(keys)


def quadguis():
    for i in range(0, 9):
        textpos = tuple((quadrants[i][0]*213-203, quadrants[i][1]*120))
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, keys[i], textpos, font, 1, (255, 255, 255))


while cap.isOpened():
    ret, frame = cap.read()
    hsvVid = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    mask = cv.inRange(hsvVid, lower_green, upper_green)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    currentframe += 1
    drawquads()
    fishgaming()
    quadguis()
    cv.imshow('hsv', hsvVid)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
