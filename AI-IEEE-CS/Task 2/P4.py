dict_info = {}

with open ("grades.txt", "r") as f:
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
print(dict_info)
old_birth = min([value['birthyear'] for value in dict_info.values()])
old_id = list((filter(lambda test : dict_info[test]['birthyear'] == old_birth,dict_info.keys())))[0]
avg = (sum(value['score'] for value in dict_info.values())) / len(dict_info.keys())
maximum=max([value['score'] for value in dict_info.values()])
id_maximum= list(filter(lambda test: dict_info[test]["score"] == maximum, dict_info.keys()))[0]
print(old_id)
print(f"{avg:.3f}")
print(dict_info[id_maximum]['gender'])

