from typing import Optional
class Action:
    def __init__(self,
                 name: str,
                 action_type: str,
                 skill: Optional[str],
                 xp_per_tick: Optional[float],
                 ):
        self.name = name
        self.action_type = action_type
        self.skill = skill
        self.xp_per_tick = xp_per_tick

    # we need to use threads...
    def use(self, character):
        if self.action_type == "skilling":
            character.skills[self.skill] += self.xp_per_tick
        else:
            return None


def create_action(name, type, skill: Optional[str], xp: Optional[float]):
    return Action(name, type, skill, xp)

