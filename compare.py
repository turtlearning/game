import random
import tkinter as tk

class Drink:
    def __init__(self, name, cup, temperature, syrup, shot, ice, liquid,
                 steamed_milk=False, topping=None):
        self.name = name                  # 음료 이름
        self.cup = cup                    # 컵 사이즈 (oz 단위)
        self.temperature = temperature    # HOT / ICE
        self.syrup = syrup                # 시럽 종류 또는 None
        self.shot = shot                  # 샷 개수
        self.ice = ice                    # 얼음 유무 (bool)
        self.liquid = liquid              # 물, 우유 등
        self.steamed_milk = steamed_milk  # 스팀 우유 유무
        self.topping = topping            # 시나몬, 휘핑 등

espresso = Drink(
    name="에스프레소(HOT)",
    cup=12,
    temperature="HOT",
    syrup=None,
    shot=None,
    ice=False,
    liquid=False,
    steamed_milk=False,
    topping=None,
)

ice_americano = Drink(
    name="아메리카노(ICE)",
    cup=16,
    temperature="ICE",
    syrup=None,
    shot=None,
    ice=True,
    liquid="물",
    steamed_milk=False,
    topping=None,
)

hot_americano = Drink(
    name="아메리카노(HOT)",
    cup=12,
    temperature="HOT",
    syrup=None,
    shot=None,
    ice=False,
    liquid="물",
    steamed_milk=False,
    topping=None,
)

ice_cafelatte = Drink(
    name="카페라떼(ICE)",
    cup=16,
    temperature="ICE",
    syrup=None,
    shot=None,
    ice=True,
    liquid="우유",
    steamed_milk=False,
    topping=None,
)

hot_cafelatte = Drink(
    name="카페라떼(HOT)",
    cup=12,
    temperature="HOT",
    syrup=None,
    shot=None,
    ice=False,
    liquid="우유",
    steamed_milk=True,
    topping=None,
)

capuccino = Drink(
    name="카푸치노(HOT)",
    cup=12,
    temperature="HOT",
    syrup=None,
    shot=None,
    ice=False,
    liquid="우유",
    steamed_milk=True,
    topping=None,
)

ice_vanilalatte = Drink(
    name="바닐라라떼(ICE)",
    cup=16,
    temperature="ICE",
    syrup="바닐라",
    shot=None,
    ice=True,
    liquid="우유",
    steamed_milk=False,
    topping=None,
)

hot_vanilalatte = Drink(
    name="바닐라라떼(HOT)",
    cup=12,
    temperature="HOT",
    syrup="바닐라",
    shot=None,
    ice=False,
    liquid="우유",
    steamed_milk=True,
    topping=None,
)

ice_cafemocha = Drink(
    name="카페모카(ICE)",
    cup=16,
    temperature="ICE",
    syrup="초콜릿",
    shot=None,
    ice=True,
    liquid="우유",
    steamed_milk=False,
    topping=None,
)

hot_cafemocha = Drink(
    name="카페모카(HOT)",
    cup=12,
    temperature="HOT",
    syrup="초콜릿",
    shot=None,
    ice=False,
    liquid="우유",
    steamed_milk=True,
    topping=None,
)

ice_caramelmacchiato = Drink(
    name="카라멜마끼아또(ICE)",
    cup=16,
    temperature="ICE",
    syrup= {"바닐라", "카라멜"},
    shot=None,
    ice=True,
    liquid="우유",
    steamed_milk=False,
    topping="카라멜",
)

hot_caramelmacchiato = Drink(
    name="카라멜마끼아또(HOT)",
    cup=12,
    temperature="HOT",
    syrup= {"바닐라", "카라멜"},
    shot=None,
    ice=False,
    liquid="우유",
    steamed_milk=True,
    topping="카라멜",
)

drink_menu = {
        espresso,
        ice_americano,
        hot_americano,
        ice_cafelatte,
        hot_cafelatte,
        capuccino,
        ice_vanilalatte,
        hot_vanilalatte,
        ice_cafemocha,
        hot_cafemocha,
        ice_caramelmacchiato,
        hot_caramelmacchiato
}

random_drink = random.choice(list(drink_menu)) #무작위로 음료 뽑뽑기
random_shot = random.randint(1, 3)
shot_density = ""

match random_shot:     #손님의 요청에 따른 샷 조절 
    case 1:
        shot_density = "연하게"
    case 2:
        shot_density = "보통"
    case 3:
        shot_density = "진하게"

player_drink = Drink(
    name=random_drink.name,
    cup=None,
    temperature=None,
    syrup= None,
    shot=shot_density,
    ice=None,
    liquid=None,
    steamed_milk=None,
    topping=None    
)

