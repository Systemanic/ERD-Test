import nltk
import os.path
import time

lemmatizer = nltk.WordNetLemmatizer()


def initialize_files(file_name, ran, file_extension):
    """Picks up files at a certain range and extension then packs them in a list"""
    """Specifiy a file name and the number of files --> file_name, range and file extension that is readable e.g .txt"""
    answer_file_rep = [file_name + str(number) for number in range(1, ran)]
    answer_files_txt = [file + "{}".format(file_extension) for file in answer_file_rep]
    answers = ["answer" + str(number) for number in range(1, ran)]
    stor_lib = dict(zip(answer_files_txt, answers))
    open_read_files(stor_lib, ran)


def open_read_files(stor_lib, ran):
    """Opens up all the files packed in a list"""
    checking = [number for number in range(1, ran)]
    while checking:
        for file, answer in stor_lib.items():
            boolean = os.path.isfile(file)
            print("\nChecking if {} exists".format(file))
            time.sleep(0)
            if boolean == True:
                print("{} found!".format(file))
                checking.pop()
                time.sleep(0)
                print(f"Opening {file}...")
                answer = open(file, mode='r')
            else:
                print(f"{file} not found")
                checking.pop()           


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    


def question_create():
    questions = {
         "What is an ERD? ": "DBF_3.txt", #DBF_3.TXT
         "Explain what an ERD is ": ["high-level conceptual data", "relationships", "systematically", "data", "database"], #DBF_1.TXT
         "Importance of an ERD ": ["describes entities attributes relationships", "build database quickly", "blueprint", "structure", "schematic" #DBF_2.TXT
         "better understanding of the information", "allows communitcation with logical structure of database", "translate to table", "translated to table",
         "preview table connections", "a preview on table connections"],
         "Why are ERDs used? ": "", #DBF_4
         "Give the components of an ERD ": "", #DBF_5
         "What is an entity? ": "", #DBF_6
         "Give examples of entities ": "", #DBF_7 (BLANK FOR NOW)
         "What is an entity set? ": "", #DBF_8
         "What is a weak entity": "", #DBF_9
         "What is a strong entity": "", #DBF_10
         "What is an attribute? ": "", #DBF_11
         "What are the 4 types of attributes? ": "", #DBF_12
         "What is cardinality? ": "", #DBF_13
         "What are the 4 types of cardinality? ": "", #DBF_14
        }     
