# coding=utf-8
from classes import Node, Option

nodes = \
    Node("root").add_children(
        Node("node a").add_children(
            Option("option a", "echo 'Message for selecting option 1'"),
        ).add_children(
            Option("option b", "pwd")
        ),
        Option("option z", "echo '42 - Answer to the Ultimate Question of Life, the Universe, and Everything'"),
        Node("node b").add_children(
            Node("node c", collapsed=True).add_children(
                Option("option c", "echo \"Hello $USER!\""),
                Option("option d", "echo '( ͡° ͜ʖ ͡°)'")
            ),
            Option("option f", "echo 'blah'"),
            Node("node d").add_children(
                Option("option e", "echo 'sudo rm -rf /'")
            ),
            Node("empty")
        ),
        Option("option g", "gg")
    )