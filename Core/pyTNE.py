#커스텀 모듈
import globalVar
import route
import saveload
import struct
import core
import menu

route.routeInit()
menu.intro()
globalVar.status.room = menu.mainMenu()
while True:
	if core.gameCore() == 1:
		break