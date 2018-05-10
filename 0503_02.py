import operator

def find_name(my_student,name):
	for id, i in my_student.items():
		if i == name:
			return id

student = {20181696:"조재오",20191694:"조영완"}

while True :
	n = int(input("추가 : 1, 검색 : 2, 정렬 : 3, 삭제 : 4, 종료 : 5 >>"))
	if n == 1:
		student_id = int(input("학번을 입력하세요.>>"))
		student_name = input("이름을 입력하세요.>>")
		student.update({student_id:student_name})
		print(student)
	elif n == 2:
		m = int(input("학번으로 검색 : 1, 이름으로 검색 : 2>>"))
		if m == 1:
			student_id = int(input("학번을 입력하세요.>>"))
			print("이름 : ",student[student_id])
		elif m == 2:
			student_name = input("이름을 입력하세요.>>")
			print("학번 :",find_name(student,student_name))

	elif n == 3:
		m = int(input("학번으로 정렬 : 1, 이름으로 정렬 : 2>>"))
		if m == 1:
			sortedArr = sorted(student.items())
			student = sortedArr
		elif m == 2:
			sortedArr = sorted(student.itmes(),key=operator.itemgetter(1))
			student = sortedArr
		print(student)

	elif n == 4:
		m = int(input("학번으로 삭제 : 1, 이름으로 삭제 : 2>>"))
		if m == 1:
			student_id = int(input("학번을 입력하세요.>>"))
			del student[student_id]
		elif m == 2:
			student_name = input("이름을 입력하세요.>>")
			student_id = find_name(student,student_name)
			del student[student_id]
		print(student)

	elif n == 5:
		exit()		
