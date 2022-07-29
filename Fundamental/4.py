# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def count_positives_sum_negatives(arr):
      if arr == []:
      #  if not arr: return [] 
            return []
      else:
            arr2=[]
            sum =0
            count =0
            for i in range(len(arr)):
                  if arr[i] > 0:
                        count = count + 1
                  elif arr[i] < 0:
                        sum = sum + arr[i]
            
            arr2.append(count)
            arr2.append(sum)
            return arr2
            

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []