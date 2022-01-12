# 공식 모듈
import time
import os
# 커스텀 모듈
import globalVar
import route
import saveload
import menu
import GUI

"""
	[문자 출력]
	한 글자씩 출력해주는 기능
	sleepTime을 조정하여 빠르게/느리게 출력이 가능 (단위 : 초)
	특수 기능들에 대한 예외처리도 여기서 담당한다 (`, $, $$, _, __, >nn)
"""


def printScript(sentence, i, sleepTime=0.1):
    # 속도 조절
    if(sentence[i] == '>'):
        delayRate = (int(sentence[i+1]) * 10) + int(sentence[i+2])
        sleepTime = delayRate*0.01
        i += 2
    # 선택지
    elif(sentence[i] == '$'):
        if(sentence[i+1] == '$'):
            routeCheck()
            return 1
        else:
            print('$', end="")
    # 게임 끝
    elif (sentence[i] == '_'):
        if (sentence[i+1] == '_'):
            menu.endingMenu()
            return 1
        else:
            print('_', end="")
    else:
        return sentence[i]
        time.sleep(sleepTime)


"""
	[분기점 선택기]
	선택지 입력받은 후 routeSelect를 다음 룸으로 지정.
	선택 후 룸을 옮기고 상태를 저장한다.
"""


def routeCheck():
    while True:
        print("당신의 선택은? >> ", end="")
        select = input()
        if(select != ""):
            globalVar.status.next_room = route.routeSelect(
                globalVar.status.room, int(select))
            if(globalVar.status.next_room != -1):
                print(select + " 번을 선택했습니다. \n", flush=True)
                globalVar.status.room = globalVar.status.next_room
                saveload.autoSave(globalVar.status.room)
                break
        print("잘못된 선택입니다!")


"""
	[게임 작동부]
	게임 스크립트를 받아와 출력한다.
	1. 현재 룸 번호를 받아와 Script 폴더 안에서 찾아 읽어들인다. (스크립트를 찾을 수 없는 경우 게임을 종료시킨다.)
	2. printScript 함수로 파일의 끝까지 출력한다.
	
	gameCore가 정상적으로 종료되면 1을, 비정상적으로 종료된다면 0을 반환한다.

"""


def gameCore():
    file_name = globalVar.FolderName + "/Script/Script_" + \
        str(globalVar.status.room) + ".txt"

    print(file_name)

    if os.path.isfile(file_name) == False:
        return file_name + " 파일이 존재하지 않습니다!!"

    globalVar.game_script = open(file_name, "r", encoding='utf-8')
