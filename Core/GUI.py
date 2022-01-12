from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtWidgets import *
import sys

import ImageResource_rc
import menu
import core
import globalVar
import saveload
import route

form_class = uic.loadUiType("Core/GUI.ui")[0]


class Window(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Text Novel Engine v2.0")

        # UI 연결
        self.GameLoad.clicked.connect(self.PlaysetLoad)

        # 디버그 옵션
        self.RoomLoad.clicked.connect(self.GUIIntro)
        self.Line_Selection.returnPressed.connect(self.InputCheck)

    # =======================   UI 연결 =======================

    def PlaysetLoad(self):
        globalVar.FolderName = QFileDialog.getExistingDirectory(
            self, "게임 불러오기")
        self.GameText.setPlainText(menu.intro())
        self.Line_Nowplay.setText(menu.manifest())
        route.routeInit()

    def InputCheck(self):
        selectNo = self.Line_Selection.text()
        self.Line_Selection.setText("")

        if globalVar.status.room == -1:
            if selectNo == 1:
                globalVar.status.room = 0
            elif selectNo == 2:
                globalVar.status.room = saveload.loadSave()
            elif selectNo == 0:
                quit()
            else:
                self.GameText.append("잘못된 선택 입니다!")

        else:
            globalVar.status.next_room = route.routeSelect(
                globalVar.status.room, int(selectNo))

            if(globalVar.status.next_room != -1):
                self.GameText.setPlainText("")
                self.GameText.append(selectNo + " 번을 선택했습니다.")
                globalVar.status.room = globalVar.status.next_room
                saveload.autoSave(globalVar.status.room)

        core.gameCore()
        script_buffer = globalVar.game_script.read()

        self.GameText.setPlainText("")

        print(len(script_buffer))

        #i = 0
        # while i != len(script_buffer):
        #    self.GameText.append(core.printScript(script_buffer, i, 0.02))
        #    i += 1

    # ======================= 디버그 옵션 =======================

    def GUIIntro(self):
        self.GameText.setPlainText(menu.intro())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec_())
