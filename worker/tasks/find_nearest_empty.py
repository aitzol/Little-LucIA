import math
import random

from lux.constants import Constants

from bh_trees import Task


class FindNearestEmpty(Task):

    DIRECTIONS = [
            Constants.DIRECTIONS.NORTH,
            Constants.DIRECTIONS.EAST,
            Constants.DIRECTIONS.SOUTH,
            Constants.DIRECTIONS.WEST,
        ]

    def __init__(self):
        super(FindNearestEmpty, self).__init__()


    def run(self):
        object = self._blackboard.get_value('object')
        player = self._blackboard.get_value('player')
        game_map = self._blackboard.get_value('map')
        width = self._blackboard.get_value('width')
        height = self._blackboard.get_value('height')

        random.shuffle(self.DIRECTIONS)
        for dir in self.DIRECTIONS:
            pos = object.pos.translate(dir,1)
            if pos.x>=0 and pos.y>=0 and pos.x<width and pos.y<height:
                cell = game_map.get_cell_by_pos(pos)
                if cell.resource is None and cell.citytile is None:
                    if pos:
                        self._blackboard.set_values(position = pos)
                        return True

        return False
