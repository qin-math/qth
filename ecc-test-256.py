        
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

p = 115792089210356248756420345214020892766250353991924191454421193933289684991999
e = 2

n = p ** e

P = (76287479028675456870954024993890058697272599544631742469099405516086654060771,801460110144723473186151423554159119127537623208571482810690635844348462498704903765583493516644208839170757447340795005312960952503971581034298393859575, 1)


q = 115792089210356248756420345214020892766061623724957744567843809356293439045923 # pre calcule ( merci quand meme Sage )

a = 115792089210356248756420345214020892766250353991924191454421193933289684991996
b = 18505919022281880113072981827955639221458448578012075254857346196103069175443

mult (q , P , n , a , b)