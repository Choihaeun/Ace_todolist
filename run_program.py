import sqlite3

#프로그램 실행코드
def run_program():
	while 1:
		select = input("Choose what to do:\n(a: add data, l : List todo, m: Modify todo, q: Quit)?")
		if (select == 'a'):
			add_todo()
		elif (select == 'l'):
			list_todo()
		elif (select == 'm'):
			edit()
		elif (select == 'q'):
			break