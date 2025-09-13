import os, sys

print ("\033[1;32mPASSWORDNYA KONTOL")

print ("\033[1;32mGK ADA? HUBUNGI YOS_999")

username = 'Yos-999'      

password = 'Yos123'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mNAH INI BARU BENER KONTOL", 

			sys.exit()



		else:

			print "\033[1;32mPASSWORDNYA SALAH KONTOL...[?]\033[00m"

			print "Ulangi Masukin Yang Bener Passwordnya!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
