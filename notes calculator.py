amt = int(input("Enter amount : "))
n_1000 = n_500 = n_200 = n_100 = n_50 = n_20 = n_10 = n_5 = n_2 = n_1 = 0
if amt >= 1000:
    n_1000 = amt // 1000
    amt = amt % 1000
    print("1000 rs notes are", n_1000)

if amt >= 500:
    n_500 = amt // 500
    amt = amt % 500
    print("500 rs notes are", n_500)

if amt >= 200:
    n_200 = amt // 200
    amt = amt % 200
    print("200 rs notes are", n_200)

if amt >= 100:
    n_100 = amt // 100
    amt = amt % 100
    print("100 rs notes are", n_100)

if amt >= 50:
    n_50 = amt // 50
    amt = amt % 50
    print("50 rs notes are", n_50)

if amt >= 20:
    n_20 = amt // 20
    amt = amt % 20
    print("20 rs notes are", n_20)

if amt >= 10:
    n_10 = amt // 10
    amt = amt % 10
    print("10 rs notes are", n_10)

if amt >= 5:
    n_5 = amt // 5
    amt = amt % 5
    print("5 rs notes are", n_5)

if amt >= 2:
    n_2 = amt // 2
    amt = amt % 2
    print("2 rs notes are", n_2)

if amt >= 1:
    n_1 = amt // 1
    amt = amt % 1
    print("1 rs notes are", n_1)