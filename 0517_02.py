class Ball:
	direction = "default"

	def bounce(self):
		if self.direction == "down":
			self.direction = "up"

myBall = Ball()
myBall.__class__.direction = "stop"		#'_'는 두개
yourBall = Ball()
print(yourBall.direction)