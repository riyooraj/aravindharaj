def main():
    year=int(input(""))
    if(year%4==0 and year%100!=0 or year%400==0):
         print(" if leap year")
    else:
     print("not a leap year")
if __name__ == '__main__':
    main()
