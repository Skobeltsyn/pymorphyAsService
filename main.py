from fastapi import FastAPI
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/describe_word/{name}")
async def say_hello(name: str):
    data = morph.parse(name)[0]
    print(data.tag)
    res = {"слово": name}
    res["часть речи"] = data.tag.POS
    res["одушевленность"] = data.tag.animacy
    res["вид"] = data.tag.aspect
    res["падеж"] = data.tag.case
    res["род"] = data.tag.gender
    res["включенность в действие"] = data.tag.involvement
    res["наклонение"] = data.tag.mood
    res["число"] = data.tag.number
    res["лицо"] = data.tag.person
    res["время"] = data.tag.tense
    res["переходность"] = data.tag.transitivity
    res["залог"] = data.tag.voice
    res["нормальная форма"] = data.normal_form


    return res
