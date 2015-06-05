import libtcodpy as libtcod
import data.properties

#SCREEN DEMENTIONS
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50



#Characters and objects
player = Object(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, 'P', libtcod.red, 0)
objects = [player]

#Init and Mainloop
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roague', False)#Init the root console
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#Load up a font
while not libtcod.console_is_window_closed():
    #Loop through the objects and draw them
    for object in objects:
        object.draw_object()
    
    
    libtcod.console_flush()

    for object in objects:
        object.delete()