def update_receipt(random_drink, shot_density):
    receipt_text.set(f"🧾 영수증\n음료 : {random_drink}\n샷 : {shot_density}")

# 기본 셋업
root = tk.Tk()
root.title("커피 제조 게임")
root.geometry("800x600")

receipt_text = tk.StringVar()
receipt_label = tk.Label(root, textvariable=receipt_text, justify="left", anchor="ne", font=("맑은 고딕", 12))
receipt_label.place(relx=0.75, rely=0.05)  

update_receipt(random_drink.name, shot_density)

result_label = tk.Label(root, text="", font=("맑은 고딕", 14))
result_label.place(relx=0.5, rely=0.7, anchor="center")

def select_cup(size):
    player_drink.cup = size
    if size == random_drink.cup:
        result_label.config(text="✔ 통과", fg="green")
        switch_to_making_ui()  # 제조 UI로 변경
    else:
        result_label.config(text="❌ 다시 선택하세요", fg="red")

cup_label = tk.Label(root, text="컵 사이즈를 선택해주세요", font=("맑은 고딕", 14))
cup_label.place(relx=0.05, rely=0.05, anchor="w")

# 🚀 4️⃣ "컵 사이즈 선택" 버튼
button_12oz = tk.Button(root, text="12oz", font=("맑은 고딕", 20), width=10, height=2,
                        command=lambda: select_cup(12))
button_12oz.place(relx=0.3, rely=0.5, anchor="center")

button_16oz = tk.Button(root, text="16oz", font=("맑은 고딕", 20), width=10, height=2,
                        command=lambda: select_cup(16))
button_16oz.place(relx=0.7, rely=0.5, anchor="center")

# 🚀 5️⃣ 제조 UI로 전환하는 함수
current_step = 0  # 현재 단계 인덱스 (0 = 얼음, 1 = 액체, 2 = 시럽, 3 = 샷)
steps = ["HOT / ICE를 정해주세요", "물 / 우유를 정해주세요", "무슨 시럽을 넣을지 정해주세요", "샷을 몇개 넣을지 정해주세요", "토핑을 선택해주세요"]
def switch_to_making_ui():
    global step_label

    # 기존 요소들 숨기기
    button_12oz.place_forget()
    button_16oz.place_forget()
    result_label.place_forget()
    cup_label.place_forget()

    # 🔹 현재 진행 중인 단계 표시
    step_label = tk.Label(root, text=f"{steps[current_step]}", font=("맑은 고딕", 14))
    step_label.place(relx=0.05, rely=0.05, anchor="w")

    # 🔹 진행 단계 버튼 추가 (아래쪽으로 배치)
    step_buttons = [
        ("얼음", 0.4),
        ("액체", 0.5),
        ("시럽", 0.6),
        ("샷", 0.7),
        ("토핑", 0.8)
    ]
    
    for text, pos in step_buttons:
        btn = tk.Button(root, text=text, font=("맑은 고딕", 14), width=8, height=2, command=lambda t=text: next_step(t))
        btn.place(relx=0.05, rely=pos, anchor="w")

    # 중앙에 컵 이미지 (텍스트 대체)
    cup_display = tk.Label(root, text="🧊 진행 상태에 따른 컵 이미지 🧊", font=("맑은 고딕", 16))
    cup_display.place(relx=0.7, rely=0.5, anchor="center")

# 🚀 6️⃣ 다음 단계로 이동하는 함수
def next_step(step_name):
    global current_step
    if step_name == steps[current_step]:  # 현재 단계에 맞는 버튼을 눌렀는지 확인
        current_step += 1
        if current_step < len(steps):
            step_label.config(text=f"현재 단계: {steps[current_step]}")
        else:
            step_label.config(text="☕ 제조 완료!")

option_buttons = []

def clear_option_buttons():
    global option_buttons
    for widget in option_buttons:
        widget.place_forget()
    option_buttons = []

def confirm_step():
    global current_step
    clear_option_buttons()
    current_step += 1
    if current_step < len(steps):
        step_label.config(text=f"현재 단계: {steps[current_step]}")
    else:
        step_label.config(text="☕ 제조 완료!")

