car = {  
    "name":"Ferrari",
    "color":"red",
    "year":"2013"
}

def remove_car_info():
    print(car)
    remove_int = input("Qaysi malumotni o'chirmoqchisiz = ")
    if remove_int in car:
        del car[remove_int]
        print(f"\n{remove_int} malumotlar bazasidan muvaqqaqiyatli o'chirildi.\n")
        print(car)
    else:
        print("Bu malumot malumotlar bazasida mavjud emas ! ")
        remove_car_info()

remove_car_info()