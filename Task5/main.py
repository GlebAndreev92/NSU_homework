from matplotlib import pyplot as plt
import itertools
import collections
import random

circular_buffer = collections.deque(maxlen=300)  # объявление кругового буфера длинной 300

window = 5  # Задаём ширину окна

for i in range(circular_buffer.maxlen):
    circular_buffer.append(random.uniform(0, circular_buffer.maxlen))  # Заполнение буфера рандомными значениями


def win_fil(circular_buffer, read_position, write_position, window_size
            , res_read_position=None, res_write_position=None, cb_size=None, res_cb_size=None):
    """
    Функция сравнивает позицию чтения и позицию записи
    """
    res_circular_buffer = collections.deque(maxlen=300 - window_size)

    while (read_position - window_size) >= write_position:
        buffer = list(itertools.islice(circular_buffer, write_position, write_position + window_size))
        write_position += 1
        fill_buffer(buffer, res_circular_buffer, aver)

    return res_circular_buffer


def append_buffer(value, buffer):
    """
    Функция добавляет усредненный элемент
    """
    buffer.append(value)
    return buffer


def fill_buffer(in_buf, out_buf, func):
    """
        Функция передаёт данные для вычисления среднего значения после чего получает это значение и записывает его
        в выходной буфер
    """
    aver_value = func(in_buf)
    append_buffer(aver_value, out_buf)
    return out_buf


def aver(list):
    """
        функция вычисления среднего значения по отношению суммы всех значений
        """
    a = len(list)
    avg = sum(list) / len(list)
    return avg


res_buf = win_fil(circular_buffer, len(circular_buffer), 0, window)

cb_size = len(circular_buffer)
rsb_size = len(res_buf)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(list(range(1, cb_size + 1)), circular_buffer, label='Входные данные')
ax2.plot(list(range(1, rsb_size + 1)), res_buf, label='Выходные данные')
ax1.legend()
ax2.legend()
plt.show()
