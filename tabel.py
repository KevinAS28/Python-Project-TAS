import sqlTAS

tabel = "11_rpl_2"
mapel = ["kimia", "matematika", "fisika", "ppkn"]
for i in mapel:
 #sqlTAS.Run("drop table %s_%s" %(tabel, i.upper()))
 sqlTAS.Run("create table %s_%s(nama varchar(100), nilai_uts varchar(100), nilai_uas varchar(100), nilai_ukk varchar(100))" %(tabel, i))
