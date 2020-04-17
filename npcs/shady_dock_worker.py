from classes import npc
from classes import interaction

name = 'Shady Dock Worker'
description = 'He doesn\'t seem very friendly.'
species = 'Sojourner'
inventory = []
attack = 2.5
defense = 2.5
attitude = 0
greet_responses = ['Shove off, mate, I\'m busy.',
                   'Gotta move boxes, it\'s all part of the job.',
                   'Don\'t you have somewhere else to be?']
# should increment attitude by one
greet_effects = [{'attitude': 1}]
threaten_responses = ['Excuse me?',
                      'Say that again an\' I\'ll bash your head in with a hammer.',
                      'You ain\'t got the nerve.'],
threaten_effects = [{'attitude': -2}]
question_responses = ['I see a lot of nasty things, mate, you\'re one of them. Now piss off.']
question_effects = [{'attitude': -2}]
greet = interaction.Interaction('greet', greet_responses, greet_effects)
threaten = interaction.Interaction('threaten', threaten_responses, threaten_effects)
question = interaction.Interaction('question', question_responses, question_effects)
npc_interactions = {
    'greet': greet,
    'threaten': threaten,
    'question': question
}

shady_dock_worker = npc.NPC(name,
                            description,
                            species,
                            inventory,
                            attack,
                            defense,
                            attitude,
                            npc_interactions)

shady_dock_worker.interact('threaten')
shady_dock_worker.interact('threaten')

