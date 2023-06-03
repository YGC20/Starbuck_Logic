import GPTAPI

# [a,b,c,...]을 저정하는 리스트
Check_List = [chr(i) for i in range(97,123)]

def Logic_Prefix(MLL:list):             # 중위표현을 후위표현
    stack = []                          # 연산자와 괄호를 저장하기 위한 빈 스택을 생성합니다.
    operators = {'and': 1, 'or': 1}     # 연산자와 그들의 우선순위를 정의합니다.
    prefix_expr = []                    # 접두사 표현식을 저장하기 위한 빈 리스트를 생성합니다.
    tokens = MLL.copy()
    
    for token in tokens:
        if token == '(':        # 토큰이 여는 괄호인 경우, 스택에 푸시합니다.
            stack.append(token)
        elif token == ')':      # 토큰이 닫는 괄호인 경우, 스택에서 연산자를 팝하여 접두사 표현식에 추가합니다.
            while stack and stack[-1] != '(':   # 여는 괄호를 만날 때까지 반복합니다.
                prefix_expr.append(stack.pop())
            stack.pop()                 # 여는 괄호를 스택에서 팝합니다.
        elif token in operators:        # 토큰이 연산자인 경우, 스택에서 우선순위가 더 낮은 연산자나 여는 괄호를 만날 때까지 연산자를 팝하고 접두사 표현식에 추가합니다.
            while stack and stack[-1] != '(' and operators[token] < operators.get(stack[-1], 0):
                prefix_expr.append(stack.pop())
            stack.append(token)         # 현재 연산자를 스택에 푸시합니다.
        else:                           # 토큰이 연산자나 괄호가 아닌 경우, 바로 접두사 표현식에 추가합니다.
            prefix_expr.append(token)
    while stack:                        # 모든 토큰을 처리한 후, 스택에 남아있는 모든 연산자를 팝하고 접두사 표현식에 추가합니다.
        prefix_expr.append(stack.pop())
    
    # 최종적인 접두사 표현식을 반환합니다.
    return prefix_expr

# 후위표현으로 전환된 재고와 주문을 논리식으로 변환
def Order_Change(cafe:list, order:list):
    Check_List_count = 0
    
    # 후위표현임으로 뒤쪽에서부터 확인 연산자가 없고 주문과 재고 같으면 변수로 변경
    if len(cafe) < len(order):
        for c in range(len(cafe)-1,-1,-1):
            for o in range(len(order)-1,-1,-1):
                if cafe[c] != 'and' and cafe[c] != 'or' and order[o] != 'and' and order[o] != 'or':
                    if cafe[c] == order[o]:
                        cafe[c] = order[o] = Check_List[Check_List_count]
                        Check_List_count += 1
                        break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    elif len(cafe) > len(order):
        for o in range(len(order)-1,-1,-1):
            for c in range(len(cafe)-1,-1,-1):
                if cafe[c] != 'and' and cafe[c] != 'or' and order[o] != 'and' and order[o] != 'or':
                    if cafe[c] == order[o]:
                        cafe[c] = order[o] = Check_List[Check_List_count]
                        Check_List_count += 1
                        break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    else:
        for c in range(len(cafe)-1,-1,-1):
            for o in range(len(order)-1,-1,-1):
                if cafe[c] != 'and' and cafe[c] != 'or' and order[o] != 'and' and order[o] != 'or':
                    if cafe[c] == order[o]:
                        cafe[c] = order[o] = Check_List[Check_List_count]
                        Check_List_count += 1
                        break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    
    return cafe, order
        
#Check_List를 확인하고 동일한 변수가 없으면 T를 반환함(cafe부분만)
def Order_Same_Check_cafe(cafe:list):
    for C in range(len(cafe)):
        if cafe[C] not in Check_List:
            if cafe[C] != 'and' and cafe[C] != 'or':
                cafe[C] = 'T'
    return cafe

#Check_List를 확인하고 동일한 변수가 없으면 T를 반환함(order부분만)
def Order_Same_Check_order(order:list):
    for C in range(len(order)):
        if order[C] not in Check_List:
            if order[C] != 'and' and order[C] != 'or':
                order[C] = 'F'
    return order

# 후위표현식으로 정리된 논리식을 중위표현식으로 나타날수 있도록 정리
def Change_pre_mid_Logic(PL:list):      
    stack = []
    operators = { 'and' : 1, 'or' : 1 }
    tokens = PL.copy()
    for token in tokens:
        if token in operators:
            B = stack.pop()
            A = stack.pop()
            expr = '(' + A + ' ' + token + ' ' + B + ')'
            stack.append(expr)
        else:
            stack.append(token)
    return stack[0]
        

def Logic(api , give:str):
    Logic_Order_Div = give.split('->')
    Logic_A = Logic_Order_Div[0].split(' ')
    Logic_B = Logic_Order_Div[1].split(' ')
    del Logic_A[len(Logic_A)-1]
    del Logic_B[0]
    pre_Logic_A = Logic_Prefix(Logic_A)
    pre_Logic_B = Logic_Prefix(Logic_B)
    PLA,PLB=Order_Change(pre_Logic_A,pre_Logic_B)
    Change_Logic = Change_pre_mid_Logic(PLA) + ' -> ' + Change_pre_mid_Logic(PLB)
    print(Change_Logic)
    answer = GPTAPI.ask(api , Change_Logic)
    return answer
    
