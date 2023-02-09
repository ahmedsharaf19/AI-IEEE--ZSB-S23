dict_info = {}

with open("grades.txt",'r') as f :
    skip_fist_line=f.readline().split()
    for line in f :
        read_id = int(line.split()[0])
        read_name = line.split()[1]
        read_grade = line.split()[2]
        if read_grade == 'N/A' :
            continue
        else :
            read_grade = int(read_grade)
        read_birth = int(line.split()[4])
        read_gender = line.split()[6]

        dict_info[read_id] = {'name' : read_name , 'score'  : read_grade , 'birthyear' : read_birth , 'gender' : read_gender}

with open("filtered.txt",'w') as f :
    for key , value in dict_info.items() : 
        f.write(f"{key} {value['name']} - {value['birthyear']}\n")
