students = {"rahul":85,"amit":92,"priya":78,"sneha":95}
sorted_students = sorted(students.items(), key=lambda x:x[1],reverse=True)
print("top students:")
for name,marks in sorted_students[:2]:print(name, marks)
