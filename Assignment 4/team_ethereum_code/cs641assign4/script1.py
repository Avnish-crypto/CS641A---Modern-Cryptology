import pexpect

def main():
	child = pexpect.spawn('/usr/bin/ssh student@172.27.26.188')
	def calls():

		child.expect('student@172.27.26.188\'s password:')
		child.sendline('cs641')
		child.expect('Enter your group name: ', timeout=1) 
		child.sendline("team_ethereum")

		child.expect('Enter password: ', timeout=1)
		child.sendline("team_ethereum")

		child.expect('\r\n\r\n\r\nYou have solved 3 levels so far.\r\nLevel you want to start at: ', timeout=1)
		child.sendline("4")

		child.expect('.*')
		child.sendline("back")

		child.expect('.*')
		child.sendline("enter")

		child.expect('.*')
		child.sendline("wave")

		child.expect('.*')
		child.sendline("back")


		child.expect('.*')
		child.sendline("back")

		child.expect('.*')
		child.sendline("thrnxxtzy")

		child.expect('.*')
		child.sendline("read")

		child.expect('.*')
		child.sendline("the_magic_of_wand")

		child.expect('.*')
		child.sendline("c")

		child.expect('.*')
		child.sendline("read")
	
	calls()


	f = open("plain1.txt", 'r')
	f1= open("cipher1.txt",'w')

	for line in f.readlines():
		child.sendline(line)
		#print(child.before)
		f1.writelines(str(child.before)[48:64]+"\n")
		child.expect("Slowly, a new text starts*")
		child.sendline("c")
		child.expect('The text in the screen vanishes!')

	data = child.read()
	print(data)
	child.close()
	print(child.before, child.after)

	f.close()
	f1.close()

main()