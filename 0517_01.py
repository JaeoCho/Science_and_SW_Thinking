class Ball:
	direction = "default"

	def bounce(self):
		if self.direction == "down":
			self.direction = "up"

myBall = Ball()
print(myBall.direction)
myBall.direction = "down"
print(myBall.direction)
myBall.bounce()
print(myBall.direction)
myBall.size = 10
print(myBall.size)
yourBall = Ball()
print(yourBall.size)
