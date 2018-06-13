import tkinter.filedialog
import csv
import os

import to_data

def gradeSys():
    
    path=os.getcwd()+'\\config.txt'
    if not os.path.isfile(path):
        config_file=open('config.txt', 'w')
        config_file.write('')
        config_file.close()
    
    config=[]
    config_file=open('config.txt')
    for cfg in config_file.read().split('\n'):
        cfg=cfg.split('\t')
        config.extend(cfg)
    config_file.close()
    
    f_format=''
    
    if len(config) < 6:
        print('The configuration file is bad configured. Please set it up:')
        while f_format not in ['.csv', '.txt']:
            f_format = input("Type the default file format type ('.csv' or '.txt'): ")
        file1 = input('Type the students database file name: ')
        file2 = input('Type the classes database file name file: ')
        students_file = file1+f_format
        classes_file = file2+f_format
        string='classes_file\t'+classes_file[0:-4]+'\nstudents_file\t'+students_file[0:-4]+'\ndefault_format\t'+f_format
        config_file=open('config.txt', 'w')
        config_file.write(string)
        config_file.close()
    else:
        students_file = config[3]+config[5]
        classes_file = config[1]+config[5]

    action=0

    print("WELCOME! Follow the instructions below: ")
    print("Current student database: "+students_file)
    print("Current classes database: "+classes_file)
    print()
    
    path=os.getcwd()+'\\'+students_file
    if not os.path.isfile(path):
        students_db=open(students_file, 'w')
        students_db.write('')
        students_db.close()
    students_db=open(students_file, 'r')
    content=students_db.read()
    print('lol')
    students_db.close()
    if len(content)>0:
        if content[-1] in ['', '\n']:
            content=content[:-1]
    students=content.split('\n')

    path=os.getcwd()+'\\'+classes_file
    if not os.path.isfile(path):
        classes_db=open(classes_file, 'w')
        classes_db.write('')
        classes_db.close()
    classes_db=open(classes_file, 'r')
    content=classes_db.read()
    classes_db.close()
    if len(content)>0:
        if content[-1] in ['', '\n']:
            content=content[:-1]
    classes=content.split('\n')
    
    while int(action)==0:
        print('(1):\tAccess the student database')
        print('(2):\tAccess the classes database')
        print('(3):\tAccess the grades database')
        action = input("Type your desired action: ")
        if action.isnumeric():
            if int(action) not in [0,1,2,3]:
                print('[ERROR] Wrong option!')
                print()
                action=0

        elif action == 'done':
            print('Good bye!')
            break
        else:
            print('[ERROR] Wrong option!')
            print()
            action=0
            
        while int(action) == 1:
            
            print()
            print("Students Database! Type any name to store a student ")
            print("Type 'show' to show all students")
            print("Type 'rename [oid] [new name]' to update a student name")
            print("Type 'del [oid]' to delete a student")
            print("Type 'import' to import students name from a file (txt or csv)")
            print("Type 'clear' to completaly erase the students db")
            print("Type 'done' to save modifications and return to the main menu")
            option=input("Type option: ")
            print()

            if option == 'done':
                students=[student for student in students if student != '']
                
                if students_file[-3:] == 'txt':
                    students_db = open(students_file, 'w')
                    for student in students:
                        students_db.write(student+'\n')
                    students_db.close()
                    action=0
                elif students_file[-3:] == 'csv':
                    students_db = open(students_file, 'w', newline='', encoding='utf8')
                    for student in students:
                        csv.writer(students_db).writerow([student])
                    students_db.close()
                    action=0
                else:
                    print('[ERROR]: Unknow file format')
            
            elif option == 'show':
                print('===[ List of students ]===')
                for i,k in enumerate(students):
                    print(i,k)

            elif option == 'clear':
                students=[]

            elif option == 'import':
                file_path = tkinter.filedialog.askopenfilename()
                
                if file_path[-3:] == 'txt':
                    file = open(file_path)
                    content = []
                    content = file.read()
                    file.close()
                    content=content.split('\n')
                    students.extend(content)
                    print('===[ Import students ]===')
                    print(len(content),"students imported from file '"+file_path+"'")
                elif file_path[-3:] == 'csv':
                    file = open(file_path,encoding='utf8')
                    content = []
                    for row in csv.reader(file):
                        content.extend(row)
                    file.close()
                    students.extend(content)
                    print('===[ Import students ]===')
                    print(len(content),"students imported from file '"+file_path+"'")
                
            elif 'rename' in option:
                option=option.split(' ')
                if len(option)==3:
                    if option[1].isnumeric():
                        if int(option[1]) >= len(students):
                            print('[ERROR] Student not found, check Id!')
                        else:
                            print('===[ Rename student ]===')
                            print('Student',students[int(option[1])],'updated to',option[2],'!')
                            students[int(option[1])]=option[2]
                    else:
                        print('[ERROR] Unknow Id')
                else:
                    print('[ERROR] Unknow option')
                
            elif 'del' in option:
                option=option.split(' ')
                if len(option)==2:
                    if option[1].isnumeric():
                        if int(option[1]) >= len(students):
                            print('[ERROR] Student not found, check Id!')
                        else:
                            print('===[ Delete student ]===')
                            print('Student',students[int(option[1])],'deleted!')
                            students.pop(int(option[1]))
                    else:
                        print('[ERROR] Unknow Id')
                else:
                    print('[ERROR] Unknow option')
                
            else:
                students.append(option)
                print('===[ Add student ]===')
                print('Student',option,'added to the database!')

        while int(action) == 2:
            print()
            print("Classes Database! Type any name to store a class ")
            print("Type 'show' to show all classes")
            print("Type 'rename [id] [new name]' to update a class name")
            print("Type 'del [id]' to delete a class")
            print("Type 'import' to import classes name from a file (txt or csv)")
            print("Type 'clear' to completaly erase the classes db")
            print("Type 'done' to save modifications and return to the main menu")
            option=input("Type option: ")
            print()

            if option == 'done':
                classes=[cls for cls in classes if cls != '']
                
                if classes_file[-3:] == 'txt':
                    classes_db = open(classes_file, 'w')
                    for cls in classes:
                        classes_db.write(cls+'\n')
                    classes_db.close()
                    action=0
                elif classes_file[-3:] == 'csv':
                    classes_db = open(classes_file, 'w', newline='', encoding='utf8')
                    for cls in classes:
                        csv.writer(classes_db).writerow([cls])
                    classes_db.close()
                    action=0
                else:
                    print('[ERROR]: Unknow file format')
            
            elif option == 'show':
                print('===[ List of class ]===')
                for i,k in enumerate(classes):
                    print(i,k)

            elif option == 'clear':
                classes=[]

            elif option == 'import':
                file_path = tkinter.filedialog.askopenfilename()
                
                if file_path[-3:] == 'txt':
                    file = open(file_path)
                    content = []
                    content = file.read()
                    file.close()
                    content=content.split('\n')
                    classes.extend(content)
                    print('===[ Import classes ]===')
                    print(len(content),"classes imported from file '"+file_path+"'")
                elif file_path[-3:] == 'csv':
                    file = open(file_path,encoding='utf8')
                    content = []
                    for row in csv.reader(file):
                        content.extend(row)
                    file.close()
                    classes.extend(content)
                    print('===[ Import classes ]===')
                    print(len(content),"classes imported from file '"+file_path+"'")
                
            elif 'rename' in option:
                option=option.split(' ')
                if len(option)==3:
                    if option[1].isnumeric():
                        if int(option[1]) >= len(classes):
                            print('[ERROR] Class not found, check Id!')
                        else:
                            print('===[ Rename class ]===')
                            print('Class',classes[int(option[1])],'updated to',option[2],'!')
                            classes[int(option[1])]=option[2]
                    else:
                        print('[ERROR] Unknow Id')
                else:
                    print('[ERROR] Unknow option')
                
            elif 'del' in option:
                option=option.split(' ')
                if len(option)==2:
                    if option[1].isnumeric():
                        if int(option[1]) >= len(classes):
                            print('[ERROR] Class not found, check Id!')
                        else:
                            print('===[ Delete class ]===')
                            print('Class',classes[int(option[1])],'deleted!')
                            classes.pop(int(option[1]))
                    else:
                        print('[ERROR] Unknow Id')
                else:
                    print('[ERROR] Unknow option')
                
            else:
                classes.append(option)
                print('===[ Add class ]===')
                print('Class',option,'added to the database!')



        while int(action) == 3:
            print()
            print("Scores Database!")
            print("Type 'all data' to see all available data")
            print("Type 'rank data' to see data related to ranks")
            print("Type 'grade data' to see data related to grades")
            print("Type 'class data' see data related to classes")
            print("Type 'show [student]' see data related to a student")
            print("Type 'done' to return to main menu")
            
            print()

            a,b,c,d = to_data.to_pandas(classes, students)
            
            option=input("Type option: ")
            
            if option == 'done':
                action=0

            elif option == 'all data':
                print(a)
            
            elif option == 'rank data':
                print(b)
            
            elif option == 'grade data':
                print(c)
            
            elif option == 'class data':
                print(d)
            
            elif 'show' in option.split(' '):
                name = option.split(' ')[1]
                if name in list(a['Name'].unique()):
                    print(a[a['Name']==str(name)])
                else:
                    print("Student",name,"not found!")

            else:
                print("Unknow option")

#def test():
#    import pandas as pd
#    import random
#    
#    file=open('students.txt')
#    students=file.read()
#    file.close()
#    students=students.split('\n')
#    students=students[:-1]
#    students=sorted(students)
#    
#    file=open('classes.txt')
#    classes=file.read()
#    file.close()
#    classes=classes.split('\n')
#    classes=classes[:-1]
#    classes=sorted(classes)
#    
#    scores=[]
#    
#    for cls in classes:
#        for student in students:
#            scores.append([cls, student, float('{0:.1f}'.format(random.uniform(0,100)))])
#    
#    len(scores)
#    
#    data=pd.DataFrame(scores, columns=('Class', 'Students', 'Score'))
#    
#    data_students=data[data['Score']>=60].groupby(('Students'))['Score'].count()
#    
#    idx=data['Score']>=60
#    
#    data[idx]