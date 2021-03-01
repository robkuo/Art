import random
#定義Gird網格 物件
class Grid:
    def __init__(self,UPprice,Downprice,count):
       rang=UPprice-Downprice
       self.spacing=rang/count
       self.grids=[]#放入所有的格數值
       x=Downprice
       while (x<UPprice):
          self.grids.append(x)
          x=x+self.spacing
       self.grids.append(x)
    def GetNearDown(self,price):
        """回傳現價的下一格"""
        s=-1
        for i in range(len(self.grids)):
            if (self.grids[i]>price):
                s=self.grids[i-1]
                break
        return s
    def GetNearUP(self,price):
        """回傳現價的上一格"""
        s=-1
        for i in range(len(self.grids)):
            if (self.grids[i]>price):
                s=self.grids[i]
                break
        return s    
    def GetPricePos(self,price):
        """回傳價格所在的區間"""
        s=0
        for i in range(len(self.grids)):
            if (self.grids[i]<price):
                s=s+1
        return s       
                
#Grid 物件宣告結束

#以下為摸擬價格變化的副程式    
def amplitude():
    """ 回傳脹跌幅度"""
    dice=random.randint(1,1000)
    #dice決定機率  700 以內2% 700-850 3%  850 以上5%
    if (dice <701):
       a=random.randint(1,20)/10
    if (dice in range(701,850)):
       a=random.randint(1,30)/10
    if (dice in range(850,1000)):
       a=random.randint(1,50)/10
    return (a/100)


def nextprice(price):
    """返回下個價格  dice --1表示上升 2是下跌"""
    dice=random.randint(1,2)   
    if (dice==1):
      s=price*(1+amplitude())
    else:
      s=price*(1-amplitude()) 
    return s
#以上為摸擬價格變化的副程式

#以下為改變倉位的副程式

def change(newprice,oldprice,pair,grid):

    if (grid.GetPricePos(newprice)!=grid.GetPricePos(oldprice)):
        np=grid.GetPricePos(newprice)
        op=grid.GetPricePos(oldprice)
        print (newprice)
        print (grid.grids[np])
        print (oldprice)
        print (grid.grids[op])
        
    

#以上為改變倉位的副程式
grid=Grid(60000,40000,40)
price=50000    #起始價格
pair=[50000,1]#起始的出場倉位


change(48881,49100,pair,grid)
print (grid.GetPricePos(40800))
print (grid.GetNearUP(57600))

    
