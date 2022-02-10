class Cuser:
  
    def __init__(self, usn,name,status,id,img):
      self.user = usn
      self.fn = name
      self.s = status
      self.id = id
      self.imgu = img

    def getuser(self):
        return self.user, self.fn, self.s, self.id, self.imgu


    def setuser(self):
      self.user = ''
      self.fn = ''
      self.s = -1
      self.id = -1
      self.imgu = ''
      
      
      
      
    #   class Cuser:
    
    # def __init__(self, usn='',name='',status=-1,id=-1,img=''):
    #   self.user = usn
    #   self.fn = name
    #   self.s = status
    #   self.id = id
    #   self.imgu = img

    # def getuser(self):
    #     return self.user, self.fn, self.s, self.id, self.imgu


    # def setuser(self):
    #   self.user = ''
    #   self.fn = ''
    #   self.s = -1
    #   self.id = -1
    #   self.imgu = ''