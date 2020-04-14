locations = [
    {
        'depot': {
            'description': 'Dingy, dank, and filled with boxes. Is this the last place they lived?',
            'options': [
                {
                    'text': 'Search the crates',
                    'outcome': 'You find an MRI!',
                    'programmable': fillInventory({
                        'name': 'MRI',
                        'type': 'consumable',
                        'amount': 10
                    })
                }
            ]
        }
    }
]