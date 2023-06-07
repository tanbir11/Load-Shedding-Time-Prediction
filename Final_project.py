import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('SW1.csv')
model = LinearRegression()
model.fit(data[['Temp']], data[['time']])

def graph():
    plt.step(data['Temp'], data['time'])
    plt.xlabel('Temp')
    plt.ylabel('time')
    plt.show()

def prediction():
    print("Enter today temparature : ")
    b=int(input())
    print("Today Load sheding time may be ",model.predict([[b]]),"hour")
    #print(model.predict([[b]]))

def main():
    print("---Load Sheding time prediction--")
    print("""Enter you option : 
            1.See previous graph
            2.Prediction Today Load sheding   
    """)
    print("Choice your option:")
    a=int(input())
    if a==1:
        graph()
    elif a==2:
        prediction()

def login():
    print("Welcome Simple Load Sheding time Project")
    print("-----------------------------------------")
    print("Login")
    c=(input("Enter Your Email : "))
    e=int(input("Enter password :"))

    if (c=="tanbir") & (e==1234):
        main()
    else:
        print("Try again.....")
        login()

login()

#main()