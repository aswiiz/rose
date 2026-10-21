import math as m
import random as r
import tkinter as tk
import tkinter.font as tkf

W, H = 800, 800
DURATION = 10
TICK = 16
ANIM = 38
LIFT = 32
GAP = 3
BG = "#060208"
FONT_FALLBACKS = ("Georgia", "Times New Roman", "Arial")
SEED = 17

PHRASES = [
    "I LOVE YOU", "I love you", "Te amo", "Ti amo", "Je t'aime",
    "Ich liebe dich", "Eu te amo", "Seni seviyorum", "Я тебя люблю",
    "사랑해", "愛してる", "我爱你", "मैं तुमसे प्यार करती हूँ",
    "मैं तुमसे प्यार करता हूँ", "Σ' αγαπώ", "Ik hou van jou",
    "Jag älskar dig", "Kocham cię", "ฉันรักคุณ", "Anh yêu em",
    "Aku cinta kamu", "Mahal kita", "אני אוהבת אותך", "أحبك",
    "నేను నిన్ను ప్రేమిస్తున్నాను", "நான் உன்னை காதலிக்கிறேன்",
    "আমি তোমাকে ভালোবাসি", "Volim te", "Te iubesc", "Ljubim te",
    "Nakupenda", "Я тебе кохаю", "Miluji tě", "Szeretlek",
    "Rakastan sinua", "Jeg elsker dig"
]

ACCENTS = [
    "LOVE", "TE AMO", "AMOUR", "TI AMO", "I LOVE YOU", "AMOR",
    "愛してる", "사랑해", "我爱你", "LOVE YOU", "JE T'AIME",
    "SZERETLEK", "NAKUPENDA"
]

SHORT_PHRASES = [
    "Te amo", "Ti amo", "AMOR", "LOVE", "愛してる", "사랑해", "我爱你",
    "Amour", "I love you", "Mahal kita", "Te iubesc", "Volim te",
    "Szeretlek", "Miluji tě", "Nakupenda"
]

HEAD_WORDS = PHRASES + [
    "LOVE", "LOVE", "LOVE YOU", "AMOR", "AMOR", "AMOUR", "AMOUR",
    "AMORE", "LIEBE", "TE AMO", "TE AMO", "TI AMO", "TI AMO",
    "TE QUIERO", "TE QUIERO", "JE T'AIME", "I LOVE YOU", "I LOVE YOU",
    "愛", "愛してる", "愛してる", "사랑", "사랑해", "사랑해", "我爱你",
    "Mahal kita", "รักคุณ", "ANH YÊU EM", "तुमसे प्यार है",
    "నిన్ను ప్రేమిస్తున్నా", "உன்னை காதலிக்கிறேன்", "ভালোবাসি",
    "أحبك", "LOVE", "AMOR", "AMOUR", "Nakupenda", "Szeretlek"
]

HEAD_SIZES = (7, 8, 9, 10, 11, 12, 13, 14)
HEAD_WEIGHTS = (2, 4, 5, 5, 4, 2, 1, 0.5)
SMALL_SIZES = (6, 7, 8, 9)

rng = r.Random(SEED)

def ellipse_poly(cx, cy, rx, ry, points=160):
    return [
        (cx + rx * m.cos(2 * m.pi * i / points),
         cy + ry * m.sin(2 * m.pi * i / points))
        for i in range(points)
    ]

HEAD_SHAPES = [
    ellipse_poly(400, 180, 145, 90),
    ellipse_poly(330, 180, 120, 83),
    ellipse_poly(470, 180, 120, 83),
    ellipse_poly(275, 260, 98, 112),
    ellipse_poly(525, 260, 98, 112),
    ellipse_poly(338, 325, 118, 126),
    ellipse_poly(462, 325, 118, 126),
    [(230, 330), (290, 365), (348, 414), (400, 532),
     (452, 414), (510, 365), (570, 330), (522, 452),
     (400, 542), (278, 452)],
]

