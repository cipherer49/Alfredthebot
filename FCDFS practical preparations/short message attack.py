def p_and_q(n):
   data = []
   for i in range(2, n):
      if n % i == 0:
         data.append(i)
   return tuple(data)

def euler(p, q):
   return (p - 1) * (q - 1)

def private_index(e, euler_v):
   for i in range(2, euler_v):
      if i * e % euler_v == 1:
         return i

def decipher(d, n, c):
   return c ** d % n
def main():
    e = int(input("input e: "))
    n = int(input("input n: "))
    c = int(input("input c: "))
    p_and_q_v = p_and_q(n)
    euler_v = euler(p_and_q_v[0], p_and_q_v[1])
    d = private_index(e, euler_v)
    plain = decipher(d, n, c)
    print("plain: ", plain)
if __name__ == "__main__":
   main()