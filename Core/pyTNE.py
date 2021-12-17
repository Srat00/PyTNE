import globalVar
import route
import saveload
import struct
import core

route.routeInit()
#print(globalVar.route_list) #디버그
while True:
	if core.gameCore() == 1:
		break