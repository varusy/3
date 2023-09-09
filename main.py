my_list = [int(x) for x in input().split()]
x = my_list[0]
y = my_list[1]
z = my_list[2]
if x > 0:
    if y > 0:
        if z > 0:
            print('1 четверть')
        elif z < 0:
            print('5 четверть')
        else:
          print('Точка между 1 и 5 четвертями')
    elif y < 0:
        if z > 0:
          print('4 четверть')
        elif z < 0:
            print('8 четверть')
        else:
          print('Точка между 4 и 8 четвертями')
    else:
      if z == 0:
        print('Ось x')
      elif z > 0:
        print('Точка между 1 и 4 четвертями')
      else:
        print('Точка между 5 и 8 четвертями')

elif x < 0:
    if y > 0:
        if z > 0:
          print('2 четверть')
        elif z < 0:
          print('6 четверть')
        else:
          print('Точка между 2 и 6 четвертями')
    elif y < 0:
        if z > 0:
          print('3 четверть')
        elif z < 0:
            print('7 четверть')
        else:
          print('Точка между 3 и 7 четвертями')
    else:
      if z == 0:
        print('Ось x')
      elif z > 0:
        print('Точка между 2 и 3 четвертями')
      else:
        print('Точка между 6 и 7 четвертями')

else:
    if y == 0:
      print('Ось z')
    elif y > 0:
      if z == 0:
        print('Ocь y')
      elif z > 0:
        print('Точка между 1 и 2 четвертями')
      else:
        print('Точка между 5 и 6 четвертями')
    else:
      if z == 0:
        print('Ocь y')
      elif z > 0:
        print('Точка между 3 и 4 четвертями')
      else:
        print('Точка между 7 и 8 четвертями')
