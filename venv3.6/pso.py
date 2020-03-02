import metrics
import random
# import InfluenceEvaluation
# import Word_score_with_PositionWeight_sCAKE
import os

#os.system('source /home/nayan/coding/Major/EasySearch/venv/bin/activate')
#os.system('which python2')

gBst = [0,0,0,0]
gBstFit = 0

class Particle:

	def calFitness(self):

		os.system('python2 /home/nayan/coding/Major/EasySearch/venv/InfluenceEvaluation.py '+str(self.x[0])+' '+str(self.x[1])+' '+str(self.x[2]))
		os.system('python2 /home/nayan/coding/Major/EasySearch/venv/Word_score_with_PositionWeight_sCAKE.py '+str(self.x[3]))
		# InfluenceEvaluation(x[:3])
		# Word-score-with-PositionWeight-sCAKE(x[3])

		f1 = metrics.main()
		print (f1)
		return f1

	def __init__(self, x, v):
		self.x = x
		self.f = self.calFitness()
		self.pBest = x
		self.pBestFit = self.f
		self.v = v
		print(x, v)

	def update_pBst(self):
		
		if self.f > self.pBestFit:
			self.pBest = self.x
			self.pBestFit = self.f
		print(pBest, pBestFit)

	def update_gBst(self):

		if self.f > gBestFit:
			gBst = self.x
			gBstFit = self.f

		print(gBst, gBstFit)

	def updateVel(self):

		for i in range(4):
			v[i] -= random.uniform(0, 1) * (x[i]-pBest[i])
			v[i] -= 2 * random.uniform(0, 1) * (x[i]-gBest[i])

		print(v)

	def updateX(self):

		#f = 0
		for i in range(4):
			x[i] += v[i]

			if x[i] >1 or x[i] < 0:
				x = pBest
				break

		print(x)

#Particle([1,1,1,1],[0,0,0,0])
x1 = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
#x2 = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
print(x1)
Particle(x1,[random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])

# p = []
# pop_size = 5

# for i in range(pop_size):
# 	p.append(Particle([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)], [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]))


# for i in range(5):

# 	for i in range(pop_size):

# 		p[i].update_pBst()
# 		p[i].update_gBst()
# 		p[i].updateVel()
# 		p[i].updateX()

# print(gBst)
# print(gBstFit)