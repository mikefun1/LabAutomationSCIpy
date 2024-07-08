# from matplotlib import pyplot as plt


# data = {}
# headers = []

# colors = ['Red','Yellow','Green','Blue','White']
# col = ['R','Y','G','B','W']
# linecolors = ['r','y','g','b','k']
# image_name = 'LED_VI_Curves.png'
# file_name = 'LED_VI_Curves.txt'

# with open('LED_IV_Curves_dmm.txt', 'r') as file:
#     # Read the first line (header)
#     headers = file.readline().strip().split(',')

#     # Initialize empty lists for each column
#     for header in headers:
#         data[header] = []

#     # Read the remaining lines
#     for line in file:
#         # Split the line into individual values
#         values = line.strip().split(',')

#         # Assign values to corresponding columns
#         for i, header in enumerate(headers):
#             data[header].append(float(values[i]))

# # Print the headers
# # print(headers)

# # Print the imported data
# # for header in headers:
# #     print(f'{header}: {data[header]}')

# print('\n# V_PS_R')
# print(data['# V_PS_R'])


# plt.figure()
# # for i in range(len(colors)):
# #     plt.plot(data[],data[:,i*3+2]*1000,linecolors[i]\
# #              ,label=colors[i])
# VLEDC = ['V_LED_R','V_LED_Y','V_LED_G','V_LED_B','V_LED_W']
# IC = ['I_R','I_Y','I_G','I_B','I_W',]




# # print(data['I_R'][47]*1000)    

from matplotlib import pyplot as plt

data = {}
headers = []

colors = ['Red', 'Yellow', 'Green', 'Blue', 'White']
linecolors = ['r', 'y', 'g', 'b', 'k']
image_name = 'LED_VI_Curves.png'
file_name = 'LED_VI_Curves.txt'

with open('LED_IV_Curves_dmm.txt', 'r') as file:
    # Read the first line (header)
    headers = file.readline().strip().split(',')

    # Initialize empty lists for each column
    for header in headers:
        data[header] = []

    # Read the remaining lines
    for line in file:
        # Split the line into individual values
        values = line.strip().split(',')

        # Assign values to corresponding columns
        for i, header in enumerate(headers):
            data[header].append(float(values[i]))

plt.figure()

VLEDC = ['V_LED_R', 'V_LED_Y', 'V_LED_G', 'V_LED_B', 'V_LED_W']
IC = ['I_R', 'I_Y', 'I_G', 'I_B', 'I_W']

for i, led_color in enumerate(colors):
    current_mA = [val * 1000 for val in data[IC[i]]]  # Convert current to mA
    plt.plot(data[VLEDC[i]], current_mA, linecolors[i], label=led_color)

plt.legend()
plt.grid()
plt.xlabel('Forward Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('LED I-V Analysis')
plt.savefig(image_name)  # Save figure
plt.show()

