# coding=utf-8
import sys, tty, termios, os

class C: # Color
    END =       '\x1b[0m'
    BOLD =      '\x1b[1m'
    ITALIC =    '\x1b[3m'
    UNDERLINE = '\x1b[4m'

    class F: # Foreground
        BLACK =  '\x1b[30m'
        RED =    '\x1b[31m'
        GREEN =  '\x1b[32m'
        YELLOW = '\x1b[33m'
        BLUE =   '\x1b[34m'
        PURPLE = '\x1b[35m'
        CYAN =   '\x1b[36m'
        WHITE =  '\x1b[37m'

    class B: # Background
        BLACK =  '\x1b[40m'
        RED =    '\x1b[41m'
        GREEN =  '\x1b[42m'
        YELLOW = '\x1b[43m'
        BLUE =   '\x1b[44m'
        PURPLE = '\x1b[45m'
        CYAN =   '\x1b[46m'
        WHITE =  '\x1b[47m'

class Key: # Keycodes for things
    UP = '\x1b[A'
    DOWN = '\x1b[B'
    RIGHT = '\x1b[C'
    LEFT = '\x1b[D'
    CTRL_C = chr(3)
    RETURN = chr(13)
    ESCAPE = chr(27)

class GetCh:
    # Gets a single character from standard input.  Does not echo to the screen.
    def __init__(self):
        self.impl = _GetChUnix()

    def __call__(self):
        char_list = []
        for i in range(3):
            try:
                char_list.append(self.impl())
            finally:
                pass

            if char_list[i] not in [Key.ESCAPE, '[']:
                break

            if len(char_list) > 1:
                if char_list == [Key.ESCAPE, Key.ESCAPE]:
                    break

        if len(char_list) == 3:
            print(char_list[2])
            if char_list[2] == 'A':
                return Key.UP

            elif char_list[2] == 'B':
                return Key.DOWN

            elif char_list[2] == 'C':
                return Key.RIGHT

            elif char_list[2] == 'D':
                return Key.LEFT

        elif len(char_list) == 2 and char_list == [Key.ESCAPE, Key.ESCAPE]:
                return Key.ESCAPE

        elif len(char_list) == 1:
            return char_list[0]

        return ''

class _GetChUnix:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

class Selectable(object):
    selected = 0
    iterator = 0
    def __init__(self, name):
        self.name = name
        self.id = Selectable.iterator
        Selectable.iterator += 1


class Node(Selectable):
    def __init__(self, name, collapsed=False):
        super(Node, self).__init__(name)
        self.children = []
        self.collapsed = collapsed

    def add_children(self, *args):
        for i in range(len(args)):
            child = args[i]
            if not issubclass(child.__class__, Selectable):
                raise TypeError("Node.add_children() arg " + str(i) + " must be a subclass of class Select")

            self.children.append(child)

        return self # For chaining

    def display(self, level=1):
        if self.collapsed:
            return

        for i in range(len(self.children)):
            child = self.children[i]
            if child.__class__.__name__ == "Node" and len(child.children) > 0:
                print("  " * (level - 1) + ("▸" if child.collapsed else "▾") + " " + C.BOLD + (C.F.BLUE if Selectable.selected != child.id else C.B.BLUE) + child.name + C.END)

            child.display(level=level + 1)

    def find(self, id):
        if self.id == id:
            return self

        for child in self.children:
            if child.id == id:
                return child

            if child.__class__.__name__ == "Node" and len(child.children) > 0:
                result = child.find(id)
                if result is not None:
                    return result

        return None

    def collapse(self):
        if self.id != 0:
            self.collapsed = not self.collapsed


class Option(Selectable):
    def __init__(self, name, command):
        super(Option, self).__init__(name)
        self.command = command

    def run(self):
        os.system(self.command)

    def display(self, level=1):
        print("  " * (level - 1) + (C.F.BLACK + C.B.WHITE if Selectable.selected == self.id else "") + self.name + C.END)


def clear():
    os.system("clear")