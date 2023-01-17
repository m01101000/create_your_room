# create_your_room
get to know the ursina engine by building your own three-dimensional space

***

## Try it, you might be able to design your dream room. ##

***

### Requirements: ###
- python 3.9.10
- ursina engine (https://www.ursinaengine.org/cheat_sheet_dark.html)

Install python from https://www.python.org/downloads/release/python-3910/.

Install ursina engine:

    pip install ursina

***

### Run the program ###
Open cmd.exe and navigate to your python_gallery folder.

Enter

    python room.py

to execute the program.

***

### Add any 3d object ###
To insert a tree-dimensional object, place the file obj file in the sample.obj files directory.

Add
    
    object1=Entity(
    model="sample.obj", scale=1, y=1, z=1, position=(5,5,5), color=color.blue
    )

and replace sample.obj with the name of the object you want to insert.
***
|| Your room could look like this |
|------------------------------|-|
|![room1](https://user-images.githubusercontent.com/96919599/152256617-a48f12b8-824f-4e87-9829-10f33ccd5357.png)|![room](https://user-images.githubusercontent.com/96919599/152256436-6153668b-0a45-4aaa-9615-8b9623896fd2.jpg)|
