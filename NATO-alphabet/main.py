student_dict = {
    "student": ["Aayush", "Vedhas", "Anshuman", "Sarvesh"], 
    "score": [98, 76, 56, 80]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data.to_dict())
# print(nato_data[nato_data["letter"] == "A"].letter)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    
#     print(row.student)
#     nato_name = ""
#     for i in row.student:
#         nato_name += nato_data[nato_data["letter"] == i.upper()].code
#         print(nato_name)
#     #Access row.student or row.score
#     print(nato_name)
    

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_data_dict)

nato_name = {row.student: (nato_data_dict[letter] for letter in row.student) for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter your name: ").upper()
nato_name = [nato_data_dict[letter] for letter in name]
print(nato_name)