STEM = [(378, 493), (422, 493), (427, 752), (408, 772),
        (390, 760), (374, 600)]
LEFT_LEAF = [(395, 594), (359, 554), (304, 535), (244, 541),
             (215, 562), (253, 609), (321, 631), (374, 617)]
RIGHT_LEAF = [(406, 619), (442, 581), (491, 561), (553, 578),
              (578, 600), (535, 640), (476, 660), (425, 649)]

root = tk.Tk()
root.title("A Rose Written in Every Language")
root.configure(bg=BG)
root.resizable(False, False)
canvas = tk.Canvas(root, width=W, height=H, bg=BG, highlightthickness=0)
canvas.pack()

try:
    available_families = {name.lower(): name for name in tkf.families(root)}
except tk.TclError:
    available_families = {}

family_cache = {}
font_cache = {}

def has_any(text, lo, hi):
    return any(lo <= ord(ch) <= hi for ch in text)

def choose_family(text):
    if has_any(text, 0xAC00, 0xD7AF):
        candidates = ("Malgun Gothic", "Noto Sans CJK KR", "Arial Unicode MS")
    elif has_any(text, 0x3040, 0x30FF):
        candidates = ("Yu Gothic UI", "Meiryo", "Noto Sans CJK JP", "Arial Unicode MS")
    elif has_any(text, 0x4E00, 0x9FFF):
        candidates = ("Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS")
    elif has_any(text, 0x0900, 0x097F):
        candidates = ("Nirmala UI", "Mangal", "Noto Sans Devanagari")
    elif has_any(text, 0x0980, 0x09FF):
        candidates = ("Nirmala UI", "Vrinda", "Noto Sans Bengali")
    elif has_any(text, 0x0C00, 0x0C7F):
        candidates = ("Gautami", "Nirmala UI", "Noto Sans Telugu")
    elif has_any(text, 0x0B80, 0x0BFF):
        candidates = ("Latha", "Noto Sans Tamil")
    elif has_any(text, 0x0E00, 0x0E7F):
        candidates = ("Leelawadee UI", "Noto Sans Thai")
    elif has_any(text, 0x0600, 0x06FF):
        candidates = ("Segoe UI", "Arial", "Noto Sans Arabic")
    elif has_any(text, 0x0590, 0x05FF):
        candidates = ("Arial", "Noto Sans Hebrew")
    elif has_any(text, 0x0370, 0x03FF):
        candidates = ("Georgia", "Arial")
    elif has_any(text, 0x0400, 0x04FF):
        candidates = ("Georgia", "Arial", "Segoe UI")
    else:
        candidates = FONT_FALLBACKS
    for name in candidates:
        if name.lower() in available_families:
            return available_families[name.lower()]
    return available_families.get("arial", "Arial")

def font_for(text, size):
    family = choose_family(text)
    key = (family, size)
    if key not in font_cache:
        font_cache[key] = tkf.Font(
            root=root, family=family, size=size, weight="bold"
        )
    return font_cache[key]

def hx(rgb):
    return "#%02x%02x%02x" % tuple(
        int(max(0, min(1, c)) * 255) for c in rgb
    )

def clamp(v):
    return max(0.0, min(1.0, v))

def mix(a, b, k):
    return tuple(x + (y - x) * k for x, y in zip(a, b))

def rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) / 255 for i in (0, 2, 4))

BGC = rgb(BG)

