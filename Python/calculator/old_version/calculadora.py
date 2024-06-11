class Calculadora:
    nums = []
    expressao = ''

    def calcular(self,expressao):
        try:
            self.nums = []
            self.expressao = expressao
            self.separarNumeros()
            self.multiplicarDividir()
            self.somarSubtrair()
            return float(self.nums[0])
        except:
            return 

    def separarNumeros(self):
        num = ''
        for i in range(0,len(self.expressao)):
            if self.expressao[i].isnumeric() == False and self.expressao[i] != '.':
                self.nums.append(float(num))
                num = ' '
            else:
                num += self.expressao[i]

    def multiplicarDividir(self):
        result = 0 ; position = 0
        for n in range(0,len(self.expressao)):
            if self.expressao[n] == '+' or self.expressao[n] == '-':
                position+=1
            if self.expressao[n] == '*' or self.expressao[n] == 'x':
                result = self.nums.pop(position+1)
                self.nums[position] *= result
            if self.expressao[n] == '/':
                result = self.nums.pop(position+1)
                self.nums[position] /= result

    def somarSubtrair(self):
        result = 0
        for i in range(0,len(self.expressao)-1):
            if self.expressao[i] == '+':
                result = self.nums.pop(0)
                self.nums[0] += result
            if self.expressao[i] == '-':
                result = self.nums.pop(1)
                self.nums[0] -= result