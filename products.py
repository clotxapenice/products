#讀寫檔案
products = []
with open('products.csv', 'r', encoding='utf-8')as d:
    for line in d:
        if '商品,價格' in line:
            continue
        name, price = line.strip('\n').split(',')
        products.append([name, price])
#購買紀錄
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
       break
    price = input('請輸入價格')
    products.append([name ,price])
#寫入檔案
with open('products.csv', 'w', encoding='utf-8')as f: 
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
            
            

                