def polygon_spans(poly, y):
    xs = []
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 <= y < y2) or (y2 <= y < y1):
            if y2 != y1:
                xs.append(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
    xs.sort()
    return list(zip(xs[0::2], xs[1::2]))

def merge_spans(spans):
    if not spans:
        return []
    spans = sorted(spans)
    merged = [list(spans[0])]
    for lo, hi in spans[1:]:
        if lo <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    return [(a, b) for a, b in merged]

def shape_spans(polygons, y):
    raw = []
    for poly in polygons:
        raw.extend(polygon_spans(poly, y))
    return merge_spans(raw)

def intersect_spans(a_spans, b_spans, minimum=15):
    out = []
    for a in a_spans:
        for b in b_spans:
            lo, hi = max(a[0], b[0]), min(a[1], b[1])
            if hi - lo >= minimum:
                out.append((lo, hi))
    return merge_spans(out)

def rose_color(x, y, size, edge=False):
    dx, dy = (x - 400) / 210, (y - 300) / 220
    rad = m.sqrt(dx * dx + dy * dy)
    if rad > 0.82:
        palette = ["#8f0b2b", "#ae1238", "#c41d48", "#d52b53"]
    elif rad > 0.48:
        palette = ["#b9143d", "#d21e49", "#e33b60", "#f04e73"]
    else:
        palette = ["#c51b49", "#e83c68", "#f16b8b", "#ff91a9"]
    if edge:
        palette += ["#f5a0b3", "#ef6488"]
    if size >= 14:
        palette += ["#ff9ab1", "#ffd0dc"]
    return rgb(rng.choice(palette))

def green_color(x, y, size, edge=False):
    palette = ["#3e8034", "#559c3c", "#72b84b", "#91cf62", "#b1e184"]
    if size >= 9:
        palette += ["#a7d486", "#c0e19a"]
    return rgb(rng.choice(palette))

phrase_cycles = {}

def phrase_from_pool(pool_name, size):
    pool = ACCENTS if size >= 14 else (SHORT_PHRASES if pool_name != "head" else HEAD_WORDS)
    key = (pool_name, "accent" if size >= 14 else "normal")
    if key not in phrase_cycles or not phrase_cycles[key]["items"]:
        items = pool[:]
        rng.shuffle(items)
        phrase_cycles[key] = {"items": items, "index": 0}
    state = phrase_cycles[key]
    phrase = state["items"][state["index"]]
    state["index"] += 1
    if state["index"] >= len(state["items"]):
        state["items"] = []
    return phrase

def size_for(pool_name):
    if pool_name == "head":
        return rng.choices(HEAD_SIZES, weights=HEAD_WEIGHTS, k=1)[0]
    return rng.choice((6, 7, 8) if pool_name == "stem" else (7, 8, 9, 10))

def color_for(x, y, size, kind, edge=False):
    if kind == "head":
        return rose_color(x, y, size, edge)
    return green_color(x, y, size, edge)

def build_region(polygons, y_start, y_end, row_h, kind):
    placed = []
    half = row_h / 2
    y = y_start + half

    while y < y_end - half:
        top = shape_spans(polygons, y - half + 1)
        bottom = shape_spans(polygons, y + half - 1)
        row = intersect_spans(top, bottom, minimum=19 if kind == "head" else 16)

        for lo, hi in row:
            margin = 3 if kind == "head" else 1
            lo += margin
            hi -= margin
            available = hi - lo
            if available < 18:
                continue

            line = []
            cur = lo + rng.uniform(0, min(3, max(1, available * 0.02)))
            while cur < hi - 15:
                remaining = hi - cur
                candidates = []
                target_width = min(74, max(19, remaining * 0.22))
                tries = 45 if kind == "head" else 55
                for _ in range(tries):
                    size = size_for(kind)
                    text = phrase_from_pool(kind, size)
                    font = font_for(text, size)
                    width = font.measure(text)
                    if width <= remaining and width >= min(18, remaining * 0.20):
                        score = abs(width - target_width) + rng.uniform(0, 13)
                        candidates.append((score, text, size, width))
                if not candidates:
                    break
                candidates.sort(key=lambda item: item[0])
                pick = rng.choice(candidates[:min(4, len(candidates))])
                _, text, size, width = pick
                line.append({
                    "x": cur + width / 2,
                    "y": y,
                    "text": text,
                    "size": size,
                    "width": width,
                    "kind": kind,
                })
                cur += width + (GAP if kind == "head" else 1)

            if not line:
                continue

            used = sum(item["width"] for item in line) + max(0, len(line) - 1) * (GAP if kind == "head" else 1)
            slack = max(0, available - used)
            extra = slack / max(1, len(line) - 1) if len(line) > 1 else 0
            for i, item in enumerate(line):
                item["x"] += extra * i
                item["edge"] = (i == 0 or i == len(line) - 1)
                item["color"] = color_for(
                    item["x"], item["y"], item["size"], kind, item["edge"]
                )
                placed.append(item)
        y += row_h

    return placed

head_row_h = max(font_for("I LOVE YOU", s).metrics("linespace") for s in (9, 10, 11)) + 1
leaf_row_h = max(font_for("Te amo", s).metrics("linespace") for s in (7, 8, 9)) + 1
stem_row_h = max(font_for("Te amo", s).metrics("linespace") for s in (6, 7, 8)) + 1

placed = []
placed += build_region(HEAD_SHAPES, 88, 540, head_row_h, "head")
placed += build_region([LEFT_LEAF], 543, 618, leaf_row_h, "leaf")
placed += build_region([RIGHT_LEAF], 575, 651, leaf_row_h, "leaf")
placed += build_region([STEM], 492, 773, stem_row_h, "stem")

outer = [p for p in placed if p["edge"]]
inner = [p for p in placed if not p["edge"]]
outer.sort(key=lambda p: m.atan2(p["y"] - 300, p["x"] - 400) % (2 * m.pi))
inner.sort(key=lambda p: rng.random())
ORDER = outer + inner

active = []
all_main_items = []

def spawn(p):
    x, y = p["x"], p["y"]
    size, text, color = p["size"], p["text"], p["color"]
    font = font_for(text, size)
    shadow = canvas.create_text(x + 1, y + 2, text=text, font=font, fill=BG)
    halo = canvas.create_text(x, y, text=text, font=font, fill=BG)
    main = canvas.create_text(x, y - LIFT, text=text, font=font, fill=BG)
    p.update({
        "shadow": shadow, "halo": halo, "main": main,
        "frame": 0, "dx": rng.uniform(-6, 6),
    })
    all_main_items.append((main, color))
    active.append(p)

def animate(p):
    p["frame"] += 1
    u = clamp(p["frame"] / ANIM)
    eased = 1 - (1 - u) ** 3
    color = p["color"]
    x, y = p["x"], p["y"]
    px = x + p["dx"] * (1 - eased)
    py = y - LIFT * (1 - eased)

    canvas.itemconfig(p["shadow"], fill=hx(mix(BGC, tuple(c * 0.23 for c in color), eased)))
    canvas.itemconfig(p["halo"], fill=hx(mix(BGC, tuple(c * 0.30 for c in color), eased * eased)))
    canvas.coords(p["shadow"], px + 1, py + 2)
    canvas.coords(p["halo"], px, py)

    flash = 0.55 * m.sin(m.pi * clamp((u - 0.58) / 0.42))
    col = mix(mix(BGC, color, eased ** 1.35), (1.0, 0.83, 0.88), flash)
    canvas.itemconfig(p["main"], fill=hx(col))
    canvas.coords(p["main"], px, py)

    if u >= 1:
        canvas.coords(p["halo"], x, y)
        canvas.coords(p["main"], x, y)
        canvas.itemconfig(p["main"], fill=hx(color))
        return False
    return True

def shimmer():
    if all_main_items:
        item, color = rng.choice(all_main_items)
        try:
            canvas.itemconfig(item, fill=hx(mix(color, (1.0, 0.82, 0.88), 0.55)))
            root.after(210, lambda i=item, c=color: safe_restore(i, c))
        except tk.TclError:
            pass
    root.after(145, shimmer)

def safe_restore(item, color):
    try:
        canvas.itemconfig(item, fill=hx(color))
    except tk.TclError:
        pass

items = iter(ORDER)
rate = len(ORDER) / max(1, (DURATION * 1000 / TICK))
acc = 0.0
spawning = True

def step():
    global spawning, acc
    if spawning:
        acc += rate
        while acc >= 1:
            acc -= 1
            try:
                spawn(next(items))
            except StopIteration:
                spawning = False
                break
    active[:] = [p for p in active if animate(p)]
    if not spawning and not active:
        shimmer()
        # Once the rose has finished blooming, reveal the love letter.
        root.after(1800, show_love_letter)
        return
    root.after(TICK, step)


def show_love_letter():
    letter = tk.Toplevel(root)
    letter.title("A Letter From My Heart")
    letter.configure(bg="#fff4f6")
    letter.geometry("560x620")
    letter.resizable(False, False)
    letter.transient(root)
    letter.grab_set()

    outer = tk.Frame(letter, bg="#fff4f6", padx=28, pady=24)
    outer.pack(fill="both", expand=True)

    tk.Label(
        outer, text="♡  A LETTER FROM MY HEART  ♡",
        bg="#fff4f6", fg="#a61b45",
        font=("Georgia", 15, "bold")
    ).pack(pady=(0, 16))

    message = (
        "My love,\\n\\n"
        "If I could gather every beautiful word in every language, "
        "I still don't think they could fully explain what you mean to me. "
        "That's why I made this rose for you—each little phrase is a "
        "piece of the love I carry in my heart.\\n\\n"
        "You make ordinary moments feel special. Your smile brings me "
        "comfort, your laughter makes my day brighter, and being close "
        "to you is one of my favourite feelings. I love you for who you "
        "are, and I want to keep learning, growing, and making memories "
        "with you.\\n\\n"
        "So today, I want to ask you something from the bottom of my heart…\\n\\n"
        "Will you be my girlfriend, and let me keep loving you, caring "
        "for you, and choosing you—one day at a time?\\n\\n"
        "There is no pressure to answer right away. Whatever you feel, "
        "I want you to feel safe, respected, and truly loved.\\n\\n"
        "With all my love,\\n"
        "Your boy ♡"
    )

    text_box = tk.Text(
        outer, wrap="word", height=17, width=54,
        bg="#fffaf9", fg="#40212b", relief="flat",
        padx=16, pady=14, font=("Georgia", 11),
        spacing1=3, spacing3=7
    )
    text_box.insert("1.0", message)
    text_box.configure(state="disabled")
    text_box.pack(fill="both", expand=True, pady=(0, 16))

    buttons = tk.Frame(outer, bg="#fff4f6")
    buttons.pack()

    def answer_yes():
        response = tk.Toplevel(letter)
        response.title("♡")
        response.configure(bg="#fff4f6")
        response.geometry("360x170")
        tk.Label(
            response,
            text="You just made my heart so happy!\\nI love you. ♡",
            bg="#fff4f6", fg="#a61b45",
            font=("Georgia", 14, "bold"),
            justify="center"
        ).pack(expand=True, padx=20, pady=20)
        tk.Button(
            response, text="♡", command=response.destroy,
            bg="#a61b45", fg="white", relief="flat",
            padx=20, pady=6
        ).pack(pady=(0, 16))

    tk.Button(
        buttons, text="Yes, my love ♡", command=answer_yes,
        bg="#a61b45", fg="white", activebackground="#c42d59",
        activeforeground="white", relief="flat",
        font=("Georgia", 11, "bold"), padx=18, pady=9
    ).pack(side="left", padx=6)

    tk.Button(
        buttons, text="I need a little time",
        command=letter.destroy,
        bg="#f2dce2", fg="#6d3042",
        activebackground="#e8c6d1", relief="flat",
        font=("Georgia", 10), padx=14, pady=9
    ).pack(side="left", padx=6)


root.after(200, step)
root.mainloop()