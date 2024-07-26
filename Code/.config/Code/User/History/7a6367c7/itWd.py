from icecream import ic

class InputLogic:
    def __init__(self, ui):
        self.ui = ui

    def one_word(self, var, index, mode, strvar, focus=None, unfocus=None):
        strvar = strvar
        focus_ele = focus
        unfocus_ele = unfocus
        get = self.strvar.get()
        strvar.set(get.upper())

        if len(self.get) > 1:
            strvar.set(get[0].upper())

        if focus_ele != None:
            if len(get) > 0:
                focus_ele.focus()

        # if self.unfocus_ele != None and len(self.get) == 0:
        #     self.ui.app.bind("<BackSpace>",self.unfocus_ele.focus())

    def autocomma(self,var,index,mode,Stringvar):
        StringVar = Stringvar
        strget = StringVar.get()
        if strget != None:
            ic(list(strget))
            for i in strget:
                ic(i)

