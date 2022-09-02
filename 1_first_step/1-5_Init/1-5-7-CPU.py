class CPU:
    def __init__(self, name, freq):
        self.name = name
        self.fr = freq


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mems
        self.total_mem_slots = 4

    def get_config(self):
        return [f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]


mb = MotherBoard('intel',CPU('pentium 4', '3.0'), Memory('kingston', 1024), Memory('Kitai', 2048))
mb.get_config()

