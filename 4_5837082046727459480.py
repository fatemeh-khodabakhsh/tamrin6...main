class MrKrabs:
    def __init__(self, data):
        self.data = data + data[:min(len(data), 10)]

    def process_data(self):
        return self.data.replace("tt", "o")


class SpongeBob(MrKrabs):
    def __init__(self, data):
        super().__init__(data)

    def process_data(self):
        return self.merge_sort(str(len(self.data)))

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return ''.join(result)


class Octopus:
    def __init__(self, data):
        self.data = data
        self.preprocess()

    def preprocess(self):
        index = self.liner_search('x')
        if index != -1:
            self.data += str(index)

    def liner_search(self, target):
        for i in range(len(self.data)):
            if self.data[i] == target:
                return i
        return -1

    def process_data(self):
        i = 0
        while i < len(self.data) - 2:
            if self.data[i] == self.data[i + 1] == self.data[i + 2]:
                self.data = self.data[:i] + "(0_0)" + self.data[i + 3:]
                i += 3
            else:
                i += 1
        return self.data


s = input()
ss = s[::-1]

if s.startswith("m"):
    mr_krabs = MrKrabs(s)
    print(mr_krabs.process_data())

elif s.startswith("sb"):
    sponge_bob = SpongeBob(s)
    print(sponge_bob.process_data())

elif s.startswith("s") and s[1] != "b":
    octopus = Octopus(s)
    print(octopus.process_data())

elif ss.startswith("m"):
    mr_krabs = MrKrabs(ss)
    print(mr_krabs.process_data())

elif ss.startswith("sb"):
    sponge_bob = SpongeBob(ss)
    print(sponge_bob.process_data())

elif ss.startswith("s") and ss[1] != "b":
    octopus = Octopus(ss)
    print(octopus.process_data())

else:
    print("invalid input")
