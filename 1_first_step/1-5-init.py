class CPU:
    def __init__(self, name, freq):
        self.name = name
        self.fr = freq


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, total_mem_slots=4, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        list_pk = []
        str = f"""Материнская плата: {self.name}', 'Центральный процессор: {self.cpu.name}, {self.cpu.fr}', 'Слотов памяти: {self.total_mem_slots}', 'Память: {self.mem_slots[0].name} - {self.mem_slots[0].volume};"""
        if len(self.mem_slots) < self.total_mem_slots:
            self.total_mem_slots = len(self.mem_slots)
        for i in range(1, self.total_mem_slots):
            if i != self.total_mem_slots:
                str += f' {self.mem_slots[i].name} - {self.mem_slots[i].volume}';
            else:
                str += f' {self.mem_slots[i].name} - {self.mem_slots[i].volume}'
        list_pk.append(str)
        print(list_pk)


cpu = CPU('pentium 4', '3.0')
mem_slots = [Memory('kingston', '2gb'), Memory('Kitai', '4gb')]
mb = MotherBoard('kin-dza-dza', cpu, mem_slots, 2)
mb.get_config()