# 단계 버튼 클릭 시 동작 연결 함수
def next_step(step_name):
    global current_step
    stage = ["얼음", "액체", "시럽", "샷", "토핑"]
    if step_name != stage[current_step]:
        return
    clear_option_buttons()

    y_pos = {0: 0.4, 1: 0.5, 2: 0.6, 3: 0.7, 4: 0.8}[current_step]

    if current_step == 0:  # 얼음
        def select_ice(value, button):
            player_drink.ice = value
            check_button.place_forget()
            check_button.place(relx=0.40, rely=y_pos)
            check_button.config(state="normal")

        b1 = tk.Button(root, text="넣기", command=lambda: select_ice(True, b1))
        b2 = tk.Button(root, text="안 넣기", command=lambda: select_ice(False, b2))

        b1.place(relx=0.25, rely=y_pos)
        b2.place(relx=0.30, rely=y_pos)

        # ✔ 체크 버튼 미리 생성 후 숨김
        check_button = tk.Button(root, text="✔", command=confirm_step, state="disabled")
        check_button.place(relx=0.45, rely=y_pos)
        check_button.place_forget()

        option_buttons.extend([b1, b2, check_button])


    elif current_step == 1:  # 액체
        def select_liquid(value, button):
            player_drink.liquid = value
            check_button.place_forget()
            check_button.place(relx=0.40, rely=y_pos)
            check_button.config(state="normal")

        b1 = tk.Button(root, text="물", command=lambda: select_liquid("물", b1))
        b2 = tk.Button(root, text="우유", command=lambda: select_liquid("우유", b2))

        b1.place(relx=0.25, rely=y_pos)
        b2.place(relx=0.30, rely=y_pos)

        check_button = tk.Button(root, text="✔", command=confirm_step, state="disabled")
        check_button.place_forget()

        option_buttons.extend([b1, b2, check_button])

    elif current_step == 2:  # 시럽
        def select_syrup(value, button):
            player_drink.syrup = value
            check_button.place_forget()
            check_button.place(relx=0.50, rely=y_pos)
            check_button.config(state="normal")

        b1 = tk.Button(root, text="바닐라", command=lambda: select_syrup("바닐라", b1))
        b2 = tk.Button(root, text="카라멜", command=lambda: select_syrup("카라멜", b2))
        b3 = tk.Button(root, text="초콜릿", command=lambda: select_syrup("초콜릿", b3))
        b4 = tk.Button(root, text="안 넣기", command=lambda: select_syrup(None, b4))

        b1.place(relx=0.20, rely=y_pos)
        b2.place(relx=0.27, rely=y_pos)
        b3.place(relx=0.34, rely=y_pos)
        b4.place(relx=0.41, rely=y_pos)

        check_button = tk.Button(root, text="✔", command=confirm_step, state="disabled")
        check_button.place_forget()

        option_buttons.extend([b1, b2, b3, b4, check_button])

    elif current_step == 3:  # 샷
        shot_value = tk.StringVar(value="2")

        def update_shot_display():
            shot_density_map = {1: "연하게", 2: "보통", 3: "진하게"}
            density = shot_density_map[int(shot_value.get())]
            player_drink.shot = density

        def decrease():
            val = max(1, int(shot_value.get()) - 1)
            shot_value.set(str(val))
            update_shot_display()

        def increase():
            val = min(3, int(shot_value.get()) + 1)
            shot_value.set(str(val))
            update_shot_display()

        b1 = tk.Button(root, text="-", command=decrease)
        label = tk.Label(root, textvariable=shot_value, font=("맑은 고딕", 12))
        b2 = tk.Button(root, text="+", command=increase)
        b3 = tk.Button(root, text="✔", command=lambda: [update_shot_display(), confirm_step()])

        b1.place(relx=0.2, rely=y_pos)
        label.place(relx=0.3, rely=y_pos)
        b2.place(relx=0.4, rely=y_pos)
        b3.place(relx=0.5, rely=y_pos)

        option_buttons.extend([b1, label, b2, b3])
    
    elif current_step == 4:  # ⬅️ 토핑 단계
        def select_topping(value, button):
            player_drink.topping = value
            check_button.place_forget()
            check_button.place(relx=0.55, rely=y_pos)
            check_button.config(state="normal")

        b1 = tk.Button(root, text="시나몬", command=lambda: select_topping("시나몬", b1))
        b2 = tk.Button(root, text="카라멜", command=lambda: select_topping("카라멜", b2))
        b3 = tk.Button(root, text="안 넣기", command=lambda: select_topping(None, b3))

        b1.place(relx=0.25, rely=y_pos)
        b2.place(relx=0.35, rely=y_pos)
        b3.place(relx=0.45, rely=y_pos)

        check_button = tk.Button(root, text="✔", command=confirm_step, state="disabled")
        check_button.place_forget()

        option_buttons.extend([b1, b2, b3, check_button])

# 🎮 실행
root.mainloop()