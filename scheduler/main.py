import fileinput
from scheduler import Parser, Scheduler, InfeasibleError, debug


def main():
    lines = [line for line in fileinput.input()]
    tasks, num_processors = Parser.parse(''.join(lines))   # TODO: change 'parse' to handle lists
    try:
        if debug:
            print('Tasks:\n', '\n'.join(map(str, tasks)), '\n', sep='')
        task_schedule = Scheduler.schedule(tasks, num_processors)
        task_schedule.print()
    except InfeasibleError:
        print('infeasible')
