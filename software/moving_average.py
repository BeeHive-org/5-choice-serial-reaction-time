#make a  moving average in micropython

winSize = 20
trials = 100

data = [0]*winSize
winIndex = 0
for trial in range(trials):
    accuracy = 10
    data[winIndex] = accuracy
    winIndex = winIndex+1
    if winIndex ==winSize:
        winIndex = 0
    if trial < winSize:
        avg = sum(data[0:trial])/trial
    else:
        avg = sum(data)/winSize


