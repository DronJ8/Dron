import  numpy as np


class Mattrixx:

    # Створення матриці А
    def GreatMatrixxA(self, n, m):
        self.A = np.random.randint(1, 100, size=(n, m))
        return self.A

    # Створення матриці B
    def GreatMatrixxB(self, n, m):
        self.B = np.random.randint(1, 100, size=(n, m))
        return self.B

    # Друк матриці А
    def PrintMatrixA(self, n1,m1):
        print(self.GreatMatrixxA(n1,m1))

    # Друк матриці B
    def PrintMatrixB(self, n1,m1):
        print(self.GreatMatrixxB(n1,m1))

    #  Матриця помножена на число
    def MultMatrixNumber(self):
        for i in range(2):
            for j in range(2):
                self.A[i][j] = self.A[i][j] * 2
        print("Матрицю А помножили на число 2", self.A)

    #   Різниця матриць
    def DifMatrixx(self):
        C = np.random.randint(0, 1, size=(len(self.A), len(self.B)))
        for i in range(len(self.A)):
            for j in range(len(self.B)):
                C[i][j] = self.A[i][j] - self.B[i][j]
        print("Різниця матриць-----", C)

    #   Сума матриць
    def SummMatrixx(self):
        C = np.random.randint(0, 1, size=(len(self.A), len(self.B)))
        for i in range(len(self.A)):
            for j in range(len(self.B)):
                C[i][j] = self.A[i][j] + self.B[i][j]
        print("Сума матриць-----", C)

    # Транспонована матриця
    def TransportMatrixx(self):
        B1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for i in range(len(self.A)):
            for j in range(len(self.A)):
                B1[i][j] = self.A[j][i]
        print("Матрицю А транспонували", B1)
    #     Множення матриць
    def MultiplMatrixs(self, n, m):
        X = self.GreatMatrixxA(n,m)
        Y = self.GreatMatrixxB(n,m)
        result = np.random.randint(1, 2, size=(n, m))

        for i in range(len(X)):
            # iterate through columns of Y
            for j in range(len(Y[0])):
                # iterate through rows of Y
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        for r in result:
            print(r)


M = Mattrixx()

M.MultiplMatrixs(3,3)
# # M.PrintMatrixB(3,3)
# M.MultMatrixNumber()



# print(M.PrintMatrix())