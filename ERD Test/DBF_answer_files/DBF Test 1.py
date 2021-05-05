import nltk
import file_init

stor_lib = file_init.file_init()
for file, desc in stor_lib.items():
    print(f"{file}: {desc}")
    
lemmatizer = nltk.WordNetLemmatizer()

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    

def question_create():
    questions = {
         "What is an ERD? ": "Entity Relationship Model",
         "Explain what an ERD is ": ["high-level conceptual data", "relationships", "systematically", "data", "database"],
         "Importance of an ERD ": ["describes entities attributes relationships", "build database quickly", "blueprint", "structure", "schematic"
         "better understanding of the information", "allows communitcation with logical structure of database", "translate to table", "translated to table",
         "preview table connections", "a preview on table connections"],
         "Why are ERDs used? ": "",
         "Give the components of an ERD ": "",
         "What is an entity? ": "",
         "Give examples of entities ": "",
         "What is an entity set? ": "",
         "Differentiate between a Weak and a Strong entity ": "",
         "What is an attribute? ": "",
         "What are the 4 types of attributes? ": "",
         "What is cardinality? ": "",
         "What are the 4 types of cardinality? ": "", 
        }     
