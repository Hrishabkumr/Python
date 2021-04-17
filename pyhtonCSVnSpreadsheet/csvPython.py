import csv

print('---- How to read CSV file ----')
data = open('example.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)

print(f'Number of Rows in csv file : {len(data_lines)}')

email_list = []
for line in data_lines[1:]:
    email_list.append(line[3])

print(email_list)

print('---- How to write to CSV file ----')

file_to_output = open('save_file.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
file_to_output.close()
















