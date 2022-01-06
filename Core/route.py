# 공식 모듈
import os
# 커스텀 모듈
import globalVar
import GUI

"""  
	[루트 파일 초기화]
	Script 파일에 있는 Route.txt 파일을 열어서 해당 게임의 분기점을 2차원 배열 형태로 저장함
	
	! → 해당 방 번호 ( 0번 인덱스 ) 
	* → 선택지 번호  ( 1번 인덱스 )
	> → 이동되는 방 번호 ( 2번 인덱스 )
"""


def routeInit():
    if os.path.isfile("Script/Route.txt") == False:
        print("Route.txt 파일이 존재하지 않습니다!!")
        input()
        quit()
    game_route = open("Script/Route.txt", "r")
    Temp_RF = [0, 0, 0]
    route_buffer = game_route.read()

    i = 0

    for i in range(len(route_buffer)):
        # 해당 방 번호 (index 0)
        if route_buffer[i] == '!':
            a = int(route_buffer[i + 1]) * 100
            b = int(route_buffer[i + 2]) * 10
            c = int(route_buffer[i + 3])

            Temp_RF[0] = a + b + c
            i += 3

        # 선택지 번호 (index 1)
        if route_buffer[i] == '*':
            a = int(route_buffer[i + 1])

            Temp_RF[1] = a
            i += 1

        # 이동 방 번호 (index 2)
        if route_buffer[i] == '>':
            a = int(route_buffer[i + 1]) * 100
            b = int(route_buffer[i + 2]) * 10
            c = int(route_buffer[i + 3])

            Temp_RF[2] = a + b + c
            i += 3

            # 배열에 저장
            List_temp_RF = list(Temp_RF)
            globalVar.route_list.append(List_temp_RF)

        # Flush
        target_room = 0
        select_route = 0
        return_room = 0

    print("Route Read Complete.")


"""
    [분기점 불러오기]
	루트 매니저 array 접근 후
	room → target_room, select → select_route 에 해당하는 요소 검색 후 return_room 반환
	만약 해당되는 요소가 없다면 -1 반환
"""


def routeSelect(room, select):
    for i in range(0, len(globalVar.route_list)):
        if globalVar.route_list[i][0] == int(room) and globalVar.route_list[i][1] == int(select):
            return globalVar.route_list[i][2]

    return -1
