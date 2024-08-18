import matplotlib.pyplot as plt

# Sample data for illustration
feature_importance = ['Not Important', 'Slightly Important', 'Neutral', 'Important', 'Very Important']
feature_importance_counts = [2, 4, 8, 12, 14]

plt.figure(figsize=(10, 6))
plt.bar(feature_importance, feature_importance_counts, color='coral')
plt.xlabel('Feature Importance')
plt.ylabel('Number of Responses')
plt.title('Importance of Features in Academic Support Chatbot')
plt.savefig('feature_importance.png')
plt.show()

