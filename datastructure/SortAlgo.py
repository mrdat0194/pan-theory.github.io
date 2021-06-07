#!/usr/bin/env python
# coding: utf-8

# # Swap Function in Python

# In[ ]:


var1 = 1
var2 = 2
var1, var2 = var2, var1

# In[ ]:


print(var1, var2)

# In[ ]:


list = [25, 21, 22, 24, 23, 27, 26]

# # SORTING ALGORITHMS

# # Pass 1 of Bubble Sort

# In[7]:


lastElementIndex = len(list) - 1
print(0, list)
for idx in range(lastElementIndex):
    if list[idx] > list[idx + 1]:
        list[idx], list[idx + 1] = list[idx + 1], list[idx]
    print(idx + 1, list)

# In[ ]:


list


# # Bubble Sort Algorithm

# In[5]:


def BubbleSort(list):
    # Excahnge the elements to arrange in order
    lastElementIndex = len(list) - 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list


# In[ ]:


list = [25, 21, 22, 24, 23, 27, 26]

# In[ ]:


BubbleSort(list)


# ## Insertion Sort

# In[ ]:


def InsertionSort(list):
    for i in range(1, len(list)):
        j = i - 1
        next = list[i]
        # Compare the current element with next one

        while (list[j] > next) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = next
    return list


# In[ ]:


InsertionSort(list)


# # Shell Sort Algorithm

# In[ ]:


def ShellSort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            # Sort the sub list for this distance
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        # Reduce the distance for the next element
        distance = distance // 2
    return list


# In[ ]:


list = [19, 2, 31, 45, 30, 11, 121, 27]

# In[ ]:


ShellSort(list)
print(list)


# ## Merge Sort

# In[6]:


def MergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2  # splits list in half
        left = list[:mid]
        right = list[mid:]

        MergeSort(left)  # repeats until length of each list is 1
        MergeSort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list


# In[7]:


list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
MergeSort(list)


# ## Selection Sort

# In[ ]:


def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list


# In[ ]:


list = [70, 15, 25, 19, 34, 44]
SelectionSort(list)


# # SEARCHING ALGORITHMS

# ## Linear Search

# In[1]:


def LinearSearch(list, item):
    index = 0
    found = False

    # Match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found


# In[2]:


list = [12, 33, 11, 99, 22, 55, 90]
print(LinearSearch(list, 12))
print(LinearSearch(list, 91))


# ## Binary Search

# In[6]:


def BinarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# In[7]:


list = [12, 33, 11, 99, 22, 55, 90]
sorted_list = BubbleSort(list)
print(BinarySearch(list, 12))
print(BinarySearch(list, 91))


# ## Intpolation Search

# In[11]:


def IntPolsearch(list, x):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:

        # Find the mid point
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))

        # Compare the value at mid point with search value
        if list[mid] == x:
            found = True
            return found

        if list[mid] < x:
            idx0 = mid + 1
    return found


# In[16]:


list = [12, 33, 11, 99, 22, 55, 90]
sorted_list = BubbleSort(list)
print(IntPolsearch(list, 12))
print(IntPolsearch(list, 91))


# # Depth First Search

# In[3]:


def dfs(aGraph, root):
    stack = [root]
    parents = {root: root}
    path = list
    while stack:
        print('Stack is: %s' % stack)
        vertex = stack.pop(-1)
        print('Working on %s' % vertex)
        for element in aGraph[vertex]:
            if element not in parents:
                parents[element] = vertex
                stack.append(element)
                print('Now, adding %s to the stack' % element)
                path.append(parents[vertex] + '>' + vertex)
    return path[1:]


# In[4]:


g = dict()
g['Amine'] = ['Wassim', 'Nick', 'Mike', 'Elena']
g['Wassim'] = ['Amine', 'Imran']
g['Nick'] = ['Amine']
g['Mike'] = ['Amine', 'Mary']
g['Elena'] = ['Amine']
g['Imran'] = ['Wassim', 'Steven']
g['Mary'] = ['Mike']
g['Steven'] = ['Imran']

# In[5]:


dfs(g, "Amine")

# In[ ]:




