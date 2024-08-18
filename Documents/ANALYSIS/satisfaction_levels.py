import matplotlib.pyplot as plt

# Sample data for illustration
satisfaction_levels = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied']
satisfaction_counts = [5, 8, 11, 3, 2]

plt.figure(figsize=(10, 6))
plt.bar(satisfaction_levels, satisfaction_counts, color='skyblue')
plt.xlabel('Satisfaction Level')
plt.ylabel('Number of Responses')
plt.title('Student Satisfaction with Current Academic Support')
plt.savefig('satisfaction_levels.png')
plt.show()

