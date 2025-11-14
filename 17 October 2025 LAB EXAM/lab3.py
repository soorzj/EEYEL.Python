#avg height of boys and girls
nboys=int(input("Enter No: of boys:"))
ngirls=int(input("Enter No: of girls:"))
htboys,htgirls=0,0
for i in range(nboys):
    h=int(input("Enter a boy Height :"))
    htboys+=h
for i in range(ngirls):
    h=int(input("Enter a girl Height :"))
    htgirls+=h
print("Average height of boys:",(htboys/nboys))
print("Average height of girls:",(htgirls/ngirls))




