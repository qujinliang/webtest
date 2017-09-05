#Fibonacci series: 斐波那契数列
#两个元素的综合确定了下一个数
def fibo(num):
	a,b=0,1
	while b < num:
		print (b,end = ',')
		a,b = b, a+b

fibo(100)


