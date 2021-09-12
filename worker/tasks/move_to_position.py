import random

from bh_trees import Task
from lux.constants import Constants


class MoveToPosition(Task):


    DIRECTIONS = [
            Constants.DIRECTIONS.NORTH,
            Constants.DIRECTIONS.EAST,
            Constants.DIRECTIONS.SOUTH,
            Constants.DIRECTIONS.WEST,
        ]

    def __init__(self):
        super(MoveToPosition, self).__init__()


    def run(self):

        object = self._blackboard.get_value('object')
        source_position = self._blackboard.get_value('object').pos
        target_position = self._blackboard.get_value('position')
        units_map = self._blackboard.get_value('units_map')
        direction = source_position.direction_to(target_position)

        random.shuffle(self.DIRECTIONS)
        for new_dir in self.DIRECTIONS:
            new_pos = source_position.translate(direction, 1)
            if units_map[new_pos.y][new_pos.x] is not None:
                direction = new_dir

        movement = object.move(direction)

        # If object in the position of interest then don't move
        if direction != Constants.DIRECTIONS.CENTER:
            self._blackboard.append_values(actions=movement)
            return True
        else:
            return False
