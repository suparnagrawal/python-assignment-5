studentMarks = {'Alice':85,'Bob':28}
name = input('Enter student\'s name: ')
if name in studentMarks:
    print(name+'\'s marks:{}'.format(studentMarks[name]))
else:
    print('Student not found.')
