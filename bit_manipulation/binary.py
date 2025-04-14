# binary conversion:
class binary:
    def binary(num):
        stack = []
        if  num == 0:
            return 0
        if num == 1:
            return 1
        if num<0: # store -ve num
            # Number of bits we want (e.g., 8-bit, 16-bit, etc.)
            # We can use Python's bit-length method to determine the number of bits for the absolute value.
            bit_length = num.bit_length()+1  # Adding 1 for Two's complement
            # print(bit_length)
            # Get the Two's complement representation
            num = (1 << bit_length) + num  # (1 << bit_length) creates a mask for the binary width
            # print(num)
        while num>=0:
            stack.append(num%2)
            num = num//2
            if num==0:
                return stack[::-1]
