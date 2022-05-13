PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class _TreeGenerator(object):

    def __init__(self, **kwargs):
        self._root_dir = kwargs.get('root_dir')

    def generate(self):
        """
        Generates a list with the directory contents
        :return: list
        """
        print('generating')
