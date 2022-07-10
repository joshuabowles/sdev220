#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#test_sum.py
assert sum([1, 2, 3]) == 6, "Should be 6"


# In[1]:


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")


# In[3]:


#test_sum_2.py
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")


# In[ ]:


#test_sum_unittest.py

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()


# In[ ]:


#TestSum
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


# In[5]:


target = __import__("my_sum.py")
sum = target.sum


# In[ ]:


#my_sum
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

