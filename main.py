from classes import *
from random import randint

nodes = \
    Node("root").add_children(
        Node("node a").add_children(
            Option("option a", "echo 'Message for selecting option 1'"),
        ).add_children(
            Option("option b", "pwd")
        ),
        Option("option z", "echo \"" + str(randint(0, 100)) + "\""),
        Node("node b").add_children(
            Node("node c").add_children(
                Option("option c", "echo \"Hello $USER!\""),
                Option("option d", "echo '( ͡° ͜ʖ ͡°)'")
            ),
            Option("option f", "echo 'blah'"),
            Node("node d").add_children(
                Option("option e", "echo 'sudo rm -rf /'")
            )
        ),
        Option("option g", "gg")
    )

help_text = \
    """press any key to continue
    
      UP/DOWN     navigate between adjacent selectables 
      LEFT/RIGHT  navigate between nodes
      RETURN      select option
    
      ^C          exit
    """
helping = False

# what i'd like:
#
# node
# ├── node
# │   └── option
# └── option
def display():
    clear()
    print("Press h for help\n")
    if Selectable.selected == 0:
        print(C.BOLD + C.B.BLUE + nodes.name + C.END)
    else:
        print(C.BOLD + C.F.BLUE + nodes.name + C.END)
    nodes.display()

def main():
    global helping
    os.system('setterm -cursor off')

    display()

    while True:
        char = GetCh()
        while True:
            key = char()
            if key != '':
                break


        if key == Key.CTRL_C:
            clear()
            break

        elif key == 'h':
            clear()
            helping = not helping
            if helping:
                print(help_text)
            else:
                display()

        elif key == Key.UP:
            Selectable.selected = max(0, min(Selectable.selected - 1, Selectable.iterator - 1))
            display()

        elif key == Key.DOWN:
            Selectable.selected = max(0, min(Selectable.selected + 1, Selectable.iterator - 1))
            display()

        elif key == Key.RIGHT:
            tmp = Selectable.selected
            Selectable.selected = max(0, min(Selectable.selected + 1, Selectable.iterator - 1))
            while nodes.find(Selectable.selected).__class__.__name__ != "Node":
                Selectable.selected = max(0, min(Selectable.selected + 1, Selectable.iterator - 1))
                if Selectable.selected == Selectable.iterator - 1:
                    Selectable.selected = tmp
                    break
            display()

        elif key == Key.LEFT:
            Selectable.selected = max(0, min(Selectable.selected - 1, Selectable.iterator - 1))
            while nodes.find(Selectable.selected).__class__.__name__ != "Node":
                Selectable.selected = max(0, min(Selectable.selected - 1, Selectable.iterator - 1))
            display()

        elif key == Key.RETURN:
            sel = nodes.find(Selectable.selected)
            if sel.__class__.__name__ == "Option":
                clear()
                sel.run()
                break

    os.system('setterm -cursor on')

main()