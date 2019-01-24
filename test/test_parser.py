from scheduler.parser import Parser


def test_parser():
    input_string = "4 2\n"   \
                   "5\n"     \
                   "8 0\n"   \
                   "3 0\n"   \
                   "6 1 2\n" \

    tasks, num_processors = Parser.parse(input_string)

    assert num_processors                       == 2
    assert len(tasks)                           == 4
    assert _ids(tasks)                          == [0, 1, 2, 3]
    assert [t.duration for t in tasks]          == [5, 8, 3, 6]
    assert [_ids(t.depends_on) for t in tasks]  == [[], [0], [0], [1, 2]]
    assert [_ids(t.depended_by) for t in tasks] == [[1, 2], [3], [3], []]


def _ids(list):
    return [element.id for element in list]
