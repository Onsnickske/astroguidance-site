from flask import Flask, render_template, request, url_for
from content import COMMON_TEXTS, PAGE_CONTENT

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def change_lang(lang_code):
        # start with view args (like /reports/<id> — we don’t have those now, but good practice)
        args = request.view_args.copy() if request.view_args else {}

        # also include query args (?foo=1)
        args.update(request.args.to_dict())

        # override lang
        args["lang"] = lang_code

        # build the final URL
        return url_for(request.endpoint, **args)
    return dict(change_lang=change_lang)


def get_lang():
    lang = request.args.get("lang", "en")
    if lang not in COMMON_TEXTS:
        lang = "en"
    return lang


@app.route("/")
def home():
    lang = get_lang()
    return render_template(
        "home.html",
        page="home",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["home"][lang],
        reports=PAGE_CONTENT["reports"][lang],   # 👈 add this
    )



@app.route("/about")
def about():
    lang = get_lang()
    return render_template(
        "about.html",
        page="about",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["about"][lang],
    )


@app.route("/reports")
def reports():
    lang = get_lang()
    return render_template(
        "reports.html",
        page="reports",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["reports"][lang],
    )


@app.route("/book", methods=["GET", "POST"])
def book():
    lang = get_lang()
    booked = False
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        topic = request.form.get("topic", "")
        with open("bookings.txt", "a", encoding="utf-8") as f:
            f.write(f"[{lang}] {name} / {email} / {topic}\n")
        booked = True

    return render_template(
        "book.html",
        page="book",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["book"][lang],
        booked=booked,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    lang = get_lang()
    sent = False
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        message = request.form.get("message", "")
        with open("contact_messages.txt", "a", encoding="utf-8") as f:
            f.write(f"[{lang}] {name} / {email}\n{message}\n\n")
        sent = True

    return render_template(
        "contact.html",
        page="contact",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["contact"][lang],
        sent=sent,
    )


# old URL → send to new page, just in case
@app.route("/natal-charts")
def old_natal():
    lang = get_lang()
    return render_template(
        "reports.html",
        page="reports",
        lang=lang,
        texts=COMMON_TEXTS[lang],
        content=PAGE_CONTENT["reports"][lang],
    )


if __name__ == "__main__":
    app.run(debug=False)
