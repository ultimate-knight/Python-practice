#Today we are learning abot read readiness and other methods#
f=open('students.txt', 'r')
i=0
while True:
    i=i+1
    line=f.readline()
    # print(line, type(line))
    if not line:
        break
    m1=line.split(',')[0]
    m2=line.split(',')[1]
    m3=line.split(',')[2]
    print(f"student{i} scored {m1} marks")
    print(f"student{i} scored {m2} marks")
    print(f"student{i} scored {m3} marks")
    print(line)