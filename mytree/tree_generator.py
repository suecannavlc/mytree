PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class TreeGenerator(object):

    def __init__(self, root_dir, **opt):
        self._root_dir = root_dir

    def generate(self):
        """
        Generates a list with the directory contents
        :return: list
        """
        pass
