class _TreeOutputScreen(object):
    def __init__(self, **kwargs):
        for item in kwargs.get('tree_list'):
            print(item)
