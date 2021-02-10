from scipy.io import loadmat
import matplotlib.pyplot as plt

lowMV = loadmat('EE471_LabII_Exp_2_100n_capacitor')

CH1_x = lowMV.get('time_axis')
CH1_y = lowMV.get('time_trace')

CH2_x = lowMV.get('time_axis_ch2')
CH2_y = lowMV.get('time_trace_ch2')

CH1_x = CH1_x[0] * 1000
CH1_y = CH1_y[0]
CH2_x = CH2_x[0] * 1000
CH2_y = CH2_y[0]

print(CH1_x[0])
print(CH2_x[0])
print(type(CH1_x), CH1_x.shape)
print(type(CH1_y), CH1_y.shape)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(CH1_x, CH1_y)
ax1.set_xlim(CH1_x[0], CH1_x[len(CH2_x) - 1])
ax1.grid(True)
ax1.set_xlabel('Time in ms')
ax1.set_ylabel('Amplitude')
ax1.set_title('Square wave')

ax2.plot(CH2_x, CH2_y)
ax2.set_xlim(CH2_x[0], CH2_x[len(CH2_x) - 1])
ax2.grid(True)
ax2.set_xlabel('Time in ms')
ax2.set_ylabel('Amplitude')
ax2.set_title('Triangle wave')

plt.show()

