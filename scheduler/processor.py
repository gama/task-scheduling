class Processor(object):
    def __init__(self):
        self.tasks = []

    def assign(self, task):
        task.assign(self.available_at)
        self.tasks.append(task)

    @property
    def available_at(self):
        return self.tasks[-1].end_time if self.tasks else 0
