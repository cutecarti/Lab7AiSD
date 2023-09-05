class Flowers(object):
    def cwr(self,iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)
    def most_expensive_bouquet(self, list):
        pricelist = {1:100,2:58,3:44,4:87,5:154,6:118,7:65,8:29,9:95,10:299,11:43,12:59,13:999,14:32,15:29,16:51,17:240,18:178,19:44,20:74}
        s = self.s
        for i in list:
            s += pricelist.get(i)
        self.s = s
        if s > self.max:
            self.max = s
            self.maxbouquet = tuple(list)
            self.s = 0
    def generate_hardboquets(self,K,N):
        flowers = list(range(1, K+1))
        bouquets = []

        for num_flowers in range(1, N+1):
            for bouquet in self.cwr(flowers,num_flowers):
                if len(set(bouquet)) >= len(bouquet) - 1:
                    bouquets.append(bouquet)
                    self.most_expensive_bouquet(bouquet)
        return bouquets
    def getmax(self):
        return self.max
    def getmaxbouquet(self):
        return self.maxbouquet
    max = 0
    maxbouquet = tuple()
    s = 0

flowers = Flowers()
print('Введите количество видов(Не больше 20):')
k = int(input())
print('Введите максимальный размер букета:')
n = int(input())
print('Сгенерированные букеты:')
for i in flowers.generate_hardboquets(k,n):
    print(i)
print('Самый дорогой букет: ',flowers.getmaxbouquet())
print('Цена: ',flowers.getmax())


