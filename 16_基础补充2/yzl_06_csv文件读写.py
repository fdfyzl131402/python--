import csv

# file = open("demo.csv", "w")
# w = csv.writer(file)
# # w.writerow(['name', 'age', 'height', 'city'])
# # w.writerow(['zhangsan', 19, 178, 'wuhan'])
# w.writerows([
#     ['name', 'age', 'height', 'city'],
#     ['zhangsan', 19, 178, 'wuhan']
# ])
# file.close()

file = open("text.csv", "r")
r = csv.reader(file)
for date in r:
    print(date)

file.close()