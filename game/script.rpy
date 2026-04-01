# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image mc = "SJN.webp"
image cow = "KBO.png"
image girl1 = "TNP.webp"
image girl2 = "AHR.webp"


# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('김문수', color="#ffc738")
define c = Character('호반우', color="#562e1d")
define g1 = Character('티니핑', color="#ff45c1")
define g2 = Character('아리', color="#bddfff")

# 여기에서부터 게임이 시작합니다.
label start:

    show mc at left
    e "...!!"

    e "아아... 낯선 천장이다..."

    hide mc

    show girl1 at left
    g1 "오빠, 나 믿어?"

    show girl2 at right
    g2 "아니야, 날 믿어 오빠"

    show mc at center
    e "이게 무슨 말일까... 도저히 모르겠다..."
    
    menu:
        "1. 티니핑을 믿기":
            jump girl1

        "2. 아리를 믿기":
            jump girl2
    
    jump hospital

label girl1:

    hide mc
    hide girl1
    hide girl2

    show girl1 at left
    g1 "날 믿어줬구나..."
    return

label girl2:

    hide mc
    hide girl1
    hide girl2

    show girl2 at left
    g2 "날 믿어줬구나..."
    
    hide girl2
    show mc at left
    e "잠깐... 내가 이런 예쁜 여자를 알고 있다고...?"
    jump hospital


label hospital:

    hide mc
    show cow at left
    c "눈을 떴구나..."

    c "다시 감아라..."

    hide cow
    show mc at left
    e "나는 정신을 잃고 말았다..."

    return