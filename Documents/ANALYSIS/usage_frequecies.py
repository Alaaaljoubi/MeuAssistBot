import matplotlib.pyplot as plt

# Sample data for illustration
usage_frequencies = ['Daily', 'Weekly', 'Monthly']
usage_counts = [10, 20, 5]

plt.figure(figsize=(10, 6))
plt.bar(usage_frequencies, usage_counts, color='lightgreen')
plt.xlabel('Usage Frequency')
plt.ylabel('Number of Responses')
plt.title('Frequency of Academic Support Usage')
plt.savefig('usage_frequencies.png')
plt.show()

