## Упражнение 3
# С помощью какой операции можно заменить последний элемент кортежа tpl = (1, 2, 3) на 4?

#В Python кортежи неизменяемы, однако можно создать новый кортеж, и на экран выведется последний созданный кортеж:
tpl = (1, 2, 3)
tpl = (1, 2, 4)
print(tpl)

#Если нужно изменить последний элемент, то лучше создать список.