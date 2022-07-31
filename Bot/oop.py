class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Hello, класс {}'.format(cls.__name__))

# SomeClass.hello()

def creat_table(obj_name, tablename, column_name, column_info):
    obj_name = obj_name
    tablename = tablename
    column_name = column_name
    column_info = column_info
    return obj_name, tablename, column_name, column_info

print(creat_table("Aziz", "Laziz", "Xusen", "Xasan"))
