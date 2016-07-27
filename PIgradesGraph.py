import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np

# Change default matplotlib style
plt.style.use("ggplot")

print(round(18.5))

def gradeConverter (grade):
	try:
		return round(float(grade))
	except Exception as e:
		return float(-1)

# Load grades
grades = np.loadtxt('grades.txt', converters = {0: gradeConverter})

# Convert grades to list (we need to delete a few elements and numpy arrays are fixed size)
grades = grades.tolist()

possibleGrades = list(range(0, 21))
ocurrences = [0] * 21

for index, value in enumerate(grades):
	# Remove D's (students that missed the test, value was converted to -1 by gradeConverter)
	if value == -1:
		del grades[index]

	# Create array of ocurrences
	else:
		ocurrences[int(value)] += 1

print('Notas possíveis/ocorrências:')
print(possibleGrades)
print(ocurrences)

plt.xlim(-1, 21)
plt.xticks(list(range(0, 21)))

plt.bar(possibleGrades, ocurrences, align = 'center')

plt.xlabel('Nota (arredondada ao inteiro mais próximo)', labelpad = 10)
plt.ylabel('Ocorrências', labelpad = 10)
title = plt.title('Distribuição das notas do 2º teste de PI')
title.set_y(1.05)

plt.show()
