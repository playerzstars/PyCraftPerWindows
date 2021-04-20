# PyCraft by ZachTheCoder

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

grassBlock  = "assets/grass.png"
dirtBlock   = "assets/dirt.png"
stoneBlock  = "assets/stone.png"
diamondOre  = "assets/diamond_ore.png"
zachBlock   = "assets/zach.jpg"
pythonBlock = "assets/python.png"

blockPick = grassBlock

app = Ursina()
player = FirstPersonController(
    speed = 6,
    fov = 100,
    jump_height = 1,
    jump_duration = 0.5
    )

def update():
    print(player.y)
    if player.x > 15:
        player.x = 15
    if player.x < 0:
        player.x = 0
    if player.z > 15:
        player.z = 15
    if player.z < 0:
        player.z = 0
    if player.y < -1:
        player.y = -2
    
    global blockPick
    
    if held_keys["1"]:
        blockPick = grassBlock
    if held_keys["2"]:
        blockPick = dirtBlock
    if held_keys["3"]:
        blockPick = stoneBlock
    if held_keys["4"]:
        blockPick = zachBlock
    if held_keys["5"]:
        blockPick = pythonBlock
    if held_keys["escape"]:
        quit()
  #  print(player.x, player.y, player.z)

class Voxel(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = blockPick,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.lime,
            )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel(position = self.position + mouse.normal)
            if key == "left mouse down":
                destroy(self)

# Hotbar

#hotbar = Button(
#    model = "quad",
#    texture = "assets/hotbar.png"
#    )

for z in range(16):
    for x in range(16):
    voxel = Voxel(position = (x, y - 1, z))

player.y += 8

app.run()
