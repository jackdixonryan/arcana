from classes import object, action
create = object.Object

stool = create('Barstool', 'good for thinking', {}, False, False, True, '◉', None)
booth = create('Booth', 'A diner vibe', {}, False, False, True, '◨', None)
table = create('Table', 'I put things on that', {}, True, False, False, '▢', [])
counter = create('Counter', 'Lean on me', {}, True, False, False, '▢', [])
chat_up = action.create_action("Chat Up", "skilling", "linguistics", 2.5)
hologram = create("Hologram", "It wants to talk", { 'chat_up': chat_up }, False, True, False, '⏀', None)
