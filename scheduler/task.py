class Task(object):
    def __init__(self, index, duration, dependencies):
        self.id          = index
        self.duration    = int(duration)
        self.depends_on  = list(map(int, dependencies))
        self.depended_by = []
        self.start_time  = None
        self.end_time    = None

    def assign(self, min_start_time):
        self.start_time = max(min_start_time, self.dependencies_end_time())
        self.end_time   = self.start_time + self.duration

    def dependencies_end_time(self):
        return max([dep.end_time for dep in self.depends_on]) if self.depends_on else 0

    def shortstr(self):
        return "T{}:{}".format(self.id, self.duration)

    def __str__(self):
        return "<Task-{}:duration={}:deps_on={}:dep_by:{}>".format(self.id, self.duration, [t.id for t in self.depends_on], [t.id for t in self.depended_by])

    def __repr__(self):
        return self.__str__()
