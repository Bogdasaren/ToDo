from BD import create_todo_table, add_task, get_all_tasks

create_todo_table()

def add_task_interface():
    title = input('Введите заголовок задачи: ')
    description = input('Введите описание задачи: ')
    add_task(title, description)
    print('Задача добавлена успешно!')

def show_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print('Список задач пуст.')
    else:
        print('Список задач:')
        for task in tasks:
            print(f'{task[0]}. {task[1]} - {task[3]}')

if __name__ == '__main__':
    while True:
        print('\nМеню:')
        print('1. Добавить задачу')
        print('2. Показать задачи')
        print('3. Выход')
        choice = input('Выберите действие (1/2/3): ')

        if choice == '1':
            add_task_interface()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            print('Выход из программы.')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')