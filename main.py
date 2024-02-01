from datetime import datetime
import json


# ================== 1 ==================
class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def cls_method(cls, value):
        pass

    def method(self):
        pass


# ================== 2 ==================


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.a = b
        self.b = self.cls_method(a)
        self.c = c

    @classmethod
    def cls_method(cls, value):
        return value * 4

    def method(self):
        print(self.a, self.b, self.c)

instance = B(1, 2, 3)
instance.method()

# ================== 3 ==================

integer_list = [1, 2, 3, 4]

filter_odd = lambda x: x % 2 != 0

even_list = [x for x in integer_list if filter_odd(x)]

print(even_list)

# ================== 4 ==================

dl = [{"x": 1}, {"x": 2}, {"x": 3}, {"x": 4}, {"x": 5}, {"x": 6}]


def get_five(dl):
    return next((i for i in dl if i["x"] == 5), {})


print(get_five(dl))

# ================== 5 ==================

with open("file.json", "r") as f:
    file = json.load(f)

print(file.get("payee", {}).get("id", ""))

print([inv for inv in file.get("invoiceIds", []) if "583" in inv])

for k, v in file.items():
    if "DateTime" in k:
        file[k] = datetime.strftime(datetime.fromtimestamp(v / 1000), "%Y-%m-%dT%H:%M:%S")

with open("new_file.json", "w") as f:
    json.dump(file, f, indent=4)
