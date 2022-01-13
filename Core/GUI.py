from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import Qt
from PyQt5.QtWidgets import *
import sys
import time

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
        self.Line_Selection.returnPressed.connect(self.Select)

        # 디버그 옵션
        self.RoomLoad.clicked.connect(self.GUIIntro)

    # =======================   UI 연결 =======================

    def PlaysetLoad(self):
        globalVar.FolderName = QFileDialog.getExistingDirectory(
            self, "게임 불러오기")
        self.GameText.setPlainText(menu.intro())
        self.Line_Nowplay.setText(menu.manifest())
        route.routeInit()

    def Select(self):
        print(globalVar.status.room)
        if self.Line_Selection.text() != "":
            selectNo = self.Line_Selection.text()
        else:
            self.GameText.append("잘못된 선택 입니다!")
            return

        self.Line_Selection.setText("")

        # 메인화면
        if globalVar.status.room == -1:
            if selectNo == '1':
                self.GameCore(selectNo)

            elif selectNo == '2':
                globalVar.status.room = saveload.loadSave()
                self.GameCore(selectNo)

            elif selectNo == '0':
                quit()

            else:
                self.GameText.append("잘못된 선택 입니다!")

        elif globalVar.status.room == -2:
            globalVar.status.room = -1
            self.GameText.setPlainText(menu.intro())

        else:
            self.GameCore(selectNo)

    def GameCore(self, selectNo):
        self.GameText.setPlainText("")
        globalVar.status.next_room = route.routeSelect(
            globalVar.status.room, int(selectNo))

        if globalVar.status.next_room == 404:
            self.GameText.append("잘못된 선택 입니다!")
            return

        if(globalVar.status.next_room != -1):
            self.GameText.setPlainText("")
            self.GameText.append(selectNo + " 번을 선택했습니다.")
            globalVar.status.room = globalVar.status.next_room
            saveload.autoSave(globalVar.status.room)

        else:
            globalVar.status.room = 0

        core.gameCore()
        script_buffer = globalVar.game_script.readlines()

        i = 0
        while i != len(script_buffer)-1:
            self.GameText.append(core.printScript(script_buffer, i))
            i += 1

        if script_buffer[len(script_buffer)-1] == '$':
            self.GameText.append("당신의 선택은?")
        elif script_buffer[len(script_buffer)-1] == '_':
            self.GameText.append("게임이 끝났습니다... 0. 메인화면으로 돌아가기")
            globalVar.status.room = -2

    # ======================= 디버그 옵션 =======================

    def GUIIntro(self):
        self.GameText.setPlainText(menu.intro())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec_())
