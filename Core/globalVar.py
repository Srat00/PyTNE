# 공식 모듈
from dataclasses import dataclass

route_list = []


@dataclass
class game_framework:
    room: int = None
    next_room: int = None


status = game_framework(-1, 0)

sleepTime = 0.1

FolderName = ""
game_script = ""
