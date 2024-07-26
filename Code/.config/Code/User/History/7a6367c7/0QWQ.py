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

    def autocomma(self,var,index,mode,Stringvar,Entry=None):
        StringVar = Stringvar
        strget = StringVar.get()
        new_list = []
        
        if strget != None:
            for i in strget:
                if i not in ",":
                    new_list.append(f"{i},")
            StringVar.set("".join(new_list))
            ic(new_list)

