print('Welocme to my computer quiz')

playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()

print('Okay lets play :)')
score = 0

answer = input('What does the cpu stand for? ')
if answer == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does the gpu stand for? ')
if answer == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does the ram stand for? ')
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does the psu stand for? ')
if answer == 'power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print('You got ' + str(score) + ' questions correct')
print('You got ' + str(score/4*100) + '%.')


