f = open('CupcakeInvoices.csv')

# for row in f:
#     print(row)

# f.seek(0)

# for row in f:
#     row = row.split(',')
#     print(row[2])

# f.seek(0)

for row in f:
    row = row.rstrip('\r\n').split(',')
    # x = str((float(row[3])*float(row[4]))).strip('.0')
    x = float(row[3]) * float(row[4])
    x = '{:g}'.format(x)
    # print("{:.2f}".format(x))
    print(x)

# f.seek(0)

# total = 0

# for row in f:
#     row = row.rstrip('\r\n').split(',')
#     total = total + float(row[3]) * float(row[4])

# print(total)

# f.close()