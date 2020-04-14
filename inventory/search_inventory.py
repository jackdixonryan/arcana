def search_inventory(term, inventory):
    for item in inventory:
        if item['name'] == term:
            return item
    else:
        return ''
