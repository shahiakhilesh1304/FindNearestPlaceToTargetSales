import Imports as im

def main():
    target = im.target.targetCityCoOrdinates(input("What is the target city of sales: "))
    branch = im.ListOfBranchCoOrdinate.coOrd()
    result= im.findDistance.minDistance(branch,target)
    print("The Nearest Station which will give the heighest productivity at low cost with less resource utilization is -> ",result)


if __name__ == '__main__':
    main()

