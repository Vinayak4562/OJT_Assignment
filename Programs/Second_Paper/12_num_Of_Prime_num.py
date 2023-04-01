def number_of_prime_numbers(num1, num2):
    prime_count = 0                                     # Initialize count to zero
    prime_sum = 0                                       # Initialize sum to zero
    primes = []
    
    for num in range(num1, num2+1):                     # Iterate over the range of numbers from num1 to num2, inclusive
        if num > 1:                                     # Bcz 1 is not a prime number so we have to skip 1 using condition num > 1              
            
            for i in range(2, int(num/2)+1):            # num/2 will give Float val so we have to convert it in to integer         
                if num % i == 0:                        # if number is divisible by i then its a not a prime number we will break the loop
                    break
            else:
                primes.append(num)                      # appending the prime number to the primes list
                prime_count += 1                        # incrementing the prime number count
                prime_sum += num                        # adding the prime number to the primes_sum

    print("Prime numbers in a given range: ", primes)   # printing all prime numumbers in given range
    return prime_count, prime_sum                       # returning both values i,e.. prime_count and prime_sum 


count, prime_sum = number_of_prime_numbers(10,20)

print("Count of prime numbers:", count)
print("Sum of prime numbers:", prime_sum)
