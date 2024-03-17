def even_generator(n):
    for i in range(2, n+1, 2):
        yield i

def main():
    for i in even_generator(20):
        print(i)

main()