number = int(input("Please Input The Number Of Days : "))
year = number // 365
month = ((number % 365 ) // 30)
week = ((((number % 365)) % 30) // 7)
day = ((((number % 365) % 30) % 7))   
print(f"Amount Of {number} Days Equals To : {year} Year(s) , {month} Month(s) , {week} Week(s) , {day} Day(s) ")