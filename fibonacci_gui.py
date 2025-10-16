import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import sys

def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class FibonacciGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔢 Calculadora de Fibonacci - Dark Edition")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Colores del tema dark
        self.colors = {
            'bg_primary': '#1e1e1e',      # Fondo principal (gris muy oscuro)
            'bg_secondary': '#2d2d2d',    # Fondo secundario (gris oscuro)
            'bg_tertiary': '#3e3e3e',     # Fondo terciario (gris medio)
            'accent': '#0078d4',          # Azul Microsoft
            'accent_hover': '#106ebe',    # Azul más oscuro para hover
            'success': '#107c10',         # Verde para éxito
            'warning': '#ff8c00',         # Naranja para advertencias
            'error': '#d13438',           # Rojo para errores
            'text_primary': '#ffffff',    # Texto blanco
            'text_secondary': '#cccccc',  # Texto gris claro
            'text_muted': '#999999',      # Texto gris
            'border': '#454545',          # Bordes
            'shadow': '#000000'           # Sombras
        }
        
        # Configurar el tema dark
        self.setup_dark_theme()
        
        # Configurar el ícono (opcional)
        try:
            self.root.iconbitmap(default="favicon.ico")
        except:
            pass  # Si no hay ícono, continuar sin él
        
        # Establecer color de fondo principal
        self.root.configure(bg=self.colors['bg_primary'])
        
        self.setup_ui()
        
    def setup_dark_theme(self):
        """Configura el tema dark personalizado"""
        style = ttk.Style()
        
        # Configurar tema base
        style.theme_use('clam')
        
        # Configurar estilos personalizados
        
        # Frame principal
        style.configure('Dark.TFrame', 
                       background=self.colors['bg_primary'],
                       borderwidth=0)
        
        # Frame secundario
        style.configure('DarkSecondary.TFrame', 
                       background=self.colors['bg_secondary'],
                       borderwidth=1,
                       relief='solid')
        
        # Botones principales
        style.configure('DarkAccent.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text_primary'],
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 12, 'bold'))  # Aumentado de 10 a 12
        
        style.map('DarkAccent.TButton',
                 background=[('active', self.colors['accent_hover']),
                           ('pressed', '#005a9e')])
        
        # Botones secundarios
        style.configure('DarkSecondary.TButton',
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       borderwidth=1,
                       relief='solid',
                       focuscolor='none',
                       font=('Segoe UI', 11))  # Aumentado de 9 a 11
        
        style.map('DarkSecondary.TButton',
                 background=[('active', self.colors['border']),
                           ('pressed', self.colors['bg_secondary'])])
        
        # Entry (campos de entrada)
        style.configure('Dark.TEntry',
                       background='#f0f0f0',  # Fondo gris muy claro
                       foreground='#000000',  # Texto negro para mejor contraste
                       borderwidth=2,
                       relief='solid',
                       insertcolor='#000000',  # Cursor negro
                       font=('Segoe UI', 14),  # Aumentado de 11 a 14
                       fieldbackground='#f0f0f0')  # Asegurar fondo claro
        
        # Mapeo de estados para Entry
        style.map('Dark.TEntry',
                 focuscolor=[('!focus', self.colors['border']),
                           ('focus', self.colors['accent'])],
                 bordercolor=[('focus', self.colors['accent']),
                            ('!focus', self.colors['border'])])
        
        # LabelFrame
        style.configure('Dark.TLabelframe',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['text_secondary'],
                       borderwidth=1,
                       relief='solid',
                       font=('Segoe UI', 10, 'bold'))
        
        style.configure('Dark.TLabelframe.Label',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['accent'],
                       font=('Segoe UI', 10, 'bold'))
        
        # Progressbar
        style.configure('Dark.Horizontal.TProgressbar',
                       background=self.colors['accent'],
                       troughcolor=self.colors['bg_secondary'],
                       borderwidth=0,
                       lightcolor=self.colors['accent'],
                       darkcolor=self.colors['accent'])
        
    def setup_ui(self):
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, style='Dark.TFrame', padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Título principal con gradiente visual
        title_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        # Título con efecto de sombra
        shadow_title = tk.Label(title_frame, 
                               text="🔢 CALCULADORA DE FIBONACCI", 
                               font=("Segoe UI", 20, "bold"),  # Aumentado de 18 a 20
                               fg=self.colors['shadow'], 
                               bg=self.colors['bg_primary'])
        shadow_title.pack(anchor='center')
        
        title_label = tk.Label(title_frame, 
                              text="🔢 CALCULADORA DE FIBONACCI", 
                              font=("Segoe UI", 20, "bold"),  # Aumentado de 18 a 20
                              fg=self.colors['accent'],
                              bg=self.colors['bg_primary'])
        title_label.place(in_=shadow_title, x=-1, y=-1)
        
        # Subtítulo
        subtitle = tk.Label(title_frame,
                           text="Edición Dark • Interfaz Moderna",
                           font=("Segoe UI", 12),  # Aumentado de 10 a 12
                           fg=self.colors['text_muted'],
                           bg=self.colors['bg_primary'])
        subtitle.pack()
        
        # Frame para entrada con estilo
        input_container = ttk.Frame(main_frame, style='DarkSecondary.TFrame', padding=15)
        input_container.pack(fill='x', pady=(0, 20))
        
        # Etiqueta de entrada
        input_label = tk.Label(input_container, 
                              text="💡 Ingrese un número:",
                              font=("Segoe UI", 14, "bold"),  # Aumentado de 12 a 14
                              fg=self.colors['text_primary'],
                              bg=self.colors['bg_secondary'])
        input_label.pack(anchor='w', pady=(0, 8))
        
        # Frame para entry y botón principal
        entry_frame = ttk.Frame(input_container, style='DarkSecondary.TFrame')
        entry_frame.pack(fill='x', pady=(0, 15))
        
        self.number_entry = ttk.Entry(entry_frame, style='Dark.TEntry', font=("Segoe UI", 14))  # Aumentado de 12 a 14
        self.number_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.number_entry.bind("<Return>", lambda e: self.calculate())
        
        # Botón principal más grande y llamativo
        self.calculate_btn = ttk.Button(entry_frame, 
                                       text="🚀 CALCULAR", 
                                       command=self.calculate, 
                                       style="DarkAccent.TButton")
        self.calculate_btn.pack(side='right', ipady=5, ipadx=15)
        
        # Frame para botones secundarios
        button_frame = ttk.Frame(input_container, style='DarkSecondary.TFrame')
        button_frame.pack(fill='x')
        
        self.clear_btn = ttk.Button(button_frame, 
                                   text="🧹 Limpiar", 
                                   command=self.clear_all,
                                   style="DarkSecondary.TButton")
        self.clear_btn.pack(side='left', padx=(0, 10), ipady=3, ipadx=10)
        
        self.exit_btn = ttk.Button(button_frame, 
                                  text="❌ Salir", 
                                  command=self.root.quit,
                                  style="DarkSecondary.TButton")
        self.exit_btn.pack(side='left', ipady=3, ipadx=10)
        
        # Área de resultados con estilo mejorado
        result_frame = ttk.LabelFrame(main_frame, 
                                     text="  📊 RESULTADOS  ", 
                                     style='Dark.TLabelframe', 
                                     padding=15)
        result_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        # Resultado actual con fondo destacado
        result_bg = tk.Frame(result_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        result_bg.pack(fill='x', pady=(0, 15))
        
        self.current_result = tk.Label(result_bg, 
                                      text="Introduce un número para ver el resultado aquí...", 
                                      font=("Consolas", 14, "bold"),  # Aumentado de 12 a 14
                                      fg=self.colors['success'],
                                      bg=self.colors['bg_secondary'],
                                      wraplength=600,
                                      pady=15)
        self.current_result.pack(fill='x')
        
        # Historial con título
        history_label = tk.Label(result_frame,
                                text="📈 Historial de cálculos:",
                                font=("Segoe UI", 14, "bold"),  # Aumentado de 12 a 14
                                fg=self.colors['text_secondary'],
                                bg=self.colors['bg_primary'])
        history_label.pack(anchor='w', pady=(0, 8))
        
        # Text area con scrollbar personalizada
        text_frame = tk.Frame(result_frame, bg=self.colors['bg_primary'])
        text_frame.pack(fill='both', expand=True)
        
        self.history_text = tk.Text(text_frame, 
                                   height=10, 
                                   width=70, 
                                   font=("Consolas", 12),  # Aumentado de 11 a 12
                                   bg=self.colors['bg_secondary'],
                                   fg=self.colors['text_primary'],
                                   insertbackground=self.colors['text_primary'],
                                   selectbackground=self.colors['accent'],
                                   selectforeground=self.colors['text_primary'],
                                   relief='solid',
                                   bd=1,
                                   wrap='word')
        
        # Scrollbar personalizada
        scrollbar = tk.Scrollbar(text_frame, 
                                bg=self.colors['bg_tertiary'],
                                troughcolor=self.colors['bg_secondary'],
                                activebackground=self.colors['accent'])
        
        self.history_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.history_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.history_text.yview)
        
        # Barra de progreso con estilo
        self.progress_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        self.progress_frame.pack(fill='x', pady=5)
        
        self.progress_label = tk.Label(self.progress_frame, 
                                      text="", 
                                      font=("Segoe UI", 9),
                                      fg=self.colors['warning'],
                                      bg=self.colors['bg_primary'])
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, 
                                           style='Dark.Horizontal.TProgressbar',
                                           mode='indeterminate')
        
        # Mensaje inicial en el historial
        welcome_msg = """🌟 ¡Bienvenido a la Calculadora de Fibonacci Dark Edition! 🌟

💡 Consejos de uso:
• Números pequeños (1-50): ⚡ Cálculo instantáneo
• Números grandes (51-1000): ⏳ Cálculo con advertencia y progreso
• Números muy grandes (>1000): ⚠️ Requieren confirmación especial

🎯 Ejemplos recomendados para probar:
• Fibonacci(10) = 55
• Fibonacci(20) = 6,765
• Fibonacci(30) = 832,040
• Fibonacci(45) = 1,134,903,170

⚡ ¡Comienza ingresando un número arriba!
📊 Los resultados aparecerán aquí abajo...
"""
        self.history_text.insert('1.0', welcome_msg)
        self.history_text.config(state='disabled')
        
        # Focus inicial en la entrada
        self.number_entry.focus()
        
        # =================== FIRMA SIMPLE PERO VISIBLE EN LA PARTE INFERIOR ===================
        # Separador antes de la firma
        separator_top = tk.Frame(main_frame, height=3, bg=self.colors['accent'])
        separator_top.pack(fill='x', pady=(20, 10))
        
        # Frame para la firma FORZADA en la parte inferior con place() - COLOR DISCRETO
        signature_frame = tk.Frame(self.root, bg="#2d2d2d", relief='flat', bd=1, height=40)
        signature_frame.place(relx=0, rely=1.0, anchor='sw', relwidth=1.0)  # Forzar posición inferior
        
        # Firma principal - COLOR DISCRETO
        signature_label = tk.Label(signature_frame,
                                  text="POWERED BY TREYER",
                                  font=("Arial", 11, "normal"),
                                  fg="#888888",  # Texto gris discreto
                                  bg="#2d2d2d")  # Fondo gris oscuro discreto
        signature_label.pack(expand=True, fill='both')
        
    def calculate(self):
        try:
            input_text = self.number_entry.get().strip()
            if not input_text:
                messagebox.showwarning("Entrada vacía", "Por favor, ingrese un número.")
                return
                
            n = int(input_text)
            
            if n < 0:
                messagebox.showerror("Número inválido", "Por favor, ingrese un número entero no negativo.")
                return
            
            # Advertencia para números muy grandes
            if n > 1000:
                result = messagebox.askyesno("⚠️ Número muy grande", 
                    f"¿Está seguro de calcular Fibonacci({n})?\n\n"
                    f"⚠️ ADVERTENCIA:\n"
                    f"• Esto puede tardar varios minutos\n"
                    f"• Usará mucha memoria del sistema\n"
                    f"• El resultado será extremadamente largo\n\n"
                    f"¿Continuar de todos modos?")
                if not result:
                    return
            
            # Advertencia para números grandes
            elif n > 50:
                result = messagebox.askyesno("💡 Número grande", 
                    f"Vas a calcular Fibonacci({n})\n\n"
                    f"💡 INFORMACIÓN:\n"
                    f"• El cálculo puede tardar unos segundos\n"
                    f"• Se mostrará una barra de progreso\n"
                    f"• El resultado será bastante largo\n\n"
                    f"¿Continuar?")
                if not result:
                    return
            
            # Mostrar progreso para números grandes
            if n > 50:
                self.show_progress(f"Calculando Fibonacci({n})...")
                # Ejecutar cálculo en hilo separado para no bloquear la UI
                thread = threading.Thread(target=self.calculate_in_thread, args=(n,))
                thread.daemon = True
                thread.start()
            else:
                # Cálculo directo para números pequeños
                self.calculate_in_thread(n)
                
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingrese un número válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def calculate_in_thread(self, n):
        try:
            # Calcular resultado
            result = calculate_fibonacci(n)
            
            # Actualizar UI en el hilo principal
            self.root.after(0, self.update_result, n, result)
            
        except Exception as e:
            self.root.after(0, self.show_error, str(e))
    
    def update_result(self, n, result):
        # Ocultar barra de progreso
        self.hide_progress()
        
        # Mostrar resultado actual con colores temáticos
        if len(str(result)) > 100:
            display_result = f"{str(result)[:50]}...{str(result)[-50:]}"
            result_text = f"✨ Fibonacci({n}) = {display_result}\n💡 Resultado muy largo, ver historial completo abajo"
            self.current_result.config(fg=self.colors['warning'])
        else:
            result_text = f"✅ Fibonacci({n}) = {result}"
            self.current_result.config(fg=self.colors['success'])
        
        self.current_result.config(text=result_text)
        
        # Agregar al historial con formato mejorado
        self.history_text.config(state='normal')
        timestamp = "🕐 " + str(n).rjust(4) + " → "
        history_entry = f"{timestamp}{result}\n"
        self.history_text.insert(tk.END, history_entry)
        self.history_text.see(tk.END)
        self.history_text.config(state='disabled')
        
        # Limpiar entrada y enfocar
        self.number_entry.delete(0, tk.END)
        self.number_entry.focus()
    
    def show_error(self, error_msg):
        self.hide_progress()
        messagebox.showerror("Error de cálculo", f"Error: {error_msg}")
    
    def show_progress(self, message):
        self.progress_label.config(text=f"⚡ {message}", fg=self.colors['warning'])
        self.progress_bar.pack(fill="x", pady=5)
        self.progress_bar.start(10)
        self.calculate_btn.config(state="disabled")
    
    def hide_progress(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.config(text="")
        self.calculate_btn.config(state="normal")
    
    def clear_all(self):
        self.number_entry.delete(0, tk.END)
        self.current_result.config(text="🔄 Historial limpiado. Listo para nuevos cálculos...", 
                                  fg=self.colors['text_muted'])
        
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        
        # Restaurar mensaje de bienvenida
        welcome_msg = """🌟 ¡Bienvenido a la Calculadora de Fibonacci Dark Edition! 🌟

💡 Consejos de uso:
• Números pequeños (1-50): ⚡ Cálculo instantáneo
• Números grandes (51-1000): ⏳ Cálculo con advertencia y progreso
• Números muy grandes (>1000): ⚠️ Requieren confirmación especial

🎯 Ejemplos recomendados para probar:
• Fibonacci(10) = 55
• Fibonacci(20) = 6,765
• Fibonacci(30) = 832,040
• Fibonacci(45) = 1,134,903,170

⚡ ¡Comienza ingresando un número arriba!
📊 Los resultados aparecerán aquí abajo...
"""
        self.history_text.insert('1.0', welcome_msg)
        self.history_text.config(state='disabled')
        self.hide_progress()
        self.number_entry.focus()

def main():
    root = tk.Tk()
    
    # Configurar tema dark a nivel de sistema (si es posible)
    try:
        # Intentar usar el tema dark de Windows 10/11
        root.tk.call('tk', 'scaling', 1.0)
        
        # Configurar colores de ventana del sistema
        root.option_add('*TkFDialog*foreground', 'white')
        root.option_add('*TkFDialog*background', '#2d2d2d')
    except:
        pass
    
    app = FibonacciGUI(root)
    
    # Centrar ventana en pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Configurar evento de cierre
    def on_closing():
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

if __name__ == "__main__":
    main()