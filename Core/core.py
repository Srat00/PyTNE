import time
import globalVar
import route

#sentence = 출력할 문자, sleepTime = 글자가 출력되는 시간간격(단위:초)
def printScript(sentence, sleepTime=0.1):
	for i in range(len(sentence)):
		if(sentence[i] == '`'):
			input()
			break
		if(sentence[i] == '$'):
			routeCheck()
		print(sentence[i], end="")
		time.sleep(sleepTime)

def routeCheck():
	while True:
		print("당신의 선택은? >> ")
		select = input()
		globalVar.status.next_room = route.routeSelect(globalVar.status.room, int(select))
		if(globalVar.status.next_room != -1):
			print(select + " 번을 선택했습니다. \n\n")
			globalVar.status.room = globalVar.status.next_room
			break
		print("잘못된 선택입니다!")
	
	
def gameCore():
	file_name = "Script/Script_" + str(globalVar.status.room) + ".txt"
	game_script = open(file_name, "r", encoding='utf-8')
	"""
	#파일이 있는지 체크
    if(game_route == None)
    {
        print("Route.txt가 발견되지 않았습니다! 게임을 실행할 수 없습니다!")
        input()
        quit()
    }
	"""
	script_buffer = game_script.read()
	
	i = 0
	for i in range(len(script_buffer)):
		printScript(script_buffer[i], 0.02)
		