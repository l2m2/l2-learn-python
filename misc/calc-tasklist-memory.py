import re

def run(filename):
    with open(filename, encoding='utf-8') as f:
        k = sum([ int(re.sub(r',', '', re.split( r'\s+', line.rstrip())[-2])) for line in f ])
        g = k / 1024 / 1024
        return g

if __name__ == "__main__":
    usage = run("tasklist.txt")
    print(f"Memory Usage: {usage} G")