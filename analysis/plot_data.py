import numpy as np

import matplotlib.pyplot as plt

# Load data from npz file
file_path = 'analysis/recorded_positions.npz'  # Replace with your file path
data = np.load(file_path)

# Extract the data
positions = data['positions']  # Replace with the appropriate key
is_dones = data['is_dones']  # Replace with the appropriate key
num_robot = positions.shape[1]
num_timesteps = positions.shape[0]
num_dimensions = positions.shape[2]

# print("Number of robots:", num_robot)
# print("Number of successful robots:", np.sum(is_dones == 0.0))

valid_indices = np.where(is_dones == 0.0)[0]
x_positions = positions[:, :, 0] + 90.0
mean_x_positions = np.mean(x_positions, axis=1)
std_x_positions = np.std(x_positions, axis=1)

y_positions = positions[:, :, 1]
mean_y_positions = np.mean(y_positions, axis=1)
std_y_positions = np.std(y_positions, axis=1)

time = np.arange(num_timesteps) * 1/50

plt.rcParams.update({'font.size': 10, 'font.family': 'Times New Roman', 'legend.fontsize': 8})

fig, ax = plt.subplots(2, 1, figsize=(3.0, 2.9), sharex=True)
ax[0].plot(time, mean_x_positions, label='mean x position', color='blue')
ax[0].fill_between(time, mean_x_positions - std_x_positions, mean_x_positions + std_x_positions, color='blue', alpha=0.3)

ax[0].grid(True, which='both', linestyle='--', linewidth=0.5)
ax[0].plot([time[0], time[-1]], [7.5, 7.5], color='black', label='x command', linestyle='--',lw=1.5)
ax[0].set_ylabel('X position (m)')
ax[0].legend()
ax[0].minorticks_on()
ax[0].tick_params(axis='both', which='both', direction='in')

ax[1].plot(time, mean_y_positions, label='mean y position', color='orange')
ax[1].fill_between(time, mean_y_positions - std_y_positions, mean_y_positions + std_y_positions, color='orange', alpha=0.3)
ax[1].grid(True, which='both', linestyle='--', linewidth=0.5)
ax[1].plot([time[0], time[-1]], [1.5, 1.5], color='black', label='y command', linestyle='--', lw=1.5)
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Y position (m)')
ax[1].legend()
ax[1].minorticks_on()
ax[1].tick_params(axis='both', which='both', direction='in')

plt.tight_layout(h_pad=0.1)
plt.savefig('analysis/recorded_positions.png', dpi=300, bbox_inches='tight')