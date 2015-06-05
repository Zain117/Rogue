import libtcodpy as libtcod
class Object():
    def __init__(self, x, y, char, color, screen):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.screen = screen


    def draw_object(self):
        #Set the color of the character and draw it
        libtcod.console_set_default_foreground(self.screen, self.color)
        libtcod.console_put_char(self.screen, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def delete(self):
        #Erase the char
        libtcod.console_put_char(self.screen, self.x, self.y, self.char, libtcod.BKGND_NONE)
        

    


class Tile():
    #Properties of a map's tiles, theres not much to it like there is to Object
    def __init__(self, blocked, blocked_sight):
        self.blocked = blocked
        self.blocked_sight = blocked_sight

        #blocked_sight's variable depends on blocked if its None
        if blocked_sight == None: blocked_sight = blocked
        

