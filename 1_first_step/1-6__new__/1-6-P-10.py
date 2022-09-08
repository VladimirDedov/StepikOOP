
class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        st=string.strip()
        return float(st)

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)
        return seq


# эти строчки не менять!
ld = Loader()

res = ld.parse_format("4, 5, -6.5", Factory())
print(res)