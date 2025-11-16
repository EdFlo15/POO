class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None

    def __str__(self):
        return f"CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}"


class ComputerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        product = self.computer
        self.reset()   # prepare builder for next object
        return product


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return (
            self.builder
            .set_cpu("Intel i9")
            .set_gpu("Nvidia RTX 4090")
            .set_ram("32GB")
            .build()
        )

    def build_office_pc(self):
        return (
            self.builder
            .set_cpu("Intel i5")
            .set_gpu("Integrated Graphics")
            .set_ram("16GB")
            .build()
        )

builder = ComputerBuilder()
director = ComputerDirector(builder)

gaming_pc = director.build_gaming_pc()
office_pc = director.build_office_pc()

print("Gaming PC:", gaming_pc)
print("Office PC:", office_pc)

