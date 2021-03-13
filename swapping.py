def reverse():
    with open('teacherlist.txt','r') as a:
        data_a=a.read()
    with open('studentslist.txt','r') as b:
        data_b=b.read()
    with open('teacherlist.txt','w') as a:
        a.write(data_b)
    with open('studentslist.txt','w') as b:
        b.write(data_a)

reverse()