f = open('CupcakeInvoices.csv')

# for row in f:
#     print(row)

# f.seek(0)

# for row in f:
#     row = row.split(',')
#     print(row[2])

# f.seek(0)

# for row in f:
#     row = row.rstrip('\r\n').split(',')
#     # x = str((float(row[3])*float(row[4]))).strip('.0')
#     x = float(row[3]) * float(row[4])
#     x = '{:g}'.format(x)
#     # print("{:.2f}".format(x))
#     print(x)

# f.seek(0)

# total = 0

# for row in f:
#     row = row.rstrip('\r\n').split(',')
#     total = total + float(row[3]) * float(row[4])

# print(total)

# f.close()

choco = 0
vanil = 0
strawb = 0

for i in f:
       x = i.rstrip().split(',')
       if x[2] == 'Chocolate':
              choco = choco + (float(x[3]) * float(x[4]))
       elif x[2] == 'Vanilla':
              vanil = vanil + (float(x[3]) * float(x[4]))
       elif x[2] == 'Strawberry':
              strawb = strawb + (float(x[3]) * float(x[4]))




import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('_mpl-gallery')

# make data:
cupcake_varities = ['Chocolate', 'Vanilla', 'Strawberry']
cupcake_revenue = [choco, vanil, strawb]

ypos = np.arange(len(cupcake_varities))

plt.xticks(ypos, cupcake_varities)


plt.bar(ypos, cupcake_revenue)

plt.show()