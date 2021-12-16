from dataclasses import dataclass 

route_list = []

@dataclass 
class game_framework: 
    room: int = None
    next_room: int = None
        