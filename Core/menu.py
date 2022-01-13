# 공식 모듈
import os
# 커스텀 모듈
import saveload
import globalVar

"""
	[게임 인트로 로고]
	Script 파일에 있는 Intro.txt 파일을 열어서 출력
"""


def intro():
    filePath = globalVar.FolderName + "/Script/Intro.txt"
    if os.path.isfile(filePath) == False:
        return "Error : " + filePath + " 파일을 찾을 수 없습니다!"

    intro_file = open(filePath, "r", encoding='UTF8')
    return intro_file.read()


"""
	[게임 정보]
	Script 파일에 있는 Intro.txt 파일을 열어서 출력
"""


def manifest():
    filePath = globalVar.FolderName + "/Script/Manifest.txt"
    if os.path.isfile(filePath) == False:
        return "Error : " + filePath + " 파일을 찾을 수 없습니다!"

    manifest_file = open(filePath, "r", encoding='UTF8')
    return manifest_file.read()


"""
    [메인메뉴]
	메뉴값을 입력받아 기능을 실행시킨다.
	1. 새로하기
	2. 이어하기
	0. 종료
"""


def mainMenu(a):
    if int(a) == 1:
        return 0
    elif int(a) == 2:
        return saveload.loadSave()
    elif int(a) == 0:
        quit()
    else:
        return "잘못된 선택입니다!"


"""
    [종료화면]
	게임이 종료된 경우 메뉴값을 입력받아 기능을 실행시킨다.
	1. 메인화면
	2. 종료
"""


def endingMenu():
    print("1. 메인 화면으로 0. 종료 \n")

    while True:
        print("메뉴 값을 입력하세요. >> ", end="")
        a = input()

        if int(a) == 1:
            return 1
            break
        elif int(a) == 0:
            quit()
            break
        else:
            print("잘못된 선택입니다!")
