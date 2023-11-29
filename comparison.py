import matplotlib.pyplot as plt

# Hardcoded latest accuracies for each method
neural_network_accuracies = [34.95, 43.25, 52.48, 61.89, 72.39, 80.39, 85.12, 88.39, 90.62, 92.15]
based_rule_accuracies = [14.55, 21.60, 26.35, 32.75, 35.05, 38.00, 39.25, 39.85, 41.55, 43.15]
deep_learning_accuracies = [33.11, 33.19, 33.60, 33.88, 34.96, 57.36, 74.30, 81.57, 89.60, 93.69]

# Epochs
epochs = range(1, 11)

# Plotting the accuracies
plt.figure(figsize=(10, 6))
plt.plot(epochs, neural_network_accuracies, label='Neural Network', marker='o')
plt.plot(epochs, based_rule_accuracies, label='Based-Rule', marker='s')
plt.plot(epochs, deep_learning_accuracies, label='Deep Learning', marker='^')

plt.title('Comparison of Model Accuracies over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy (%)')
plt.xticks(epochs)

plt.legend()
plt.show()
