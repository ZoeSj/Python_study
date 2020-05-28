# @File    : file_error.py
# @Date    : 2020-05-27
# @Author  : shengjia
import os

the_file = open('sketch.txt')
for each_line in the_file:
    (role, line_spoken) = each_line.split(':', 1)
    print(role)
    print(' said:')
    print(line_spoken)
the_file.close()

# handle exception
if os.path.exists('sketch.txt'):
    the_file = open('sketch.txt')
    for each_line in the_file:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role)
            print(' said:')
            print(line_spoken)
    the_file.close()
else:
    print('the data file is missing!')

# another handle way
try:
    the_file = open('sketch.txt')
    for each_line in the_file:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role)
            print(' said:')
            print(line_spoken)
        except ValueError:
            pass
    the_file.close()
except IOError:
    print('the data file is missing!')
