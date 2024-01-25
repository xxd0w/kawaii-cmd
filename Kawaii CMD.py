import tkinter as tk

def execute_command():
    command = entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"> {command}\n", "input")
    # Add your command execution logic here

    # Append cute face at the end of the output
    output_text.insert(tk.END, "Output: Command executed successfully (⁄ ⁄•⁄ω⁄•⁄ ⁄)\n", "output")

    output_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Kawaii Terminal")
window.configure(bg="#FCE4EC")  # Light pink background

# Entry for user input without yellow background
entry = tk.Entry(window, width=50, font=("Comic Sans MS", 12), fg="#880E4F")  # Dark pink text
entry.pack(pady=10)

# Button to execute command
execute_button = tk.Button(window, text="Execute", command=execute_command, bg="#FF4081", fg="white")  # Pink button
execute_button.pack()

# Text widget to display output
output_text = tk.Text(window, width=80, height=20, font=("Comic Sans MS", 12), bg="#FCE4EC", fg="#880E4F", state=tk.DISABLED)  # Light pink background, dark pink text
output_text.tag_config("input", foreground="#880E4F")  # Dark pink text for input
output_text.tag_config("output", foreground="#880E4F")  # Dark pink text for output
output_text.pack()

# Run the Tkinter event loop
window.mainloop()
