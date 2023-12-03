define college_girl = Character("女大")

init:
    image background = im.Scale("background.png", config.screen_width, config.screen_height)

default girl_affection = 0

# 使用艺术字体和边框
init python:
    style.create("affection_text", "default")
    style.affection_text.font = "a.ttf"  # 你的字体文件
    style.affection_text.size = 30
    style.affection_text.color = "#ffffff"
    style.affection_text.outlines = [(2, "#FFC0CB", 0, 0)]  # 粉色边框

screen affection_display():
    text "女大好感度: [girl_affection]" style "affection_text" align (0.01, 0.01)

label start:
    scene background

    show screen affection_display

    "凌晨，男主在宿醉中被老铁的微信消息吵醒，打开微信回复老铁信息，老铁微信透露出男主有个室友但从未见过面，引发好奇。"

    "男主回忆，查看房屋细节。"

    "女大出现，在门外敲门。"

    menu:
        "开门":
            "男主开门，看到了女大。"
            college_girl "你好，我是你的新室友。"
            $ girl_affection += 1
            "女大好感+1。"

        "询问身份":
            "男主在门后问：“你是谁？”"
            college_girl "我是你的新室友。"
            "听到这个声音，男主打开了门。"

    "两人见面，女大行李很多。"

    return
