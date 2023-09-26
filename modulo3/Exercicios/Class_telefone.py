class Telefone:

    __Tipo = 'Smartphone'

    def __init__(self, xiaomi, samsung, apple, nokia, lg, blu, blackberry, asus):

        self.__Xiaomi = xiaomi
        self.__Samsung = samsung
        self.__Apple = apple  
        self.__Nokia = nokia
        self.__Lg = lg
        self.__Blu = blu
        self.__Blackberry = blackberry
        self.__Asus = asus

    # getters

    @property
    def xiaomi(self):
        return self.__Xiaomi
    
    @property
    def samsung(self):
        return self.__Samsung
    
    @property
    def apple(self):
        return self.__Apple
    
    @property
    def nokia(self):
        return self.__Nokia
    
    @property
    def lg(self):
        return self.__Lg
    
    @property
    def blu(self):
        return self.__Blu
    
    @property
    def blackberry(self):
        return self.__Blackberry

    @property
    def asus(self):
        return self.__Asus
    
    # setters

    @xiaomi.setter
    def xiaomi(self, xiaomi):
        self.__Xiaomi = xiaomi
   
    @samsung.setter
    def samsung(self, samsung):
        self.__Samsung = samsung
   
    @apple.setter
    def apple(self, apple):
        self.__Apple = apple
   
    @nokia.setter
    def nokia(self, nokia):
        self.__Nokia = nokia
   
    @lg.setter
    def lg(self, lg):
        self.__Lg = lg
   
    @blu.setter
    def blu(self, blu):
        self.__Blu = blu
   
    @blackberry.setter
    def blackberry(self, blackberry):
        self.__Blackberry = blackberry
   
    @asus.setter
    def asus(self, asus):
        self.__Asus = asus
   
    def __str__(self):
        return f'''\nModelo Xiaomi : {self.xiaomi} 
            \nModelo Samsung : {self.samsung} 
            \nModelo Apple : {self.apple} 
            \nModelo Nokia : {self.nokia}
            \nModelo Lg :  {self.lg} 
            \nModelo Blue : {self.blu} 
            \nModelo Blackberry : {self.blackberry} 
            \nModelo Asus : {self.asus}
'''
    

        