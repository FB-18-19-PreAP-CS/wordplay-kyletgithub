def palindromic_number():
    for i in range(1000000):
        if (str(i).zfill(6))[2:] == (str(i).zfill(6))[5:1:-1]:
            if (str(i+1).zfill(6))[1:] == (str(i+1).zfill(6))[5:0:-1]:
                if (str(i+2).zfill(6))[1:5] == (str(i+2).zfill(6))[4:0:-1]:
                    if (str(i+3).zfill(6)) == (str(i+3).zfill(6))[::-1]:
                        print(i)
