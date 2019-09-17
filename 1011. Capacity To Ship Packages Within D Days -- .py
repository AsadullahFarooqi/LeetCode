def shipWithinDays(weights, D):
    avg = sum(weights) // D 
    items_limit = len(weights)//D
    start = 0
    end = 0
    l = []
    while end <= len(weights):
        if sum(weights[start:end]) > avg:
              l.append(weights[start:end-1])
              start = end-1
        end += 1
    print(l)

if __name__ == "__main__":
    weights_list = {
      15: ([1,2,3,4,5,6,7,8,9,10], 5),
      6: ([3,2,2,4,1,4], 3),
      3: ([1,2,3,1,1], 4)
    }
    for k,v in weights_list.items():
        print("Inputs : ", v ,"\nOutputs : ", k , " - ", shipWithinDays(*v))