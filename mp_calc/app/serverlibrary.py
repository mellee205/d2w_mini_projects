def merge(array,p,q,r,byfunc):
    len_left=q-p+1
    len_right=r-q
    left_array=array[p:q+1]
    right_array=array[q+1:r+1]
    left=0
    right=0
    target=p

    if byfunc!=None:
      command=byfunc
      while (left<len_left) and (right<len_right):
          if command(left_array[left])<=command(right_array[right]):
              array[target]=left_array[left]
              left+=1
          else:
              array[target]=right_array[right]
              right+=1
          target+=1
    else:
      while (left<len_left) and (right<len_right):
        if left_array[left]<=right_array[right]:
            array[target]=left_array[left]
            left+=1
        else:
            array[target]=right_array[right]
            right+=1
        target+=1
    while (left<len_left):
        array[target]=left_array[left]
        left+=1
        target+=1
    while (right<len_right):
        array[target]=right_array[right]
        right+=1
        target+=1

def mergesort_recursive(array, p, r,byfunc):
  if r-p>0:
    q=(p+r)//2
    mergesort_recursive(array,p,q,byfunc)
    mergesort_recursive(array,q+1,r,byfunc)
    merge(array,p,q,r,byfunc)

def mergesort(array, byfunc=None):
  mergesort_recursive(array,0,len(array)-1,byfunc)

class Stack:
    def __init__(self)->None:
        self._items=[]
    
    def push(self,item):
        self._items.append(item)
    
    def pop(self):
        if len(self._items)==0:
            return None
        else:
            last_item=self._items[-1]
            self._items=self._items[:-1]
            return last_item
    
    def peek(self):
        if len(self._items)==0:
            return None
        else:
            return self._items[-1]
    
    @property
    def is_empty(self)->bool:
        if len(self._items)==0:
            return True
        else:
            return False
    
    @property
    def size(self)->int:
        return len(self._items)
    
    @property
    def _Stack__items(self):
        return self._items
    
    @_Stack__items.setter
    def _Stack__items(self,value):
        self._items=value

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr=""
    self.expression=string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    #this somehow also handles "" but im not complaining
    is_valid=True
    for ch in new_expr:
      if ch not in self.valid_char:
        is_valid=False
    if is_valid:
      self.expr=new_expr
    else:
      self.expr=""

  def insert_space(self):
    final_str=""
    operators='+-*/()'
    operands="1234567890"
    for ch in self.expression:
      if ch in operators:
        final_str+=f" {ch} "
      elif ch in operands:
        final_str+=ch
    return final_str
  
  def process_operator(self, operand_stack, operator_stack):
    second=operand_stack.pop()
    first=operand_stack.pop()
    operator=operator_stack.pop()

    if operator=="/":
      operand_stack.push(int(first)//int(second))
    else:
      #print(str(first))
      #print(operator)
      #print(str(second))
      operand_stack.push(eval(str(first)+operator+str(second)))  

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    #print(tokens)
    operands="1234567890"

    for ch in tokens:
      #print(ch)
      #print("operand",operand_stack._Stack__items)
      #print("operator",operator_stack._Stack__items)
      if ch in operands:
        operand_stack.push(ch)
      elif ch=="+" or ch=="-":
        while operator_stack.size!=0 and operator_stack.peek()!="(" and operator_stack.peek()!=")":
          self.process_operator(operand_stack,operator_stack)
        operator_stack.push(ch)
      elif ch=="*" or ch=="/":
        while operator_stack.size!=0 and (operator_stack.peek()=="*" or operator_stack.peek()=="/"):
          self.process_operator(operand_stack,operator_stack)
        operator_stack.push(ch)
      elif ch=="(":
        operator_stack.push(ch)
      elif ch==")":
        while operator_stack!=0 and operator_stack.peek()!="(":
          self.process_operator(operand_stack,operator_stack)
        if operator_stack.peek()=="(":
          operator_stack.pop()
    while operator_stack.size!=0:
      self.process_operator(operand_stack,operator_stack)
    
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





