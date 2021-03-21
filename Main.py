import csv
import time
def first_load():
    data = "hotel_data.csv"
    row_data=[]
    with open(data,'r') as csvfile:
        reader=csv.reader(csvfile)
        feild=next(reader)
        for row in reader:
            row_data.append(row)


        Hotel_dict=dict()
        for i in row_data:
            if i[2] in Hotel_dict:
                Hotel_dict[i[2]].append([int(i[3]),float(i[4]),i[1]])
            else:
                Hotel_dict[i[2]]=[[int(i[3]),float(i[4]),i[1]]]
    return Hotel_dict

def find(state,val,ops,Hotel_dict):
        arr=Hotel_dict[state]
        if ops=="highest":
            if val=="cost":
                highest_data=max(arr,key=lambda x:x[0])
                print("Hotel with",ops,"price",state,"is",highest_data[2],"with price",highest_data[0])
            elif val=="rating":
                highest_data=max(arr,key=lambda x:x[1])
                print("Hotel with",ops,"rating",state,"is",highest_data[2],"with rating",highest_data[1])
            else:
                print("Invalid Input")
        elif ops=="average":
            if val=="cost":
                avgerage_value=0
                for i in arr:
                    avgerage_value+=i[0]
                avgerage_data=avgerage_value//len(arr)
                print(ops,val,"of Hotel in",state,"is",avgerage_data)
            elif val=="rating":
                avgerage_value=0.0
                for i in arr:
                    avgerage_value+=i[1]
                avgerage_rating=avgerage_value//len(arr)
                print(ops,val,"of Hotel in",state,"is",avgerage_rating)
            else:
                print("Invalid Input")
        elif ops=="cheapest":
            if val=="cost":
                highest_data=min(arr,key=lambda x:x[0])
                print("Hotel with",ops,"price",state,"is",highest_data[2],"with price",highest_data[0])
            elif val=="rating":
                highest_data=min(arr,key=lambda x:x[0])
                print("Hotel with",ops,"rating",state,"is",highest_data[2],"with rating",highest_data[1])
            else:
                print("Invalid Input")
        else:
                print("Invalid Input")


def Main():
    state=input("What is the state :")
    value=input("Cost or Rating :")
    Operation=input("Operation :")
    Hotel_dict=first_load()
    time.sleep(2)  #given to time to load all excel data
    find(state,value,Operation,Hotel_dict)
Main()


