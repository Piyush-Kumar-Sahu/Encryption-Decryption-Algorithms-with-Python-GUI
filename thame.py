"""
Theme module for CodeSnippet Manager.

Handles the visual appearance of the application, including colors, fonts,
and widget styles.
"""
import tkinter as tk
from tkinter import ttk
import platform

def setup_theme(root):
    """
    Set up the application theme.
    
    Args:
        root: The root Tkinter window
    """
    # Define color scheme
    colors = {
        'primary': '#2C2C2C',     # dark grey
        'secondary': '#383838',   # medium grey
        'background': '#1E1E1E',  # charcoal
        'text': '#D4D4D4',        # light grey
        'accent': '#569CD6',      # blue
        'highlight': '#CE9178',   # coral
        'error': '#F44747',       # red
        'success': '#6A9955',     # green
        'selection': '#264F78',   # darker blue for selections
        'comment': '#608B4E',     # green for comments
        'keyword': '#C586C0',     # purple for keywords
        'string': '#CE9178',      # coral for strings
        'number': '#B5CEA8',      # light green for numbers
        'function': '#DCDCAA',    # yellow for functions
    }
    
    # Determine default font family based on platform
    if platform.system() == 'Windows':
        default_font = 'Consolas'
        mono_font = ('Consolas', 10)
    elif platform.system() == 'Darwin':  # macOS
        default_font = 'Menlo'
        mono_font = ('Menlo', 10)
    else:  # Linux and others
        default_font = 'Monaco'
        mono_font = ('Monaco', 10)
    
    # Configure root window colors
    root.configure(bg=colors['background'])
    
    # Create custom ttk style
    style = ttk.Style(root)
    
    # Try to use a modern theme as a base
    try:
        style.theme_use('clam')  # Use clam theme as a base
    except tk.TclError:
        pass  # Fallback to default theme if clam is not available
    
    # Configure TFrame
    style.configure('TFrame', background=colors['background'])
    
    # Configure TLabel
    style.configure('TLabel', 
                  background=colors['background'],
                  foreground=colors['text'],
                  font=(default_font, 10))
    
    # Configure TButton
    style.configure('TButton',
                  background=colors['secondary'],
                  foreground=colors['text'],
                  borderwidth=1,
                  focusthickness=1,
                  focuscolor=colors['accent'],
                  padding=(5, 2),
                  font=(default_font, 9))
    
    style.map('TButton',
            background=[('active', colors['accent']),
                        ('pressed', colors['accent'])],
            foreground=[('active', '#FFFFFF'),
                        ('pressed', '#FFFFFF')])
    
    # Configure TEntry
    style.configure('TEntry',
                  fieldbackground=colors['secondary'],
                  foreground=colors['text'],
                  insertcolor=colors['text'],
                  borderwidth=1,
                  padding=5,
                  font=mono_font)
    
    # Configure TCombobox
    style.configure('TCombobox',
                  fieldbackground=colors['secondary'],
                  background=colors['background'],
                  foreground=colors['text'],
                  arrowcolor=colors['text'],
                  borderwidth=1,
                  padding=5)
    
    style.map('TCombobox',
            fieldbackground=[('readonly', colors['secondary'])],
            selectbackground=[('readonly', colors['accent'])],
            selectforeground=[('readonly', '#FFFFFF')])
    
    # Configure dropdown list for comboboxes
    root.option_add('*TCombobox*Listbox.background', colors['secondary'])
    root.option_add('*TCombobox*Listbox.foreground', colors['text'])
    root.option_add('*TCombobox*Listbox.selectBackground', colors['accent'])
    root.option_add('*TCombobox*Listbox.selectForeground', '#FFFFFF')
    root.option_add('*TCombobox*Listbox.font', mono_font)
    
    # Configure TScrollbar
    style.configure('TScrollbar',
                  background=colors['secondary'],
                  troughcolor=colors['background'],
                  borderwidth=0,
                  arrowcolor=colors['text'])
    
    style.map('TScrollbar',
            background=[('active', colors['accent']),
                        ('pressed', colors['accent'])])
    
    # Configure TPanedwindow
    style.configure('TPanedwindow',
                  background=colors['background'],
                  sashrelief='flat',
                  sashwidth=4)
    
    # Configure TNotebook
    style.configure('TNotebook',
                  background=colors['background'],
                  tabmargins=[0, 0, 0, 0],
                  borderwidth=0)
    
    style.configure('TNotebook.Tab',
                  background=colors['secondary'],
                  foreground=colors['text'],
                  padding=[10, 2],
                  borderwidth=0,
                  font=(default_font, 9))
    
    style.map('TNotebook.Tab',
            background=[('selected', colors['accent'])],
            foreground=[('selected', '#FFFFFF')])
    
    # Configure TLabelframe
    style.configure('TLabelframe',
                  background=colors['background'],
                  foreground=colors['text'],
                  borderwidth=1,
                  relief='solid')
    
    style.configure('TLabelframe.Label',
                  background=colors['background'],
                  foreground=colors['text'],
                  font=(default_font, 9, 'bold'))
    
    # Configure Listbox
    root.option_add('*Listbox.background', colors['secondary'])
    root.option_add('*Listbox.foreground', colors['text'])
    root.option_add('*Listbox.selectBackground', colors['accent'])
    root.option_add('*Listbox.selectForeground', '#FFFFFF')
    root.option_add('*Listbox.font', mono_font)
    
    # Configure Text
    root.option_add('*Text.background', colors['secondary'])
    root.option_add('*Text.foreground', colors['text'])
    root.option_add('*Text.selectBackground', colors['selection'])
    root.option_add('*Text.selectForeground', '#FFFFFF')
    root.option_add('*Text.insertBackground', colors['text'])
    root.option_add('*Text.font', mono_font)
    
    # Return the colors dictionary for use elsewhere in the application
    return colors
