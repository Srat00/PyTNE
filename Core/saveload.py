#공식 모듈
import os

"""
    [저장하기]
	savedata_.bin파일을 열어 현재 있는 방 번호를 저장한다
"""
def autoSave(room_no):
    save_file = open("savedata__", "w")
    save_file.write(str(room_no))
    save_file.close
    
"""
    [이어하기]
	savedata_.bin파일을 열어 저장되어있는 방 번호를 반환한다
	만약 savedata_.bin이 없다면 안내 후 종료한다.
"""
def loadSave():
    if os.path.isfile("savedata__") == False:
        print("세이브 파일이 존재하지 않습니다!!!")
        input()
        quit()
        
    save_file = open("savedata__", "r")
    room_no = save_file.read()
    
    return int(room_no)
    