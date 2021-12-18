import saveload


"""
    [메인메뉴]
	메뉴값을 입력받아 기능을 실행시킨다.
	1. 새로하기
	2. 이어하기
	0. 종료
"""
def mainMenu():
    while True:
        print("메뉴 값을 입력하세요. >>", end="")
        a = input()
        
        if int(a) == 1:
            return 0
            break
        elif int(a) == 2:
            return saveload.loadSave()
            break
        elif int(a) == 0:
            quit()
            break
        else:
            print("잘못된 선택입니다!")
            
"""
    [종료화면]
	게임이 종료된 경우 메뉴값을 입력받아 기능을 실행시킨다.
	1. 메인화면
	2. 종료
"""
def endingMenu():
        print("게임이 끝났습니다. 다시 하시겠습니까?")
        print("1. 메인 화면으로 0. 종료 \n")
        
        while True:
            print("메뉴 값을 입력하세요. >>", end="")
            a = input
            
            if int(a) == 1:
                return 1
                break
            elif int(a) == 0:
                quit()
                break
            else:
                print("잘못된 선택입니다!")
        
        