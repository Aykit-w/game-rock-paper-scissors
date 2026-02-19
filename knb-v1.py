import tkinter as tk
from tkinter import messagebox
import random

ICON_PATHS = {
    "камень": "stone.png",
    "ножницы": "scissors.png",
    "бумага": "paper.png"
}

CHOICES = list(ICON_PATHS.keys())
RESULTS = {
    ("камень", "ножницы"): "Победа!",
    ("бумага", "камень"): "Победа!",
    ("ножницы", "бумага"): "Победа!",
    ("камень", "бумага"): "Проигрыш",
    ("бумага", "ножницы"): "Проигрыш",
    ("ножницы", "камень"): "Проигрыш"
}

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Камень-Ножницы-Бумага')
        self.geometry('600x600')
        self.configure(bg="#153ddc")

        frame_title = tk.Frame(self, bg="#ffffff")
        frame_buttons = tk.Frame(self, bg="#153ddc")
        frame_result = tk.Frame(self, bg="#E71111")
        frame_stats = tk.Frame(self, bg="#153ddc")

        title_label = tk.Label(frame_title, text="Камень-Ножницы-Бумага",
                              font=("Arial Bold", 20),
                              fg="#121111", bg="#FFFFFF")
        title_label.pack(padx=10, pady=10)
        frame_title.pack(side="top", fill="x")

        self.result_label = tk.Label(frame_result,
                                    text="Сделайте свой выбор",
                                    font=("Helvetica", 14),
                                    fg="#000000", bg="#E71111")
        self.result_label.pack(pady=10)
        frame_result.pack(side="bottom", fill="x")

        self.wins_label = tk.Label(frame_stats, text="Победы: 0", font=("Helvetica", 12), fg="white", bg="#153ddc")
        self.wins_label.pack(pady=2)
        self.losses_label = tk.Label(frame_stats, text="Поражения: 0", font=("Helvetica", 12), fg="white", bg="#153ddc")
        self.losses_label.pack(pady=2)
        self.current_streak_label = tk.Label(frame_stats, text="Текущая серия побед: 0", font=("Helvetica", 12), fg="white", bg="#153ddc")
        self.current_streak_label.pack(pady=2)
        self.longest_streak_label = tk.Label(frame_stats, text="Рекорд серии побед: 0", font=("Helvetica", 12), fg="white", bg="#153ddc")
        self.longest_streak_label.pack(pady=2)
        frame_stats.pack(side="bottom", fill="x", pady=10)

        buttons = []
        icons = [
            "\U0001F44A",
            "\U00002702",
            "\U0001F4C4"
        ]

        for i, choice in enumerate(CHOICES):
            btn = tk.Button(
                frame_buttons,
                text=f"{icons[i]} {choice}",
                width=15,
                height=3,
                font=("Helvetica", 12),
                relief="raised",
                borderwidth=2,
                command=lambda ch=choice: self.play_round(ch)
            )
            btn.pack(side="left", padx=10, pady=10)
            buttons.append(btn)

        frame_buttons.pack(expand=True)

        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.current_streak = 0
        self.longest_streak = 0

    def animate_icon(self, icon_path):
        canvas_width = 600
        canvas_height = 500
        try:
            image_file = tk.PhotoImage(file=icon_path)
        except tk.TclError:
            messagebox.showerror("Ошибка", f"Изображение не найдено: {icon_path}. Убедитесь, что файлы .png находятся в той же директории, что и скрипт.")
            return

        img_id = None

        def move_image():
            nonlocal img_id
            y_pos = canvas_height + 50
            step_size = 10

            while y_pos > 0:
                canvas.delete(img_id)
                img_id = canvas.create_image(canvas_width // 2, y_pos, anchor='center', image=image_file)
                canvas.update()
                y_pos -= step_size
                canvas.after(50)

        canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, bg='#153ddc', highlightthickness=0)
        canvas.place(x=0, y=0)
        move_image()

        self.wins_label.config(text=f"Победы: {self.wins}")
        self.losses_label.config(text=f"Поражения: {self.losses}")
        self.ties_label.config(text=f"Ничьи: {self.ties}")

    def play_round(self, player_choice):
        comp_choice = random.choice(CHOICES)
        result_message = ""
        game_outcome = ""

        if player_choice == comp_choice:
            result_message = f"Ничья! Оба выбрали {player_choice}"
            game_outcome = "Ничья!"
        else:
            game_result = RESULTS.get((player_choice, comp_choice))
            if game_result == "Победа!":
                result_message = f"Победа!\n\nВаш выбор: {player_choice}\nКомпьютер: {comp_choice}"
                game_outcome = "Победа!"
            else:
                result_message = f"Проигрыш\n\nВаш выбор: {player_choice}\nКомпьютер: {comp_choice}"
                game_outcome = "Проигрыш"

        self.animate_icon(ICON_PATHS[player_choice])
        self.result_label.config(text=result_message)
        self.update_stats(game_outcome)

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()