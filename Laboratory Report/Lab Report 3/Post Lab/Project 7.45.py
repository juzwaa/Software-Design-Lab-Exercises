class SparseArray(object):

        def __init__(self,items=0):

            self.L = [0]*items

 
        def __setitem__(self, j, e):

            self.L[j] = e


        def __getitem__(self, j):

            return self.L[j]

 
        def __str__(self):

            return str(self.L)


sa=SparseArray(5)


sa[0]=(12,"Hi")

sa[1]=(21,"I'm")

sa[2]=(51,"Jozhua")

sa[3]=(76,"Lenard")

sa[4]=(108,"Huertas")


print("Sparse Array Content: \n",sa)