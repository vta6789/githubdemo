import math
opptinons = input( "chọn 1 trong các loại phép tính sau ( + ;- ;* ;/ ;% **)" )

a = float ( input ( "nhập số thứ nhất: " ) )
b = float ( input ( "nhập số thứ hai: " ) )
c = float ( input ( "nhập số thứ ba: " ) )


if opptinons == " +" :
    print (" kết quả là: " , int(a + b + c ) )

elif opptinons == "-" :
    answer = a - b - c 
    answer = answer -  math.floor(answer) 
    if answer <= 0.5 :
        answer =  answer + 1 
        print(f" kết quả là:  {round(answer,3)} " )
    elif answer >= 0.5 :
        answer = answer + 1
        print ( f" kết quả là: {math.ceil(answer)} " )
    else :
        print ( f" kết quả là: { answer} " ) 

elif opptinons == "*" :
    print ( "kết quả là: ", int(a * b * c ))

elif opptinons == "/" :
    print ( "kết quả là: ", int(a / b / c )) 
elif opptinons == "%" :
    print ( "kết quả là: ", int(a % b % c ))
else :
    print ( "kết quả là: ", int(a ** b ** c ))