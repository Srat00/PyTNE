import globalVar

"""  
	[루트 파일 초기화]
	Script 파일에 있는 Route.txt 파일을 열어서 해당 게임의 분기점을 2차원 배열 형태로 저장함
	
	! → 해당 방 번호 ( 0번 인덱스 ) 
	* → 선택지 번호  ( 1번 인덱스 )
	> → 이동되는 방 번호 ( 2번 인덱스 )
"""

def routeInit():
	game_route = open("Script/Route.txt", "r")
	"""
	#파일이 있는지 체크
    if(game_route == None)
    {
        print("Route.txt가 발견되지 않았습니다! 게임을 실행할 수 없습니다!")
        input()
        quit()
    }
	"""
	Temp_RF = [0,0,0]
	route_buffer = game_route.read()
	
	i = 0
	
	for i in range(len(route_buffer)):
		#해당 방 번호 (index 0)
		if route_buffer[i] == '!':
			a = int(route_buffer[i + 1]) * 100
			b = int(route_buffer[i + 2]) * 10
			c = int(route_buffer[i + 3])
			
			Temp_RF[0] = a + b + c
			i += 3
		
		#선택지 번호 (index 1)
		if route_buffer[i] == '*':
			a = int(route_buffer[i + 1])
			
			Temp_RF[1] = a
			i += 1
		
		#이동 방 번호 (index 2)
		if route_buffer[i] == '>':
			a = int(route_buffer[i + 1]) * 100
			b = int(route_buffer[i + 2]) * 10
			c = int(route_buffer[i + 3])
			
			Temp_RF[2] = a + b + c
			i += 3

			#배열에 저장
			List_temp_RF = list(Temp_RF)
			globalVar.route_list.append(List_temp_RF)
						
		#Flush
		target_room = 0;
		select_route = 0;
		return_room = 0;
			
			
	print("Route Read Complete.")
	
def routeSelect(room, select):
	for i in range(0,len(globalVar.route_list)):
		if globalVar.route_list[i][0] == int(room) and globalVar.route_list[i][1] == int(select):
			return globalVar.route_list[i][2]
		
	return -1
	
	
	
	