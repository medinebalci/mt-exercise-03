import matplotlib.pyplot as plt

# training steps (every 500 steps)
steps = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# extracted validation perplexities
baseline_ppl = [44.81, 30.78, 26.38, 23.67, 21.99, 20.50, 19.33, 18.23, 17.22, 16.09]
prenorm_ppl = [41.52, 30.22, 27.01, 24.88, 23.59, 22.60, 21.74, 20.89, 20.52, 20.11]
postnorm_ppl = [45.33, 32.00, 28.50, 26.10, 24.40, 23.10, 22.00, 21.00, 20.30, 19.80] 

# create the plot
plt.figure(figsize=(10, 6))
plt.plot(steps, baseline_ppl, label='Baseline', color='blue', marker='o')
plt.plot(steps, prenorm_ppl, label='Pre-norm', color='green', marker='o')
plt.plot(steps, postnorm_ppl, label='Post-norm', color='red', marker='o')

# labels and title
plt.xlabel('Training Steps')
plt.ylabel('Validation Perplexity')
plt.title('Validation Perplexity over Training Steps')
plt.legend()
plt.grid(True)
plt.tight_layout()

# save or show the plot
plt.savefig('validation_perplexities.png')
plt.show()  
