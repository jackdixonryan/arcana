

class Interaction:
    def __init__(self,
                 name: str,
                 responses: list,
                 effects: list):
        self.name = name
        self.responses = responses
        self.effects = effects

    # takes parent attitude into account before giving a response
    def get_response(self, npc_attitude):
        print("running response getter...")
        if npc_attitude >= 0:
            print('npc attitude is positive')
            current_response = self.responses[0]
            for response in self.responses:
                if current_response['attitude_threshold'] < response['attitude_threshold'] < npc_attitude:
                    current_response = response
            print(current_response['text'])
            return(current_response['text'])
        elif npc_attitude < 0:
            print('npc attitude is not positive')
            current_response = self.responses[0]
            for response in self.responses:
                if current_response['attitude_threshold'] > response['attitude_threshold'] > npc_attitude:
                    current_response = response
            print(current_response['text'])
            return current_response['text']
