import pytest
from scheduler.parser     import Parser
from scheduler.scheduler  import Scheduler
from scheduler.exceptions import InfeasibleError


def test_same_duration_one_processor():
    schedule = schedule_from_file('test/input/same_duration_one_processor.txt')
    assert len(schedule.processors) == 1
    assert schedule.serialize() == '12 0 13 1 0 2 1 3 4 4 6 5 5 6 3 7 7 8 8 9 10 10 9 11 2 12 11 13 \n'


def test_same_duration_two_processors():
    schedule = schedule_from_file('test/input/same_duration_two_processors.txt')
    assert len(schedule.processors) == 2
    assert schedule.serialize() == '12 0 13 1 4 2 6 3 5 4 7 5 8 6 10 7 9 8 11 9 \n' \
                                   '0 0 1 1 3 2 2 3 \n'


def test_diff_duration_two_processors():
    schedule = schedule_from_file('test/input/diff_duration_two_processors.txt')
    assert len(schedule.processors) == 2
    assert schedule.serialize() == '12 0 13 5 3 12 7 20 8 22 10 27 9 31 11 40 \n' \
                                   '0 0 1 8 4 12 6 15 5 16 2 19 \n'


def test_diff_duration_many_processors():
    schedule = schedule_from_file('test/input/diff_duration_many_processors.txt')
    assert len(schedule.processors) == 5
    assert schedule.serialize() == '12 0 13 5 \n'                                         \
                                   '0 0 1 2 4 5 6 14 5 15 7 18 8 20 10 25 9 29 11 38 \n'  \
                                   '3 5 \n'                                               \
                                   '2 5 \n'                                               \
                                   '\n'


def test_graph_with_cycle():
    with pytest.raises(InfeasibleError):
        schedule_from_file('test/input/cycle.txt')


# TODO: add truly large input file, to validate performance
# def test_large_graph():
#     pass


def schedule_from_file(filename):
    with open(filename) as file:
        tasks, num_processors = Parser.parse(file.read())
    return Scheduler.schedule(tasks, num_processors)
