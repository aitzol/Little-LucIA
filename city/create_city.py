from .tasks import CanAct
from .tasks import Research
from .tasks import BuildWorker
from .tasks import IsResourceResearched

from bh_trees import recursive_build
from bh_trees import Inverter, Sequence, Selector


def create_simple_city():

    graph = {
        Sequence(): {
            Sequence(): {
                CanAct(): {}
                },
            Selector(): {
                BuildWorker(): {},
                Sequence(): {
                    Inverter(): {
                        IsResourceResearched(): {}
                        },
                    Research(): {}
                    }
                }
            }
        }

    return recursive_build(graph)
