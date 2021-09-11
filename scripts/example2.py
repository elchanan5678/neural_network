import numpy as np



def main():
    print('---------------------------------------------------------')
    a = np.zeros(3)
    b = np.empty(4)
    print(a, b, type(a), type(b))  

    c = np.ones(5)  
    d = np.linspace(0,10, 4)
    print(c, d, type(c[0]))
    print('--------------------------------------------------------')

    e = np.array([[1, 2, 3], [4, 5, 6]])
    print(e, e.shape)

    f = np.array([[1,2,3], [4, 5, 6]])
    print(f, f.shape)
    print('-----------tensor \/ ----------------------------------------------')

    g = np.array([f, e])
    print("tensor", g)



if __name__ ==  '__main__':
    main()
