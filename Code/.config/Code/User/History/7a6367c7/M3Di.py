class InputLogic:
    def __init__(self, ui):
        self.ui = ui

    def one_word(self, var, index, mode, strvar, focus=None,unfocus=None):
        self.strvar = strvar
        self.focus_ele = focus
        self.unfocus_ele = unfocus
        self.get = self.strvar.get()
        self.strvar.set(self.get.upper())

        if len(self.get) > 1:
            self.strvar.set(self.get[0].upper())

        if self.focus_ele != None:
            if len(self.get) > 0:
                self.focus_ele.focus()

        # if self.unfocus_ele != None and len(self.get) == 0:
        #     self.ui.app.bind("<BackSpace>",self.unfocus_ele.focus())

    def word_sep(self,word_list: list):
        
