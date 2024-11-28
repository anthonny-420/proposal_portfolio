students_notes = {
    'ramiro vargas': [3.4, 4.5, 4.0, 5.0, 4.7],
    'pibe valderrama': [4.4, 3.2, 2.8, 4.0, 5.0],
    'james rodriguez': [5.0, 4.5, 2.9, 3.0, 1.1],
    'arturo vidal': [3.0, 2.9, 4.5, 3.7, 4.9],
    'juan quintero': [4.5, 4.0, 5.0, 4.3, 5.0],
}
print('luis caicedo' in students_notes)
print(list(students_notes.keys()))
print(list(students_notes.values()))
print(students_notes.get('ramiro vargas'))
print(students_notes['pibe valderrama'])
students_notes['arturo vidal'].append(1.1)
students_notes.update({'daniel muñoz': [4.3, 4.2, 4.7, 5.0, 5.0]})
del students_notes['ramiro vargas']
index = students_notes['pibe valderrama'].index(4.0)
new_index = students_notes['pibe valderrama'][:]
new_index[index] = 2.0

print(new_index)
