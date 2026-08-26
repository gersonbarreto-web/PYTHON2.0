notas = []

for x in range(8):
        n = float(input(f"Digite a {x+1} nota?"))
        notas.append(n)

media = sum(notas)/len(notas)

for espiao in notas:
    if(espiao>=media):
          print(espiao,end="-")

print(f"\n A media da turma e {media:.1f}")              
    