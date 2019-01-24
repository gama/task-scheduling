import sys
import io
import scheduler


class Scheduler(object):
    @classmethod
    def schedule(cls, tasks, num_processors):
        processors = cls._assign(tasks, num_processors)
        return Schedule(processors)

    @classmethod
    def _assign(cls, tasks, num_processors):
        # variation of topological sort algorithm
        processors      = [scheduler.Processor() for _ in range(num_processors)]
        depends_on_map  = {task: len(task.depends_on) for task in tasks if len(task.depends_on) > 0}
        no_dependencies = [task for task in tasks if len(task.depends_on) == 0]

        while no_dependencies:
            task      = no_dependencies.pop()
            processor = cls._select_processor(processors, task)
            processor.assign(task)

            for next_task in task.depended_by:
                depends_on_map[next_task] -= 1
                if depends_on_map[next_task] == 0:
                    no_dependencies.append(next_task)
                    del depends_on_map[next_task]

        if depends_on_map:
            raise scheduler.InfeasibleError('graph has cycle')

        return processors

    @classmethod
    def _select_processor(cls, processors, task):
        # select processor which will be available as close as possible to the
        # time the last dependencie will be done
        min_start_time = task.dependencies_end_time()
        processors     = sorted(processors, key=lambda processor: abs(processor.available_at - min_start_time))
        return processors[0]


class Schedule(object):
    def __init__(self, processors):
        self.processors = processors

    def print(self, file=sys.stdout):
        if scheduler.debug:
            print('Schedule:')
        for processor in self.processors:
            for task in processor.tasks:
                if scheduler.debug:
                    print('T{}:{}:{}'.format(task.id, task.duration, task.start_time), end='  ', file=file)
                else:
                    print(task.id, task.start_time, end=' ', file=file)
            print(file=file)

    def serialize(self):
        sio = io.StringIO()
        self.print(file=sio)
        return sio.getvalue()
