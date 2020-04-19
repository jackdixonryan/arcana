from layout.generate_base_text_display import generate_dialog_box


class Interaction:
    def __init__(self,
                 name: str,
                 responses: list,
                 effects: list):
        self.name = name
        self.responses = responses
        self.effects = effects

    # takes parent attitude into account before giving a response
    def get_response(self, npc_attitude, npc_name):
        if npc_attitude >= 0:
            current_response = self.responses[0]
            for response in self.responses:
                if current_response['attitude_threshold'] < response['attitude_threshold'] < npc_attitude:
                    current_response = response
            dialog = generate_dialog_box(npc_name, current_response['text'])
            print(dialog)
            return dialog
        elif npc_attitude < 0:
            current_response = self.responses[0]
            for response in self.responses:
                if current_response['attitude_threshold'] > response['attitude_threshold'] > npc_attitude:
                    current_response = response
            dialog = generate_dialog_box(npc_name, current_response['text'])
            print(dialog)
            return dialog
