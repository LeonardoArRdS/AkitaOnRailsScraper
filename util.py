import json

def read_lines(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read().splitlines()

def read_file(file_path):
    with open(file_path) as f:
        return f.read()
        
def read_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

def append_file(file_path, line):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(line  + "\n")