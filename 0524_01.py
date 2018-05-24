#인터넷 뱅킹을 활용하여 다양한 입출금 서비스 만들기
#
def check_money(balance, money):
	if balance >= money:
		return True
	else : 
		return False

class account():
	def __init__(self, name, number, balance):
		self.Name = name
		self.Number = number
		self.Balance = balance

	def injection(self, money):
		if check_money(self.Balance, money):
			print("Success injection")
			self.Balance -= money
		else :
			print("You can't inject money over your balance", self.Balance)

	def deposit(self, money):
		self.Balance += money
		print("Success")

	def __str__(self):
		msg = "Name :" + str(self.Name) + "\nAccountNumber :" + str(self.Number) + "\nYourBalance :" + str(self.Balance)
		return msg

def transfer(SendP, GetP, money):
	if check_money(SendP.Balance, money):
		SendP.Balance -= money
		GetP.Balance += money
		print("Success transfer")
	else :
		print("You can't send money over your balance", self.Balance)



Person01 = account("Cho", "1234", 1000)
Person02 = account("Cho", "1345", 1000)
transfer(Person01, Person02, 100)
print(Person01)
print(Person02)

