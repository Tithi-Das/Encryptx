#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(x, y):
  return x + y


# In[3]:


def sub(x, y):
  return x - y


# In[4]:


def mul(x, y):
  return x * y


# In[5]:


def div(x, y):
  if y == 0:
    return "Error: Division by zero is not defined!"
  return x / y


# In[6]:


print("Simple Calculator")
print("----------------")


# In[13]:


# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# In[9]:


print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


# In[14]:


op_choice = int(input("Enter your choice (1/2/3/4): "))


# In[16]:


# Perform the calculation
if op_choice == 1:
  result = add(num1, num2)
elif op_choice == 2:
  result = sub(num1, num2)
elif op_choice == 3:
  result = mul(num1, num2)
elif op_choice == 4:
  result = div(num1, num2)
else:
  result = "Error: Invalid operation choice!"


# In[17]:


# Display the result
print("Result:", result)


# In[ ]:




