#q=>https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern/
def alphaRamp(n: int) -> None:
    # Write your solution from here.
    character='A'
    for i in range(n):
        for j in range(i+1):
            print(character,end=" ")
        print()
        character=chr(ord(character)+1)
    pass
 
#other way
n=5
alpha=65
for i in range(n):
 for k in range(i+1):
   print(chr(alpha), end='')
 alpha+=1
 print()