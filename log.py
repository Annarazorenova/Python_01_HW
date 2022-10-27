def input_write(data: str):
    road = r'file.txt'
    with open(road,'a', encoding = 'UTF-8') as f:
        f.write(f'{data} \n')