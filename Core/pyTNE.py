# 커스텀 모듈
import globalVar
import route
import saveload
import struct
import core
import menu
import GUI

# 여깄는걸 GUI로 옮기고 GUI에서 함수들이 작동되도록 해야함
route.routeInit()
menu.intro()
globalVar.status.room = menu.mainMenu()
while True:
    if core.gameCore() == 1:
        break
