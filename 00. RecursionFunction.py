def function(n):
    if(n > 0):
        print("Samith", n)
        function(n-1)
        print("After Function call of", n)
        # print("After Function call of", n-1)


if __name__ == '__main__':
    function(3)
