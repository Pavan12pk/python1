def check_memory(usage):
    if usage >75:
        return "Hisgh Memory Usage!"
    return "Memory is Normal"
print(check_memory(40))
