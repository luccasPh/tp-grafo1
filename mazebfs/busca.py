
class BFS:
	def __init__(self, lab, rato, queijo):
		self.fronteira = []
		self.lab = Labirinto(lab[0], lab[1], lab[2])
		self.rato = Rato(rato[1], rato[0])
		self.queijo = Queijo(queijo[1], queijo[0])
		

	def buscar(self):
		vis = []
		for i in range(self.lab.alt):
			vis.append([])
			for j in range(self.lab.larg):
				vis[i].append(False)

		
		self.fronteira.append(Vertice(self.rato.pos_x, self.rato.pos_y))
		while self.fronteira != []:

			#TODO: retirar no da fronetira
			u = self.fronteira.pop(0)

			if u.v_x == self.queijo.pos_x and u.v_y == self.queijo.pos_y:
				V = u
				self.rato.pego = True
				break

			for i in range(4):
				x, y = self.rato.movi(i)
				self.rato.pos_x = u.v_x + x
				self.rato.pos_y = u.v_y + y

				if self.rato.pos_x > -1 and self.rato.pos_y > -1 and self.rato.pos_x < self.lab.alt and self.rato.pos_y < self.lab.larg:
					if self.lab.form[self.rato.pos_x][self.rato.pos_y] != -1 and not vis[self.rato.pos_x][self.rato.pos_y]:
						V = Vertice(self.rato.pos_x, self.rato.pos_y)
						self.fronteira.append(V)
						V.pai = u
			
			vis[u.v_x][u.v_y] = True

		solu = []
		while True:
			solu.insert(0,V)
			if V.pai == None:
				break
			V = V.pai
		
		return solu


class Vertice:
	def __init__(self, v_x, v_y):
		self.v_x = v_x
		self.v_y = v_y
		self.pai = None
		self.carlos = None

class Rato:
	def __init__(self, pos_x, pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.pego = False
	
	def movi(self, i):
		mov_x = [0,0,1,-1]
		mov_y = [1,-1,0,0]

		return mov_x[i], mov_y[i]

class Queijo:
	def __init__(self, pos_x, pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y

class Labirinto:
	def __init__(self, alt, larg, form):
		self.alt = alt
		self.larg = larg
		self.form = form
	"""
	def percuso(self, x, y):
		return lab[x][y]
	"""


"""
b = BFS()

r = Rato(6,10)
q = Queijo(1, 2)
l = Labirinto(8, 13)

c = b.buscar(l, r, q) 

for i in c:
	print(i.v_x, i.v_y)
"""
