

import sys

EventCount = 0

def DiceCount(CountValue, Level, CountTemp):

    if Level == 0:
        if CountValue == CountTemp:
            global EventCount
            EventCount += 1
        return None

    if CountTemp >= CountValue:
        return None
    
    MaxDistance = 6 * Level
    if CountValue - CountTemp > MaxDistance:
        return None

    for i in reversed(range(1, 7)):
        if CountValue - (CountTemp + i) > MaxDistance:
            break
        if CountTemp + i > CountValue:
            continue
        DiceCount(CountValue, Level - 1, CountTemp + i)
    return None

if len(sys.argv) != 2:
    print('Error!')
    print('> DiceProbabilityCalculator.py 3')
    sys.exit()
try:
    Dice = int(sys.argv[1])
except ValueError:
    print('Error!')
    print('> DiceProbabilityCalculator.py 3')
    sys.exit()

if Dice < 1:
    print('Error!')
    print('Please input positive integer')
    sys.exit()

MaxValue = 6 * Dice
MinValue = 1 * Dice
TotalEvent = 6 ** Dice
print('Total dice:', Dice)
print('Max value:', MaxValue)
print('Min value:', MinValue)
print('Total event:', TotalEvent)

# for CountValue in range(MinValue, MaxValue + 1):
    
#     EventCount = 0
#     DiceCount(CountValue, Dice, 0)
        
#     print('Total number:', CountValue , 'Event count:', EventCount, 'Probability:', EventCount * 100 / TotalEvent, '%')

AnswerList = []
Changed = False
for CountValue in range(MinValue, MaxValue + 1):
    
    if CountValue < (MinValue + MaxValue + 1) / 2:
        EventCount = 0
        DiceCount(CountValue, Dice, 0)
        AnswerList.append(EventCount)    
    else:
        if not Changed:
            Changed = True
            if Dice % 2 == 0:
                AnswerList.pop()
        EventCount = AnswerList.pop()

    print('Total number:', CountValue , 'Event count:', EventCount, 'Probability:', EventCount * 100 / TotalEvent, '%')


