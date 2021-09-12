from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

from little_lucia import LittleLucIA

game_state = None

def agent(observation, configuration):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player

    else:
        game_state._update(observation["updates"])

    ### AI Code goes down here! ###
    actions = LittleLucIA().play(game_state, observation)

    return actions
