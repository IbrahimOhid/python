# def my_fun():
#     for i in range(1, 11):
#         print(i)
# my_fun();

# def my_fun(n):
#     print(n)
#     my_fun(n + 1)
# my_fun(1);

def fun(n):
    if n > 10:
        return
    print(n)
    fun(n + 1)
fun(1)