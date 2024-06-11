class Calculadora:
    nums = []
    expressao = ''

    def calcular(self,expressao):
            self.nums = []
            self.expressao = expressao
            self.separarNumeros()
            self.multiplicarDividir()
            self.somarSubtrair()
            return float(self.nums[0])
       

    def separarNumeros(self):
        num = '0'
        inverter = False
        for i in range(0,len(self.expressao)):
            if self.expressao[i].isnumeric() == False and self.expressao[i] != '.':
                if inverter == True:
                    self.nums.append(-float(num))
                    if self.expressao[i] != '-':
                        inverter = False
                elif self.expressao[i] == '-':
                    inverter = True
                    if num != '0' or self.expressao[i] == '0':
                        self.nums.append(float(num))
                else:
                    self.nums.append(float(num))
                num = '0'
            else:
                num += self.expressao[i]
        if self.nums[0] == 0 and self.expressao[0] != '0':
            self.nums.pop(0)

    def multiplicarDividir(self):
        result = 0 ; position = 0
        for n in range(0,len(self.expressao)):
            if self.expressao[n] == '+':
                position+=1
            if self.expressao[n] == '*' or self.expressao[n] == 'x':
                result = self.nums.pop(position+1)
                self.nums[position] *= result
            if self.expressao[n] == '/':
                result = self.nums.pop(position+1)
                self.nums[position] /= result

    def somarSubtrair(self):
        result = 0
        for numeros in self.expressao[:-1]:
            if (numeros == '+' or numeros == '-') and len(self.nums)>1:
                result = self.nums.pop()
                self.nums[0] += result

#calculadora = Calculadora()
#exp = input('Equa: ')
#exp+='?'
#print('Resultado {}'.format(calculadora.calcular(exp)))
