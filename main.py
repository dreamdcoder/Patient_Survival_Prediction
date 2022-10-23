9def TowerOfHanoi(source, destination, auxiliary):
    def TowerOfHanoi(n, source, destination, auxiliary):
        if n == 1:
            print("Move disk 1 from source", source, "to destination", destination)
            return
        TowerOfHanoi(n - 1, source, auxiliary, destination)
        print("Move disk", n, "from source", source, "to destination", destination)
        TowerOfHanoi(n - 1, auxiliary, destination, source)

    # Driver code
    n = 4
    TowerOfHanoi(n, 'A', 'B', 'C')



# Driver code
n = 3
bay_1= [100,150,200]
bay_2 =[]
bay_3 = []
TowerOfHanoi(n, 'A', 'B', 'C')

3333333333333333333333333333333333333333.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
