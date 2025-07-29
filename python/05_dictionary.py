marks = {'Hindi': 80, 'English': 90, 'sanskirit': 70}

print(type(marks))
print(marks['English'])

makrs = {
'Hindi': 80,
'English': 90,
'Science': 70
}

print(makrs['Hindi'])

print(marks.get('sanskirit'))

marks['Maths'] = 100

print(marks)
print(marks.get('Maths'))

del makrs['Science']
print(makrs)
