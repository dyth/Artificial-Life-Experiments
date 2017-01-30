#!/usr/bin/env python
"""neuron model with diffusion, fire at threshold: 100.0"""
import matplotlib.pyplot as plt
import random

graph = [0.0, 2.990000000000009, 5.890300000000025, 8.703591000000017, 11.432483270000034, 14.079508771900038, 16.64712350874305, 19.13770980348076, 21.553578509376337, 23.89697115409504, 26.170062019472198, 28.37496015888803, 30.513711354121384, 32.588300013497744, 34.6006510130928, 36.55263148270002, 38.44605253821902, 40.28267096207246, 42.064190833210276, 43.79226510821397, 45.46849715496755, 47.09444224031853, 48.671608973108974, 50.2014607039157, 51.68541688279822, 53.124854376314275, 54.52110874502485, 55.875475482674105, 57.189211218193876, 58.46353488164807, 59.69962883519864, 60.89863997014268, 62.0616807710384, 63.18983034790725, 64.28413543747004, 65.34561137434594, 66.37524303311555, 67.37398574212209, 68.34276616985844, 69.2824831847627, 70.19400868921983, 71.07818842854323, 71.93584277568694, 72.76776749241634, 73.57473446764385, 74.35749243361452, 75.11676766060609, 75.8532646307879, 76.56766669186428, 77.26063669110835, 77.9328175903751, 78.58483306266385, 79.21728807078394, 79.83076942866042, 80.42584634580061, 81.0030709554266, 81.56297882676381, 82.1060894619609, 82.63290677810208, 83.14391957475902, 83.63960198751624, 84.12041392789077, 84.58680151005404, 85.03919746475242, 85.47802154080985, 85.90368089458555, 86.31657046774798, 86.71707335371553, 87.10556115310408, 87.48239431851096, 87.84792248895562, 88.20248481428695, 88.54641026985834, 88.88001796176259, 89.20361742290972, 89.51750890022242, 89.82198363321575, 90.11732412421928, 90.4038044004927, 90.68169026847792, 90.95123956042359, 91.21270237361088, 91.46632130240255, 91.71233166333047, 91.95096171343056, 92.18243286202764, 92.40695987616681, 92.6247510798818, 92.83600854748535, 93.0409282910608, 93.23970044232897, 93.4325094290591, 93.61953414618733, 93.80094812180172, 93.97691967814768, 94.14761208780325, 94.31318372516915, 94.47378821341408, 94.62957456701166, 94.78068733000131, 94.92726671010126, 95.06944870879823, 95.20736524753428, 95.34114429010826, 95.47090996140501, 95.59678266256287, 95.718879182686, 95.83731280720542, 95.95219342298927, 96.0636276202996, 96.17171879169061, 96.27656722793989, 96.3782702111017, 96.47692210476865, 96.57261444162559, 96.66543600837682, 96.7554729281255, 96.84280874028174, 96.92752447807328, 97.0096987437311, 97.08940778141917, 97.1667255479766, 97.2417237815373, 97.31447206809119, 97.38503790604847, 97.45348676886701, 97.519882165801, 97.58428570082697, 97.64675712980215, 97.7073544159081, 97.76613378343086, 97.82314976992794, 97.8784552768301, 97.9321016185252, 97.98413856996945, 98.03461441287037, 98.08357598048426, 98.13106870106972, 98.17713664003763, 98.2218225408365, 98.26516786461141, 98.30721282867307, 98.34799644381289, 98.3875565504985, 98.42592985398355, 98.46315195836404, 98.49925739961311, 98.53427967762472, 98.56825128729598, 98.60120374867711, 98.6331676362168, 98.6641726071303, 98.69424742891638, 98.7234200060489, 98.75171740586742, 98.7791658836914, 98.80579090718066, 98.83161717996525, 98.85666866456629, 98.8809686046293, 98.90453954649043, 98.92740336009572, 98.94958125929286, 98.97109382151407, 98.99196100686865, 99.01220217666258, 99.03183611136271, 99.05088102802182, 99.06935459718116, 99.08727395926573, 99.10465574048776, 99.12151606827312, 99.13787058622492, 99.15373446863816, 99.16912243457901, 99.18404876154165, 99.1985272986954, 99.21257147973454, 99.2261943353425, 99.23940850528223, 99.25222625012375, 99.26465946262005, 99.27671967874144, 99.28841808837919, 99.29976554572781, 99.31077257935598, 99.3214494019753, 99.33180591991604]

def boost(x):
    i = 0
    while ((graph[i] < x) and (i < 187)):
        i += 1
    return i

number = 50
count = [random.randint(0, 188) for _ in range(number)]
buf = [[graph[i-1]] for i in count]

plt.ion()

while True:
    correction = [0.0 for _ in range(number)]
    for i in range(number):
        buf[i].append(graph[count[i]])
        count[i] += 1
        # if over threshold, add potential to others
        if (count[i] > 186):
            for j in range(number):
                correction[j] += 2
                
    # reset neuron if hyperpolerisation reached
    for j in range(number):
        if (boost(graph[count[j]] + correction[j]) > 186):
            count[j] = 1
        else:
            count[j] = boost(graph[count[j]] + correction[j])
        # if buffer over 400 length, delete first item and then plot
        if (len(buf[j]) > 400):
            buf[j].pop(0)
        plt.plot(buf[j])
    plt.pause(0.001)
    plt.clf() # clear screen
