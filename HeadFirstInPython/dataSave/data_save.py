# @File    : data_save.py
# @Date    : 2020-05-28
# @Author  : shengjia
import pickle

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing')

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man)
    print(other)

    man_file.close()
    other_file.close()
except IOError as err:
    print('file error' + str(err))
finally:
    if 'data' in locals():
        data.close()

# new way for with
try:
    with open('man_data.txt', 'w') as man_file:
        print(man)
    with open('other_data.txt', 'w') as other_file:
        print(other)
except IOError as err:
    print('file error' + str(err))

# new way for pickle
try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error' + str(err))

except pickle.PickleError as perr:
    print('pickling error:' + str(perr))
