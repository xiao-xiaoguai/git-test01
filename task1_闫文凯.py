print("欢迎使用购物车管理系统")
print('''
##########购物车系统##########
#        1.添加购物车        #
#        2.修改购物车        #
#        3.删除购物车        #
#        4.查询购物车        #
#        5.退出购物车        #
############################
''')
shop_car={}
while True:
    choice = input("请选择要执行的操作（1-5）")
    match choice:
        case "1":
            good_name = input("请输入商品名称")
            good_price = float(input("请输入商品价格"))
            good_namber = int(input("请输入商品数量"))
            if good_name in shop_car:
                print("商品已存在，请重新选择")
            else:
                shop_car[good_name] = {"price": good_price, "namber": good_namber}
                print("商品添加完毕")
        case "2":
            good_name = input("请输入要修改的商品名称")
            if good_name not in shop_car:
                print("商品不存在，请重新选择")
            else:
                good_price = float(input("请重新输入商品价格"))
                good_namber = int(input("请重新输入商品数量"))
                shop_car[good_name] = {"price": good_price, "namber": good_namber}
                print("商品信息修改完毕")
        case "3":
            good_name = input("请输入要删除的商品名称")
            if good_name not in shop_car:
                print("商品不存在，请重新选择")
            else:
                del shop_car[good_name]
                print("商品已删除")
        case "4":
            for good_name in shop_car.keys():
                goods_info = shop_car[good_name]
                print(f"商品名称：{good_name},商品价格：{goods_info['price']},商品{goods_info['namber']}")
        case "5":
            break
        case _:
            print("非法操作，不支持")






































