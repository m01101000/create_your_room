from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#world
class sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene, model='sphere', scale=5000, double_sided=True, texture="img/sphere/sphere.jpg"
        )
#floor
for z in range(10):
    for x in range(19):
        Entity(
            model="cube", color=color.dark_gray, collider="box", ignore=True, position=(x, 0, z), parent=scene, origin_y=0.5, texture="img/texture/6.jpg"
        )
#roof
for z in range(10):
    for x in range(19):
        Entity(
            model="cube", color=color.dark_gray, collider="box", ignore=True, position=(x, 5, z), parent=scene, origin_y=0.5, texture="img/texture/6.jpg"
        )
#wall
for x in range(19):
    for y in range(5):
        Entity(
            model="quad", collider="box", ignore=True, position=(x,y,9.5), texture="img/texture/1.jpg"
        )
#wall
for z in range(10):
    for y in range(5):
        spawnh=Entity(
            model="quad", rotation = (0,270,0), collider="box", ignore=True, position=(-0.5,y,z), texture="img/texture/1.jpg"
        )
#wall
for x in range(13):
    for y in range(5):
        Entity(
            model="quad", rotation = (180,0,0), collider="box", ignore=True, position=(x,y,-0.5), texture="img/texture/1.jpg"
        )
#   # # #   # ###   ##  #   #
# # # # ##  # #  # #  # # # #
## ## # # # # #  # #  # ## ##
## ## # #  ## #  # #  # ## ##
#   # # #   # ###   ##  #   #
for x in range(19):
    for y in range(5):
        Entity(
            model="quad", rotation = (180,0,0), collider="box", ignore=True, position=(x,y,-0.5), texture="img/texture/glas.png"
        )
#   # # #   # ###   ##  #   #
# # # # ##  # #  # #  # # # #
## ## # # # # #  # #  # ## ##
## ## # #  ## #  # #  # ## ##
#   # # #   # ###   ##  #   #        
for z in range(10):
    for y in range(5):
        Entity(
            model="quad", rotation = (0,90,0), collider="box", ignore=True, position=(18.5,y,z), texture="img/texture/glas.png"
        )

sky = sky()
player = FirstPersonController()
app.run()