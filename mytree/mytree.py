from .tree_generator import _TreeGenerator
from .tree_output import _TreeOutputScreen


class GeneratorFactory(object):

    def __init__(self):
        self._generators = {}

    def register_generator(self, gen_name, generator):
        self._generators[gen_name] = generator

    def create_generator(self, gen_name, **kwargs):
        generator = self._generators.get(gen_name)
        if not generator:
            raise ValueError(gen_name)
        return generator(**kwargs)


class OutputFactory(object):

    def __init__(self):
        self.__outputs = {}

    def register_output(self, output_name, output):
        self.__outputs[output_name] = output

    def create_output(self, output_name, **kwargs):
        output = self.__outputs.get(output_name)
        if not output_name:
            raise ValueError(output_name)
        return output(**kwargs)


gen_factory = GeneratorFactory()
gen_factory.register_generator('DEFAULT', _TreeGenerator)

output_factory = OutputFactory()
output_factory.register_output('SCREEN', _TreeOutputScreen)


class DirectoryTree(object):
    def __init__(self, root_dir, generator='DEFAULT', output='SCREEN'):
        self.generator = gen_factory.create_generator(generator, root_dir=root_dir)
        self.output = output_factory.create_output(output, tree_list=[])
