from classes import npc
from classes import interaction
from items.weapons import rusty_lever

name = 'Shady Dock Worker'
description = 'He doesn\'t seem very friendly.'
species = 'Sojourner'
inventory = [rusty_lever]
attack = 2.5
defense = 2.5
attitude = 0
greet_responses = [{'text': 'Shove off, mate, I\'m busy.', 'attitude_threshold': 0},
                   {'text': 'Gotta move boxes, it\'s all part of the job.', 'attitude_threshold': 2},
                   {'text': 'Hey, mate. Long day, right?', 'attitude_threshold': 4}]
# should increment attitude by one
greet_effects = [{'attitude': 1}]
threaten_responses = [
                         {
                             'text': 'Excuse me?',
                             'attitude_threshold': 0
                         },
                         {
                             'text': 'Say that again an\' I\'ll bash your head in with a hammer.',
                             'attitude_threshold': -6
                         },
                         {
                             'text': 'You ain\'t got the nerve.',
                             'attitude_threshold': -4
                         }
                      ]
threaten_effects = [{'attitude': -2}]
question_responses = [{'text': 'I see a lot of nasty things, mate, you\'re one of them. Now piss off.', 'attitude_threshold': 0}]
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



