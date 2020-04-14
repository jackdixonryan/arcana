def summarize_inventory(inventory):
    inventory_summary = []
    for item_name, item_description in inventory:
        for summary in inventory_summary:
            if item_name == summary['name']:
                summary['amount'] += 1
            else:
                new_item = {
                    'name': item_name,
                    'amount': 1
                }
                inventory_summary.append(new_item)

    for final_summary in inventory_summary:
        print(final_summary)


