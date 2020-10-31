students = {
    "小明": {"高等数学": 78, "大学物理": 82, "大学计算机": 65, "大学英语": 66},
    "小花": {"高等数学": 81, "大学语文": 12, "大学英语": 53, "大学计算机": 86},
    "小莲": {"大学数学": 61, "大学计算机": 21, "大学化学": 5, "大学语文": 2},
    "小亮": {"大学数学": 4, "大学化学": 5, "大学英语": 6, "大学物理": 7}
}
while True:
    print('''1.\t查询学生信息
2.\t根据课程名查询对应学生
3.\t查询不及格学生
4.\t查询当前已修读课程
5.\t查询当前所有学生成绩，并排序''')
    options = int(input('请选择(输入-1退出本程序)：'))
    print()
    if options == -1:
        print('程序退出，欢迎下次使用')
        exit()
    elif options == 1:
        name = input('请输入学生姓名：')
        for student_name, student_info in students.items():
            if student_name == name:
                print(student_info)
                print()
                break
    elif options == 2:
        course = input('请输入课程名称：')
        for student_name, student_info in students.items():
            for info, value in student_info.items():
                if info == course:
                    print('姓名：%s，课程：%s，成绩：%d' % (student_name, info, value))
                    print()
    elif options == 3:
        for student_name, student_info in students.items():
            sum = 0
            for info, value in student_info.items():
                if value < 60:
                    sum += 1
            if sum != 0:
                print('姓名：%s，不及格门数：%d' % (student_name, sum))
    elif options == 4:
        optionList = list()
        for student_name, student_info in students.items():
            for info, value in student_info.items():
                optionList.append(info)
        optionList = list(set(optionList))
        print(optionList)
    elif options == 5:
        averageScore = dict()
        for student_name, student_info in students.items():
            sum = 0
            for info, value in student_info.items():
                sum += value
            averageScore[student_name] = sum // student_info.__len__()
        sorted(averageScore.items(), key=lambda x: x[1], reverse=True)
        for i in averageScore.keys():
            print('%s平均成绩为：%d' % (i, averageScore[i]))
    else:
        print('输入错误，请重新输入')
    print()
