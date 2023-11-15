while True:
    ans = input("Действие с бд:\n1.Добавить задачу\n2.Удалить задачу\n3.Посмотреть задачи\n")
    while True:
        if 1 <= int(ans) <= 3:
            break
        ans = input()
    if int(ans) == 1:
        pass
    elif int(ans) == 2:
        pass
    elif int(ans) == 3:
        pass
    else:
        pass