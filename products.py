import os
#讀寫檔案
def read_file(filename):
    if os.path.isfile(filename):
        products = []
        with open(filename, 'r', encoding='utf-8')as d:
            for line in d:
                if '商品,價格' in line:
                    continue
                name, price = line.strip('\n').split(',')
                products.append([name, price])
        return products
#輸入購買紀錄
def input_(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入價格')
        price = int(price)
        products.append([name ,price])
    return products
#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8')as f: 
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file('products.csv')
products = input_(products)
write_file('products.csv', products)                           
            

                



