


import random


















def main():
    for i in range(5):
        print(i, random.random())

    testList = ['A','B','C','D','E']
    for i in range(5):
        print(i,random.choice(testList))





if __name__ == '__main__':
    main()
