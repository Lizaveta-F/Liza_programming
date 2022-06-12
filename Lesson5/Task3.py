# В группе учащиеся увлекаются различными видами деятельностями: секция по настолькому теннису, Dota 2, литрбол.
# Они представлены тремя множествами из строк:
# tennis = {'Evans', 'Stone', 'Roberts', 'Mills', 'Lewis', 'Morgan'}
# dota = {'Grant', 'Morgan', 'Evans', 'Mills', 'Jackson', 'Bradley',}
# litrball = {'Grant', 'Morgan', 'Evans', 'Gibson', 'Jackson', 'Barlow', 'Adams'}
# Требуется вывести списки учащихся для каждой из 7 следующих групп:
# тех, кто интересуется всем;
# тех, кто интересуется всем, кроме тенниса;
# тех, кто интересуется всем, кроме доты;
# тех, кто интересуется всем, кроме литрбола;
# тех, кто интересуется только дотой;
# тех, кто интересуется только литрболом;
# тех, кто интересуется только теннисом;

tennis = {'Evans', 'Stone', 'Roberts', 'Mills', 'Lewis', 'Morgan'}
dota = {'Grant', 'Morgan', 'Evans', 'Mills', 'Jackson', 'Bradley', }
litrball = {'Grant', 'Morgan', 'Evans', 'Gibson', 'Jackson', 'Barlow', 'Adams'}
print("The list of students who are interested in all subjects: ",
      ", ".join(list(tennis & dota & litrball)))
print("The list of dtoudents who are in interested in all subjests except for tennis: ",
      ", ".join(list((dota | litrball)-tennis)))
print("The list of dtoudents who are in interested in all subjests except for dota: ",
      ", ".join(list((tennis | litrball)-dota)))
print("The list of dtoudents who are in interested in all subjests except for litrball: ",
      ", ".join(list((tennis | dota)-litrball)))
print("The list of dtoudents who are in interested in dota only: ",
      ", ".join(list(dota-(tennis | litrball))))
print("The list of dtoudents who are in interested in litrball only: ",
      ", ".join(list(litrball-(tennis | dota))))
print("The list of dtoudents who are in interested in tennis only: ",
      ", ".join(list(tennis-(dota | litrball))))
