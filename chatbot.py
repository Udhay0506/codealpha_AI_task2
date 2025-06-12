import tkinter as tk

# Facebook FAQ database
faq_data = {
    "How do I reset my Facebook password?":
        "Go to the login page > Click on 'Forgotten password?' > Follow the instructions to reset it.",
    "How do I deactivate or delete my Facebook account?":
        "Go to Settings & Privacy > Settings > Your Facebook Information > Deactivation and Deletion.",
    "How do I recover a hacked Facebook account?":
        "Go to facebook.com/hacked and follow the on-screen instructions to secure your account.",
    "How do I make my Facebook profile private?":
        "Go to Settings > Privacy > Adjust who can see your posts, profile, and activity.",
    "How do I block or report someone on Facebook?":
        "Go to their profile > Click the three dots > Select Block or Report.",
    "Why was my Facebook post removed?":
        "Posts that violate Facebook's Community Standards may be removed without notice.",
    "How do I change my name on Facebook?":
        "Go to Settings > Personal and Account Information > Name > Edit.",
    "How do I verify my Facebook Page or Profile?":
        "Go to facebook.com/help/contact/342509036134712 to request verification.",
    "Why can't I send friend requests or messages?":
        "You may have reached a friend limit, or your account might be temporarily restricted.",
    "How do I check if Facebook is down?":
        "Use sites like downdetector.com or check Facebook's official social media pages for updates."
}

# GUI setup
root = tk.Tk()
root.title("📘 Facebook FAQ Chatbot")
root.geometry("700x520")
root.configure(bg="#e0f7fa")  # Light teal background

# Title label
title_label = tk.Label(
    root,
    text="Facebook FAQ Chatbot",
    font=("Segoe UI", 20, "bold"),
    bg="#e0f7fa",
    fg="#212121"
)
title_label.pack(pady=15)

# Dropdown menu
question_var = tk.StringVar(root)
question_var.set("Select a question")

def show_dropdown_answer(*args):
    selected = question_var.get()
    if selected in faq_data:
        response_label.config(text="Bot: " + faq_data[selected])
    else:
        response_label.config(text="")

dropdown = tk.OptionMenu(root, question_var, *faq_data.keys())
dropdown.config(width=70, font=("Segoe UI", 11), bg="white", fg="#212121")
dropdown.pack(pady=10)

question_var.trace("w", show_dropdown_answer)

# Response label
response_label = tk.Label(
    root,
    text="",
    wraplength=650,
    font=("Segoe UI", 12),
    fg="#212121",
    bg="#e0f7fa",
    justify="left"
)
response_label.pack(pady=20)

# Manual question entry
entry_label = tk.Label(
    root,
    text="Or ask your own question below:",
    font=("Segoe UI", 12),
    bg="#e0f7fa",
    fg="#212121"
)
entry_label.pack()

manual_entry = tk.Entry(root, font=("Segoe UI", 12), width=80, bg="white", fg="#212121")
manual_entry.pack(pady=5)

# Ask button
def answer_manual_question():
    user_question = manual_entry.get().strip().lower()
    found = False
    for q, a in faq_data.items():
        if user_question in q.lower():
            response_label.config(text="Bot: " + a)
            found = True
            break
    if not found:
        response_label.config(text="Bot: Sorry, I don't have an answer for that.")

ask_btn = tk.Button(
    root,
    text="Ask",
    command=answer_manual_question,
    font=("Segoe UI", 12),
    bg="#4dd0e1",  # Teal button
    fg="black",
    activebackground="#26c6da"
)
ask_btn.pack(pady=15)

root.mainloop()
