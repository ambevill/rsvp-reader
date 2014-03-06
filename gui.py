import Tkinter as tki
from tkFont import Font
from wordfeed import WordFeed
from settings import RSVP_FONT_DICT, RSVP_SHAPE
from sys import platform


master = tki.Tk()

class Gui(object):

    def __init__(self):
        self.master = master
        self._pause_flag = True
        #
        self.input_frame = InputFrame(self.master, self)
        self.input_frame.pack(side=tki.TOP)
        self.rsvp_frame = RsvpFrame(self.master, self)
        self.rsvp_frame.pack(side=tki.TOP)
        self.control_frame = ControlFrame(self.master, self)
        self.control_frame.pack(side=tki.TOP)
        self.rate_string = rs = tki.StringVar()
        self.rate_label = tki.Label(self.master, textvariable=rs)
        self.rate_label.pack(side=tki.TOP)
        #
        self.master.bind('<Escape>', lambda e: self.master.destroy())
        self.master.resizable(False, False)
        #
        self.wordfeed = None
        self.update_wordfeed()
        #
        self.apply_settings()

    def apply_settings(self):
        pass

    def export_settings(self, path):
        pass

    def update_wordfeed(self, name=None, index=None, mode=None):
        inext = self.wordfeed.inext if self.wordfeed else 0
        text = self.input_frame.entry.get()
        self.wordfeed = WordFeed(text, inext)
        self.rsvp_frame.update()
        self.update_rate()

    def update_rate(self):
        num_words, total_minutes = self.wordfeed.get_statistics()
        if num_words < 1:
            return
        stat_format = '{0} words in {1:.2f} minutes = {2} WPM.'
        self.rate_string.set(stat_format.format(
            num_words,
            total_minutes,
            int(num_words / total_minutes)))

    def update_rsvp(self):
        text, delay_ms = self.wordfeed.next()
        if text == None:
            self.pause()
        else:
            self.rsvp_frame.display_text(text)
        return delay_ms

    def rsvp_kernel(self):
        if self._pause_flag:
            return
        delay_ms = self.update_rsvp()
        if delay_ms:
            self.master.after(delay_ms, self.rsvp_kernel)

    def pause_resume(self, event=None):
        if self._pause_flag: self.resume()
        else: self.pause()

    def pause(self, event=None):
        self._pause_flag = True
        print 'pause'

    def resume(self, event=None):
        self._pause_flag = False
        print 'resume'
        self.rsvp_kernel()

    def back10(self, event=None):
        print 'back 10'
        self.wordfeed.inext -= 10
        self.update_rsvp()

    def back50(self, event=None):
        print 'back 50'
        self.wordfeed.inext -= 50
        self.update_rsvp()


class InputFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        self.inputvar = tki.StringVar(value='Enter text here...')
        self.inputvar.trace('w', self.gui.update_wordfeed)
        self.entry = tki.Entry(self, textvariable=self.inputvar, width=50)
        self.entry.pack()
        sel_all_cmd = '<Command-a>' if platform == 'darwin' else '<Control-a>'
        self.entry.bind(sel_all_cmd, self.select_all)

    def select_all(self, event=None):
        self.entry.selection_range(0, tki.END)
        return 'break'


class RsvpFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        self.font = Font(**RSVP_FONT_DICT)
        self.shape = width,height = RSVP_SHAPE
        self.text_id = None
        c = self.canvas = tki.Canvas(self, width=width, height=height)
        c.pack()
        c.bind('<Button-1>', self.gui.pause_resume)
        self.clear_canvas()

    def display_text(self, text):
        width, height = self.shape
        if self.text_id != None:
            self.canvas.delete(self.text_id)
            self.text_id = None
        self.text_id = self.canvas.create_text(
            (width/2, height/2),
            text=text,
            font=self.font)

    def clear_canvas(self):
        self.canvas.delete()
        self.canvas.create_rectangle(0,0,*self.shape,fill='white')


class ControlFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        #
        b = self.pause_button = tki.Button(
            self,
            text='PP',
            command=gui.pause_resume)
        b.pack(side=tki.LEFT)
        #
        b = self.back10_button = tki.Button(
            self,
            text='< 10',
            command=gui.back10)
        b.pack(side=tki.LEFT)
        #
        b = self.back50_button = tki.Button(
            self,
            text='< 50',
            command=gui.back50)
        b.pack(side=tki.LEFT)
