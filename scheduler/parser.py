from scheduler.task import Task


class Parser(object):
    @classmethod
    def parse(cls, input_string):
        lines = input_string.strip().split('\n')
        ntasks, nprocessors = lines.pop(0).strip().split(' ')
        assert int(ntasks) == len(lines)
        tasks = list(map(lambda x: cls._parse_line(*x), enumerate(lines)))
        cls._resolve_references(tasks)
        return tasks, int(nprocessors)

    @staticmethod
    def _parse_line(index, line):
        duration, *depends_on = line.strip().split(' ')
        return Task(index, duration, depends_on)

    @staticmethod
    def _resolve_references(tasks):
        for idx, task in enumerate(tasks):
            for dependency_idx in task.depends_on:
                tasks[dependency_idx].depended_by.append(task)
            task.depends_on = list(map(lambda idx: tasks[idx], task.depends_on))
