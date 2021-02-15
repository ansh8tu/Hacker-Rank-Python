testCases = int(input())

for case in range(testCases):
    try: 
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
