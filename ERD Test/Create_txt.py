import os.path

answer_file_rep = ["DBF_" + str(number) for number in range(4, 16)]
num = 6
while answer_file_rep:
    for files in answer_file_rep:
        file = open('DBF_{}.txt'.format(num), mode='w+')
        num += 1
        answer_file_rep.pop(0)
    



