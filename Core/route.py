import core

def routeInit():
	game_route = open("Script/Route.txt", "r")
	"""
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
		if route_buffer[i] == '!':
			a = int(route_buffer[i + 1]) * 100
			b = int(route_buffer[i + 2]) * 10
			c = int(route_buffer[i + 3])
			
			#print("TGT", a+b+c)
			Temp_RF[0] = a + b + c
			i += 3
		
		if route_buffer[i] == '*':
			a = int(route_buffer[i + 1])
			
			#print("SEL", a)
			Temp_RF[1] = a
			i += 1
		
		if route_buffer[i] == '>':
			a = int(route_buffer[i + 1]) * 100
			b = int(route_buffer[i + 2]) * 10
			c = int(route_buffer[i + 3])
			
			#print("RTN", a+b+c)
			Temp_RF[2] = a + b + c
			i += 3

			List_temp_RF = list(Temp_RF)
			core.route_list.append(List_temp_RF)
						
		target_room = 0;
		select_route = 0;
		return_room = 0;
			
			
		
print("Route Read Complete.")