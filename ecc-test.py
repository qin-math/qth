def add_points (P1 , P2 , n , a , b) :
    X1 , Y1 , Z1 = P1
    X2 , Y2 , Z2 = P2

    if X1 == X2 :
        return (0 , 1, 0)
    elif X1 != X2 :
        X3 = (X1 * Y2 - X2 * Y1) * (Y1 * Z2 + Y2 * Z1) + (X1 * Z2 - X2 * Z1) * Y1 * Y2 -a * (X1 * Z2 + X2 * Z1) * (X1 * Z2 - X2 * Z1) - 3 * b * (X1 * Z2 - X2 * Z1) * Z1 * Z2
        Y3 = -3 * X1 * X2 * (X1 * Y2 - X2 * Y1) - Y1 * Y2 * (Y1 * Z2 - Y2 * Z1) - a * (X1 * Y2 - X2 * Y1) * Z1 * Z2 + a * (X1 * Z2 + X2 * Z1) * (Y1 * Z2 - Y2 * Z1) + 3 * b * (Y1 * Z2 - Y2 * Z1) * Z1 * Z2
        Z3 = 3 * X1 * X2 * (X1 * Z2 - X2 * Z1) - (Y1 * Z2 + Y2 * Z1) * (Y1 * Z2 - Y2 * Z1) + a * (X1 * Z2 - X2 * Z1) * Z1 * Z2
        Q = ( X3 % n , Y3 % n , Z3 % n)
        print (X3)
        return  Q       


def double_points (P1 , P2 , n , a , b) :
    if P2 == (0 , 1, 0) : return P1
    if P1 == (0 , 1, 0) : return P2
    if P1 == P2 :
        X1 , Y1 , Z1 = P1
        X2 , Y2 , Z2 = P2

        X3 = Y1 * Y2 * ( X1 * Y2 + X2 * Y1) -a * X1 * X2* (Y1 *Z2 + Y2* Z1) - a * (X1*Y2+X2*Y1)*(X1*Z2+X2*Z1)-3*b*(X1*Y2+X2*Y1)*Z1*Z2-3*b*(X1*Z2+X2*Z1)*(Y1*Z2+Y2*Z1)+a*a*(Y1*Z2+Y2*Z1)*Z1*Z2
        Y3 = Y1*Y1*Y2*Y2+ 3*a*X1*X1*X2*X2+ 9*b*X1*X2*(X1*Z2+X2*Z1)-a*a*X1*Z2*(X1*Z2+2*X2*Z1)-a*a*X2*Z1*(2*X1*Z2+X2*Z1)-3*a*b*Z1*Z2*(X1*Z2+X2*Z1)-(a*a*a+ 9*b*b)*Z1*Z1*Z2*Z2
        Z3 = 3*X1*X2*(X1*Y2+X2*Y1)+Y1*Y2*(Y1*Z2+Y2*Z1)+a*(X1*Y2+X2*Y1)*Z1*Z2+a*(X1*Z2+X2*Z1)*(Y1*Z2+Y2*Z1)+ 3*b*(Y1*Z2+Y2*Z1)*Z1*Z2
        Q = ( X3 % n , Y3 % n , Z3 % n)
        print (X3)
        return  Q
    


def add_double_points (P1 , P2 , n , a , b) :
    if P2 == (0 , 1, 0) : return P1
    if P1 == (0 , 1, 0) : return P2
    if P1 == P2 :
        X1 , Y1 , Z1 = P1
        X3 = Y1 * Y2 * ( X1 * Y2 + X2 * Y1) -a * X1 * X2* (Y1 *Z2 + Y2* Z1) - a * (X1*Y2+X2*Y1)*(X1*Z2+X2*Z1)-3*b*(X1*Y2+X2*Y1)*Z1*Z2-3*b*(X1*Z2+X2*Z1)*(Y1*Z2+Y2*Z1)+a*a*(Y1*Z2+Y2*Z1)*Z1*Z2
        Y3 = Y1 * Y1 * Y2 * Y2 + 3 * a * X1 * X1 * X2 * X2 + 9 * b * X1 * X2 * (X1 * Z2 + X2 *Z1)-a * a * X1 * Z2 * (X1 * Z2 + 2* X2 * Z1)- a * a * X2 * Z1 *(2* X1 * Z2 + X2*Z1)-3*a*b*Z1*Z2*(X1*Z2+X2*Z1)-(a*a*a+ 9*b*b)*Z1*Z1*Z2*Z2
        Z3 = 3*X1*X2*(X1*Y2+X2*Y1)+Y1*Y2*(Y1*Z2+Y2*Z1)+a*(X1*Y2+X2*Y1)*Z1*Z2+a*(X1*Z2+X2*Z1)*(Y1*Z2+Y2*Z1)+ 3*b*(Y1*Z2+Y2*Z1)*Z1*Z2
        Q = ( X3 % n , Y3 % n , Z3 % n)
        print (X3)
        return  Q
    X1 , Y1 , Z1 = P1
    X2 , Y2 , Z2 = P2

    if X1 == X2  :
        return (0 , 1, 0)
    elif X1 != X2 :
        X3 = (X1 * Y2 - X2 * Y1) * (Y1 * Z2 + Y2 * Z1) + (X1 * Z2 - X2 * Z1) * Y1 * Y2 -a * (X1 * Z2 + X2 * Z1) * (X1 * Z2 - X2 * Z1) - 3 * b * (X1 * Z2 - X2 * Z1) * Z1 * Z2
        Y3 = -3 * X1 * X2 * (X1 * Y2 - X2 * Y1) - Y1 * Y2 * (Y1 * Z2 - Y2 * Z1) - a * (X1 * Y2 - X2 * Y1) * Z1 * Z2 + a * (X1 * Z2 + X2 * Z1) * (Y1 * Z2 - Y2 * Z1) + 3 * b * (Y1 * Z2 - Y2 * Z1) * Z1 * Z2
        Z3 = 3 * X1 * X2 * (X1 * Z2 - X2 * Z1) - (Y1 * Z2 + Y2 * Z1) * (Y1 * Z2 - Y2 * Z1) + a * (X1 * Z2 - X2 * Z1) * Z1 * Z2
        Q = ( X3 % n , Y3 % n , Z3 % n)
        print (X3)
        return  Q   


def mult (k , P , n , a , b) :
    if k == 0:
        return (0 , 1, 0)
    elif k == 1:
        return P
    elif k % 2 == 1:
        return add_points (P , mult ( k - 1, P , n , a , b ) , n , a , b)
    else :
        return mult (k // 2, double_points (P , P , n , a , b) , n , a , b )

p = 4451685225093714772084598273548427
e = 2

n = p ** e


P = (83723827053625960250204579067390,180506364435128720970607627035177139227921516424849324553482259192,1)


q = 4451685225093714776491891542548933 # pre calcule ( merci quand meme Sage )

a = 4451685225093714772084598273548424
b = 2061118396808653202902996166388514


mult (q , P , n , a , b)