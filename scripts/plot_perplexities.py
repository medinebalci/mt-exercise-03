import matplotlib.pyplot as plt

# training steps (every 500 steps)
steps = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500, 21000, 21500, 22000, 22500, 23000, 23500, 24000, 24500, 25000, 25500, 26000, 26500, 27000, 27500, 28000, 28500, 29000, 29500, 30000, 30500, 31000, 31500, 32000, 32500, 33000, 33500, 34000, 34500, 35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000, 39500, 40000, 40500]
# extracted validation perplexities
baseline_ppl = [56.61, 49.93, 45.33, 35.25, 28.44, 25.79, 23.77, 22.40, 21.26, 19.87, 18.80, 17.61, 16.55, 15.42, 14.26, 13.30, 12.62, 12.25, 11.83, 11.48, 11.19, 10.82, 10.69, 10.58, 10.41, 10.24, 10.05, 9.97, 9.84, 9.75, 9.60, 9.41, 9.42, 9.41, 9.30, 9.22, 9.25, 9.12, 8.97, 8.92, 8.92, 8.95, 8.92, 8.86, 8.81, 8.75, 8.70, 8.66, 8.59, 8.68, 8.63, 8.57, 8.65, 8.55, 8.53, 8.42, 8.41, 8.38, 8.44, 8.44, 8.39, 8.34, 8.39, 8.23, 8.19, 8.33, 8.33, 8.33, 8.27, 8.24, 8.20, 8.12, 8.11, 8.25, 8.27, 8.13, 8.23, 8.10, 8.11, 8.15, 8.01]
prenorm_ppl = [44.81, 30.78, 26.38, 23.67, 21.99, 20.50, 19.33, 18.23, 17.22, 16.09, 14.81, 13.59, 12.86, 12.25, 11.65, 11.37, 11.08, 10.89, 10.71, 10.61, 10.38, 10.26, 9.96, 9.87, 9.78, 9.68, 9.51, 9.49, 9.26, 9.23, 9.22, 9.02, 9.06, 8.95, 8.91, 8.88, 8.88, 8.87, 8.66, 8.60, 8.59, 8.62, 8.57, 8.50, 8.55, 8.47, 8.40, 8.34, 8.28, 8.32, 8.34, 8.22, 8.28, 8.28, 8.22, 8.17, 8.12, 8.17, 8.22, 8.13, 8.14, 8.09, 8.01, 8.01, 8.00, 8.01, 8.10, 8.05, 8.06, 7.99, 7.96, 7.92, 7.86, 7.93, 7.91, 7.87, 7.88, 7.91, 7.88, 7.87, 7.87]
postnorm_ppl = [41.52, 30.22, 27.01, 24.88, 23.59, 22.60, 21.74, 20.89, 20.52, 20.11, 19.51, 19.07, 18.68, 18.52, 18.15, 17.56, 17.15, 16.97, 16.62, 16.55, 15.92, 15.48, 15.14, 14.61, 14.21, 13.85, 13.24, 12.75, 12.41, 12.07, 11.71, 11.29, 11.37, 11.09, 11.00, 10.75, 10.82, 10.58, 10.28, 10.15, 10.18, 10.18, 10.09, 9.97, 9.96, 9.85, 9.82, 9.70, 9.69, 9.70, 9.54, 9.46, 9.42, 9.48, 9.43, 9.26, 9.29, 9.23, 9.21, 9.25, 9.20, 9.09, 9.09, 9.01, 8.91, 8.99, 8.95, 9.02, 9.03, 8.89, 8.81, 8.86, 8.73, 8.84, 8.86, 8.68, 8.66, 8.67, 8.74, 8.64, 8.61]


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
