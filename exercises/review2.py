test_dict: dict[str, int] = {}
test_dict["a"] = 1
test_dict["b"] = 2
test_dict["c"] = 3
print(test_dict)

if "a" in test_dict:
    print("true")
else:
    print("false")

a: bool = "k" in test_dict

print(a)

