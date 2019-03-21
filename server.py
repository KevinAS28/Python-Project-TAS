import socket
import os
import sqlTAS
import TCP
from threading import Thread
#jangan hapus semua pake checkbox, tambahin home, posisi cursor nilai, edit nilai, logo taro, notif kkm,
connection = TCP.Protocol(888)

def tambah_murid(data):
	torun = "insert into 11_rpl_2_%s(nama, nilai_uts, nilai_uas, nilai_ukk) values('%s', '0', '0', '0')" %(data[-1].decode("utf-8"), data[0].decode("utf-8"))
	sqlTAS.Run(torun)
	return b""
def hapus_semua(data):
	torun = "delete from 11_rpl_2_%s" %(data[-1].decode("utf-8"))
	sqlTAS.Run(torun)
	return b""
def hapus_murid(data):
	torun = "delete from 11_rpl_2_%s where nama='%s'" %(data[-1].decode("utf-8"), data[0].decode("utf-8"))
	sqlTAS.Run(torun)
	return b""

def get_all_student(data):
 dat = sqlTAS.Run("select * from 11_rpl_2_%s" %(data[-1].decode("utf-8")));
 toreturn = b""
 for i in dat:
  toreturn += (str(i)+";").replace("'", "").replace("(", "").replace(")", "").encode("utf-8")
 return toreturn

def update_nilai(data):

	for i in range(len(data)):
		data[i] = data[i].decode("utf-8")
	torun = "update 11_rpl_2_%s set nilai_uts='%s', nilai_uas='%s', nilai_ukk='%s' where nama='%s'" %(data[-1], data[1], data[2], data[3], data[0])
	print(torun)
	sqlTAS.Run(torun)
	return b"good"
allfunc = {"get_all_student": get_all_student, "update_nilai": update_nilai, "hapus_murid": hapus_murid, "tambah_murid": tambah_murid, "hapus_semua": hapus_semua}

def mergeByte(bytelist):
 toreturn = b""
 for i in bytelist:
  toreturn+=chr(i).encode("utf-8")
 return toreturn

def Client_Handler(data, idd, addr, adddr):
 print(data)
 data = list(data)
 del data[0]
 del data[0]
 data = mergeByte(data).split(b" ")
 func = data[0].decode("utf-8")
 tosend = allfunc[func](data[1:])
 print(tosend)
 connection.Send_By_ID(idd, tosend)	


connection.Start_Listen([Client_Handler])
