import os.path
import time

#Use the run_all() function to save time!

def initialize_files(file_name, ran, file_extension):
    """Picks up files at a certain range and extension then packs them in a list"""
    """Specifiy the exact file name and the number of files --> file_name_(range) e.g file_name=chickens ,ran=16"""
    answer_file_rep = [file_name + str(number) for number in range(1, ran)]
    answer_files = [file + "{}".format(file_extension) for file in answer_file_rep]
    answers = ["answer" + str(number) for number in range(1, ran)]
    return answer_files, ran, answers


def file_scan(answer_files, ran, answers):
    """Opens up all the files packed in a list"""
    checking = [number for number in range(1, ran)]
    while checking:
        for file in answer_files:
            boolean = os.path.isfile(file)
            print("\nChecking if {} exists".format(file))
            time.sleep(0)
            if boolean == True:
                print("{} found!".format(file))
                # Used .pop() to remove files from 1st to last to prevent a forever loop.
                checking.pop()
                time.sleep(0)
            else:
                print(f"{file} not found")
                checking.pop()
        return answer_files, answers
 

def open_read_files(answer_files, answers):
    """Opens up every file in stored in the file folder"""
    """And designates each file to a variable in answers"""
    count = 0
    s = 0
    answer_files2 = []
    for file in answer_files[:]: # Used [:] to get all file_names in answer_files
        ans = open(file, mode='r')
        print(f"Opening {ans.name}")
        time.sleep(s)
        answers[count] = ans
        count += 1
        if ans.closed == False: # Section for checking if files are closed
            print(f"Closing {ans.name}")
            ans.close()
            answer_files2.append(ans.name)
            answer_files.remove(ans.name)
            time.sleep(s)
    return answer_files2, answers

    
def group(answer_files2, answers):
    stor_lib = dict(zip(answer_files2, answers))
    return stor_lib

def file_init():
    """A quick way to run all the above modules"""
    answer_files, ran, answers = initialize_files("DBF_", 15, ".txt")
    answer_files, answers = file_scan(answer_files, ran, answers)
    answer_files2, answers = open_read_files(answer_files, answers)
    stor_lib = group(answer_files2, answers)
    return stor_lib
