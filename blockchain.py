import json
import os 
import hashlib
blockchain_dir = os.curdir + '/test/'
block_name= []


def get_files():
    files = os.listdir(blockchain_dir)

    if files[0] == '1.txt': #if it opened on whindows
        for name_file in range(0, len(files)):

            files_range = files[name_file].split(".")
            names = block_name.append(files_range[0])
        names = set(block_name)
    if files[0] == '1': # if it opened on linux
        names = files
    return sorted([int(i) for i in names])


def get_hash(file_name):
    
    file = open(blockchain_dir + f'{file_name}.txt', "rb").read()
    return  hashlib.md5(file).hexdigest()


def write_block(amount, from_name, to_name, prev_hash= ""):
    files = get_files()
    file_list_last =  files[-1]
    filename = str(file_list_last + 1)
    prev_hash = get_hash(str(file_list_last))
    data = {"from": from_name,
            "to": to_name,
            "amount": amount,
            "hash": prev_hash,}

    with open(blockchain_dir + f'{filename}.txt', "w") as file:
        json.dump(data, file, indent=4, ensure_ascii = False)
    check_integrition()

def check_integrition():
    files = get_files()
    result = []
    for file in files[1:]:
        f = open(blockchain_dir + str (f"{file}.txt"))
        prev_file = f"{file - 1}" 
        file = f"{file}.txt"
        h = json.load(open(blockchain_dir + str(file)))["hash"]
        actual_hash = get_hash(prev_file)
        if h == actual_hash:
            res= "Ok"
        else:
            res = "Corrupted"
        result.append({"block" : prev_file,  "result" : res})

    return result

