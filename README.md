# Y2020
Решение 

Чтобы программа нормально запускалась нужно иметь установленными следующие библиотеки:
-random
-numpy
-time

Самое интересное из решение, в моем понимании, это использование рамки вокруг поля, чтобы не волноваться из-за углов поля при
расчете соседей. Если поле выглядит вот так:

       [1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 0.],
       [0., 0., 0., 0., 1.],
       [0., 1., 0., 0., 0.],
       [0., 1., 1., 1., 1.],
       [0., 0., 1., 0., 0.]
       
То с рамкой, в программе, она выглядит вот так:

       [0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 1., 1., 1., 1., 0.],
       [0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.]
       
numpy здесь пиятно помогает со скрытием рамки при выводе ее на консоль (можно слайсить grid[1:-1,1:-1]).

**Менять клетки "одновременно"**

Так как я обрабатываю клетки справа налево, важно чтобы ранее измененные клетки не влияли на последующие, я сначала создаю копию, и
использую ее для расчетов каждого поля.


**Проблема таймера:**
Чтобы удовлетворить условие по выводу каждую, я использую time.sleep(1). Технически, это работает только если весь остальной 
код занимает 0 секунд, что неправда. Но при адекватных размерах доски, это не должно быть заметно со стороны пользователя.
