import GPTAPI

def Logic_Check(MLL:list):  #MLL = Menu_Logic_List
    menu = []
    logic = []
    for check in MLL:
        if check == 'and' or check == 'or':
            logic.append(check)
        else:
            menu.append(check)
    return menu, logic

def Order_Change(cafe:list, order:list):
    Check_List = ['p','q','r','s','t','u']
    Check_List_count = 0
    
    if len(cafe) > len(order):
        for c in range(len(cafe)):
            for o in range(len(order)):
                if cafe[c] == order[o]:
                    cafe[c] = order[o] = Check_List[Check_List_count]
                    Check_List_count += 1
                    break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    elif len(cafe) < len(order):
        for o in range(len(order)):
            for c in range(len(cafe)):
                if cafe[c] == order[o]:
                    cafe[c] = order[o] = Check_List[Check_List_count]
                    Check_List_count += 1
                    break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    else:
        for c in range(len(cafe)):
            for o in range(len(order)):
                if cafe[c] == order[o]:
                    cafe[c] = order[o] = Check_List[Check_List_count]
                    Check_List_count += 1
                    break
        cafe = Order_Same_Check_cafe(cafe)
        order = Order_Same_Check_order(order)
    
    return cafe, order
        

def Order_Same_Check_cafe(cafe:list):
    Check_List = ['p','q','r','s','t','u']
    for C in range(len(cafe)):
        if cafe[C] not in Check_List:
            cafe[C] = 'T'
    return cafe

def Order_Same_Check_order(order:list):
    Check_List = ['p','q','r','s','t','u']
    for C in range(len(order)):
        if order[C] not in Check_List:
            order[C] = 'F'
    return order

def Change_String(LTS:list, Logic:list) -> str:
    String = ''
    for i in range(len(LTS)):
        if i == len(LTS)-1:
            String = String+' '+LTS[i]
        else:
            String = String+' '+LTS[i]+' '+Logic[i]
    return String
        

def main():
    Logic_Order_Div = input().split('->')
    Logic_A = Logic_Order_Div[0].split(' ')
    Logic_B = Logic_Order_Div[1].split(' ')
    del Logic_A[len(Logic_A)-1]
    del Logic_B[0]
    Menu1, Logic1 = Logic_Check(Logic_A)
    Menu2, Logic2 = Logic_Check(Logic_B)
    Menu1, Menu2 = Order_Change(Menu1,Menu2)
    Change_Logic = Change_String(Menu1,Logic1)+' -> '+Change_String(Menu2,Logic2)
    print(Change_Logic)
    print(GPTAPI.ask(Change_Logic))
    

if __name__ == main():
    main()