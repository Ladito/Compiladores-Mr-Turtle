#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

txt = " "
cont = 0

def increaseCont():
    global cont
    cont +=1
    return "%d" %cont

class Node():
    pass

class program(Node):
    def _init_(self, son3, son5, name):
        self.name = name
        self.son3 = son3
        self.son5 = son5

    def printt(ident):
        self.son3.printt(" " +ident)
        self.son5.printt(" " +ident)

        print ident + "Node: " + self.name

    def traducir(self):
        global txt
        id = increaseCont()
        son3 = self.son3.traducir()
        son5 = self.son5.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->" + son3 + "\n\t"
        txt += id + "->" + son5 + "\n\t"

        return "diagraph G {\n\t"+txt+"}"


class var1(Node):
    def _init_(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printt(ident):
        self.son1.printt(" " +ident)
        self.son2.printt(" " +ident)

        print ident + "Node: " + self.name

    def traducir(self):
        global txt
        id = increaseCont()
        son3 = self.son1.traducir()
        son5 = self.son2.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return "diagraph G {\n\t"+txt+"}"


class var2(Node):
    def _init_(self, son1, name):
        self.name = name
        self.son1 = son1

    def printt(ident):
        self.son1.printt(" " +ident)

        print ident + "Node: " + self.name

    def traducir(self):
        global txt
        id = increaseCont()
        son3 = self.son1.traducir()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->" + son1 + "\n\t"

        return "diagraph G {\n\t"+txt+"}"

class var2Empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class varOps1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class varOps2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class func1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class func2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class func2Empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class function(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class com1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class com2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class com2Empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class funct1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class funct1Empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class commandOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class commandOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class commandOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class commandOp4(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class variableD(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class id1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class id2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class id2Empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class typeOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class typeOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class typeOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class type1Op1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class type1Op2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class type1Op3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class assign(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class valueOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class valueOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class value2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class value2typeOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class value2typeOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class value2typeOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class value2typeOp4(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class operatorOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class operatorOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class operatorOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class operatorOp4(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class operatorOp5(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class funcReturn(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class parameter(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class param1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class param2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class param2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class condition(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class cond1Op1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class cond1Op2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class statement(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateOp(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateOpEmpty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp4(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp5(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class stateoperatorOp6(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instruction(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instBloque1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instBloque2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instBloque3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instStatusOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instStatusOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp1(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp2(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp3(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp4(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp5(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class instFuncOp6(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id


class empty(Node):
    def _init_(self.name):
        self.name = name

    def traducir(self):
        global txt
        id = increaseCont()

        return id
