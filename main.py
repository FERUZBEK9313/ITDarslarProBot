from aiogram import Bot, Dispatcher, types
from aiogram.types import *
from aiogram.utils import executor
from pymongo import MongoClient

TOKEN = "5812422308:AAHjqSz4opcX7WUF_541Q-COj-rfiJ2vq80"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# -----database MONGOBD ---------------------------
myclient = MongoClient("mongodb+srv://feruzbek:user12345@cluster0.xvsb8gx.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["darslar"]
yonalish = mydb["categories"]
peoples = mydb["users"]
autor = mydb['autors']
ttype = mydb['types']
src = mydb['sources'] 




# -----variables------------------------
add_cate = False
del_cate = False

add_autor = False
del_autor = False

add_type = False
del_type = False

add_video = False
del_video = False

metka = 1

cancel = ReplyKeyboardMarkup(resize_keyboard=True).row("Bekor qilish")

# ------ function -----------------------
def add_user():
    global users
    users = []
    x = peoples.find()
    for i in x:
        users.append(i["id"])
    
def btn_categore():
    global categories, buttons, buttons_admin, del_cate_btn
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    del_cate_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    categories = []
    x = yonalish.find()
    for i in x:
        categories.append(i["name"])
    if len(categories)%2 == 0:
        for i in range(0, len(categories), 2):
            buttons.add(categories[i], categories[i+1])
            del_cate_btn.add(categories[i], categories[i+1])
            buttons_admin.add(categories[i], categories[i+1])
            
    else:
        for i in range(0, len(categories)-1, 2):
            buttons.add(categories[i], categories[i+1])
            del_cate_btn.add(categories[i], categories[i+1])
            buttons_admin.add(categories[i], categories[i+1])
        buttons.add(categories[len(categories)-1])
        del_cate_btn.add(categories[len(categories)-1])
        buttons_admin.add(categories[len(categories)-1])
    buttons_admin.add("Yo'nalish qo'shish", "Yo'nalishni o'chirish")
    buttons.add("📊 Statistika")
    buttons_admin.add("📊 Statistika")
    
    del_cate_btn.add('Bekor qilish')




def btn_autor(type):
    global autors, autor_btn, autor_btn_admin, del_autor_btn
    autors = []
    autor_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    del_autor_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    autor_btn_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    x = autor.find()
    for i in x:
        if i['type'] == type:
            autors.append(i["name"])
    if len(autors)%2 == 0:
        for i in range(0, len(autors), 2):
            autor_btn.add(autors[i], autors[i+1])
            del_autor_btn.add(autors[i], autors[i+1])
            autor_btn_admin.add(autors[i], autors[i+1])
            
    else:
        for i in range(0, len(autors)-1, 2):
            autor_btn.add(autors[i], autors[i+1])
            del_autor_btn.add(autors[i], autors[i+1])
            autor_btn_admin.add(autors[i], autors[i+1])
        autor_btn.add(autors[len(autors)-1])
        del_autor_btn.add(autors[len(autors)-1])
        autor_btn_admin.add(autors[len(autors)-1])
    autor_btn_admin.add("Muallif qo'shish", "Muallifni o'chirish")
    autor_btn.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    autor_btn_admin.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    del_autor_btn.add("Bekor qilish")




def btn_type(categor):
    global ttypes, type_btn, type_btn_admin, del_type_btn
    ttypes = []
    type_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    del_type_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    type_btn_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    x = ttype.find()
    if categor != 'null':
        for i in x:
            if i['categor'] == categor:
                ttypes.append(i["name"])
    else:
        for i in x:
            ttypes.append(i["name"])
    if len(ttypes)%2 == 0:
        for i in range(0, len(ttypes), 2):
            del_type_btn.add(ttypes[i], ttypes[i+1])
            type_btn.add(ttypes[i], ttypes[i+1])
            type_btn_admin.add(ttypes[i], ttypes[i+1])
            
    else:
        for i in range(0, len(ttypes)-1, 2):
            del_type_btn.add(ttypes[i], ttypes[i+1])
            type_btn.add(ttypes[i], ttypes[i+1])
            type_btn_admin.add(ttypes[i], ttypes[i+1])
        del_type_btn.add(ttypes[len(ttypes)-1])
        type_btn.add(ttypes[len(ttypes)-1])
        type_btn_admin.add(ttypes[len(ttypes)-1])
    type_btn_admin.add("Tur qo'shish", "Turni o'chirish")
    type_btn_admin.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    type_btn.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    del_type_btn.add("Bekor qilish")



def btn_video(autor):
    global videos, video_btn, video_btn_admin, del_video_btn
    videos = []
    video_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    del_video_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    video_btn_admin = ReplyKeyboardMarkup(resize_keyboard=True)
    x = src.find()
    for i in x:
        if i['autor'] == autor:
            videos.append(i["name"])
    if len(videos)%2 == 0:
        for i in range(0, len(videos), 2):
            del_video_btn.add(videos[i], videos[i+1])
            video_btn.add(videos[i], videos[i+1])
            video_btn_admin.add(videos[i], videos[i+1])
            
    else:
        for i in range(0, len(videos)-1, 2):
            del_video_btn.add(videos[i], videos[i+1])
            video_btn.add(videos[i], videos[i+1])
            video_btn_admin.add(videos[i], videos[i+1])
        del_video_btn.add(videos[len(videos)-1])
        video_btn.add(videos[len(videos)-1])
        video_btn_admin.add(videos[len(videos)-1])
    video_btn_admin.add("Video qo'shish", "Videoni o'chirish")
    video_btn_admin.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    video_btn.add("🔙 Orqaga", "🔝 Asosiy Menyu")
    

    del_video_btn.add("Bekor qilish")


#---------------asosiy-------------------
@dp.message_handler(commands=["start"])
async def start(message: types.Message):

    add_user()
    btn_categore()
    if message.from_user.username == 'Feruzbek_Sapayev':
        await message.answer(f"👋 Assalomu aleykum Feruzbek. Siz ADMIN siz. *IT Darslar Pro Bot* ga _XUSH KELIBSIZ!_.\nMarhamat, quyidagi bo'limlardan birini tanlang.",reply_markup=buttons_admin, parse_mode="Markdown")
    else:
        if not(message.from_user.id in users):
            data = {'id': message.from_user.id}
            peoples.insert_one(data)
        await message.answer(f"👋 Assalomu aleykum {message.from_user.first_name}. *IT Darslar Pro Bot* ga _XUSH KELIBSIZ!_.\nMarhamat, quyidagi bo'limlardan birini tanlang.",reply_markup=buttons, parse_mode="Markdown")


@dp.message_handler()
async def events(message: types.Message):
    global add_cate, del_cate, add_autor, del_autor, add_type, del_type, add_video, del_video, categor_name, type_name, autor_name, metka

# -------------------- Categoriya -----------------------------------------------
    if message.text == "Yo'nalish qo'shish" and message.from_user.username == 'Feruzbek_Sapayev':
        add_cate = True
        await message.answer("Yo'nalish nomini kiriting.", reply_markup=cancel)

    elif add_cate and message.text != "Yo'nalish qo'shish" and not(message.text in categories) and message.from_user.username == 'Feruzbek_Sapayev':
        if message.text == "Bekor qilish":
            add_cate = False
            await message.answer("Bekor qilindi.", reply_markup=buttons_admin)
        else:
            name = {'name':message.text}
            yonalish.insert_one(name)
            btn_categore()
            add_cate = False
            await message.answer("Yo'nalish muvaffaqiyatli qo'shildi.", reply_markup= buttons_admin)
            

    elif message.text == "Yo'nalishni o'chirish" and message.from_user.username == 'Feruzbek_Sapayev':
        del_cate = True
        await message.answer("Yo'nalish nomini tanlang.", reply_markup=del_cate_btn)

    elif del_cate:
        if message.text == "Bekor qilish":
            del_cate = False
            await message.answer("Bekor qilindi.", reply_markup=buttons_admin)
        else:
            if message.text in categories and message.from_user.username == 'Feruzbek_Sapayev':
                name = {'name':message.text}
                cate = {'categor': message.text}
                
                yonalish.delete_one(name)
                ttype.delete_many(cate)
                autor.delete_many(cate)
                src.delete_many(cate)
                btn_categore()
    
                del_cate = False
                await message.answer("Yo'nalish muvaffaqiyatli o'chirildi.", reply_markup= buttons_admin)
                
                
            else:
                await message.answer("Yo'nalish nomini noto'g'ri tanlandi", reply_markup=del_cate_btn)
    
    if message.text == "🔙 Orqaga":
        if message.from_user.username == "Feruzbek_Sapayev":
            if metka == 1:
                await message.answer("Siz asosiy menyudasiz.\nMarhamat quyidagilardan birini tanlang.", reply_markup=buttons_admin)
            elif metka == 2:
                metka -=1
                await message.answer("Marhamat quyidagilardan birini tanlang.", reply_markup=type_btn_admin)
            elif metka == 3:
                metka -= 1
                await message.answer("Marhamat quyidagilardan birini tanlang.", reply_markup=autor_btn_admin)
        else:
            if metka == 1:
                await message.answer("Siz asosiy menyudasiz.\nMarhamat yo'nalishlardan birini tanlang.", reply_markup=buttons)
            elif metka == 2:
                metka -= 1
                await message.answer("Marhamat quyidagilardan birini tanlang.", reply_markup=type_btn)
            elif metka == 3:
                metka -= 1
                await message.answer("Marhamat quyidagilardan birini tanlang.", reply_markup=autor_btn)

    elif message.text == "🔝 Asosiy Menyu":
        if message.from_user.username == "Feruzbek_Sapayev":
            await message.answer("Siz asosiy menyudasiz.\nMarhamat quyidagilardan birini tanlang.", reply_markup=buttons_admin)
        else:
            await message.answer("Siz asosiy menyudasiz.\nMarhamat quyidagilardan birini tanlang.", reply_markup=buttons)
    
    elif message.text == "📊 Statistika":
        add_user()
        await message.answer(f"👤 <b>Obunachilar soni - {len(users)} ta.\n\n👨🏻‍💻 Dasturchi - @Feruzbek_Sapayev\n\n📊 @ITDarslarPro1Bot statistikasi</b>", parse_mode='html')

    elif message.text in categories:
        metka = 1
        categor_name = message.text
        btn_type(message.text)
        if message.from_user.username == 'Feruzbek_Sapayev':
            await message.answer(message.text, reply_markup=type_btn_admin)
        else:
            await message.answer(message.text, reply_markup=type_btn)

    

# -------------------- Categoriya -----------------------------------------------


# -------------------- Type -----------------------------------------------
    
    elif message.text == "Tur qo'shish" and message.from_user.username == "Feruzbek_Sapayev":
        add_type =True
        await message.answer("Tur nomini kiriting.", reply_markup=cancel)

    elif add_type and message.text!="Tur qo'shish" and not(message.text in ttypes) and message.from_user.username == 'Feruzbek_Sapayev':
        if message.text == "Bekor qilish":
            add_type = False
            await message.answer("Bekor qilindi.", reply_markup=type_btn_admin)
        else:
            data = {'name':message.text, 'categor': categor_name}
            ttype.insert_one(data)
            btn_type(categor_name)
            await message.answer("Tur muvaffaqiyatli qo'shildi.", reply_markup= type_btn_admin)
            add_type = False

    elif message.text == "Turni o'chirish" and message.from_user.username == 'Feruzbek_Sapayev':
        del_type = True
        await message.answer("Tur nomini tanlang.", reply_markup=del_type_btn)

    elif del_type:
        if message.text == "Bekor qilish":
            del_type = False
            await message.answer("Bekor qilindi.", reply_markup=type_btn_admin)
        else:
            if message.text in ttypes:
                name = {'name':message.text}
                tip = {'type': message.text}
                ttype.delete_one(name)
                autor.delete_many(tip)
                src.delete_many(tip)
                btn_type(categor_name)
                del_type = False
                await message.answer("Tur muvaffaqiyatli o'chirildi.", reply_markup=type_btn_admin)
                
                
            else:
                await message.answer("Tur nomini noto'g'ri tanlandi", reply_markup=del_type_btn)

    elif message.text in ttypes:
        metka  = 2
        type_name = message.text
        btn_autor(message.text)
        if message.from_user.username == "Feruzbek_Sapayev":
            await message.answer(message.text, reply_markup=autor_btn_admin)
        else:
            await message.answer(message.text, reply_markup=autor_btn)

    

# ####################### Type ############################################




# -------------------- Autor -----------------------------------------------
    elif message.text == "Muallif qo'shish" and message.from_user.username == 'Feruzbek_Sapayev':
        add_autor =True
        await message.answer("Muallif nomini kiriting.", reply_markup=cancel)

    elif add_autor and message.text!="Muallif qo'shish" and not(message.text in autors):
        if message.text == "Bekor qilish":
            add_autor = False
            await message.answer("Bekor qilindi.", reply_markup=autor_btn_admin)
        else:
            data = {'name':message.text, 'type': type_name}
            autor.insert_one(data)
            btn_autor(type_name)
            await message.answer("Muallif muvaffaqiyatli qo'shildi.", reply_markup= autor_btn_admin)
            add_autor = False
    

    elif message.text == "Muallifni o'chirish" and message.from_user.username == 'Feruzbek_Sapayev':
        del_autor = True
        await message.answer("Muallif nomini tanlang.", reply_markup=del_autor_btn)

    elif del_autor:
        if message.text == "Bekor qilish":
            del_autor = False
            await message.answer("Bekor qilindi.", reply_markup=autor_btn_admin)
        else:
            if message.text in autors:
                name = {'name':message.text}
                vd = {'autor': message.text}
                autor.delete_one(name)
                src.delete_many(vd)
                btn_autor(type_name)
                del_autor = False
                await message.answer("Muallif muvaffaqiyatli o'chirildi.", reply_markup=autor_btn_admin)
                
                
            else:
                await message.answer("Muallif nomini noto'g'ri tanlandi", reply_markup=del_autor_btn)
    elif message.text in autors:
        metka = 3
        autor_name = message.text
        btn_video(message.text)
        if message.from_user.username == 'Feruzbek_Sapayev':
            await message.answer(message.text, reply_markup=video_btn_admin)
        else:
            await message.answer(message.text, reply_markup=video_btn)



###################### Autor #################################################

# ============================= Videos =======================================

    elif message.text == "Video qo'shish" and message.from_user.username == 'Feruzbek_Sapayev':
        add_video =True
        await message.answer("Video nomini va linklarini kiriting.", reply_markup=cancel)

    elif add_video and message.text!="Video qo'shish" and not(message.text in videos) and message.from_user.username == 'Feruzbek_Sapayev':
        if message.text == "Bekor qilish":
            add_video = False
            await message.answer("Bekor qilindi.", reply_markup=video_btn_admin)
        else:
            massiv = list(map(str, message.text.split('|')))
            if len(massiv) == 5:
                data = {'name':massiv[0], 'autor': autor_name, 'link1': massiv[1], 'link2': massiv[2], 'caption1':massiv[3], 'caption2': massiv[4] }
            else:
                data = {'name':massiv[0], 'autor': autor_name, 'link1': massiv[1], 'link2': '', 'caption1':massiv[3], 'caption2': '' }
            src.insert_one(data)
            btn_video(autor_name)
            await message.answer("Video muvaffaqiyatli qo'shildi.", reply_markup= video_btn_admin)
            add_video = False
    elif message.text == "Orqaga":
        await message.answer("Mualliflar", reply_markup=video_btn_admin)

    elif message.text == "Videoni o'chirish":
        del_video = True
        await message.answer("Video nomini tanlang.", reply_markup=del_video_btn)

    elif del_video:
        if message.text == "Bekor qilish":
            del_video = False
            await message.answer("Bekor qilindi.", reply_markup=video_btn_admin)
        else:
            if message.text in videos and message.from_user.username == 'Feruzbek_Sapayev':
                name = {'name':message.text}
                src.delete_one(name)
                btn_video(autor_name)
                del_video = False
                await message.answer("Video muvaffaqiyatli o'chirildi.", reply_markup=video_btn_admin)
                
                
            else:
                await message.answer("Video nomini noto'g'ri tanlandi", reply_markup=del_video_btn)

    elif message.text in videos:
        link1 = link2 =''
        x = src.find()
        for i in x:
            if i['name'] == message.text:
                link1 = i['link1']
                link2 = i['link2']
                caption1 = i['caption1'] + "\n\n@ITDarslarPro1Bot — IT darslar platformasi!"
                caption2 = i['caption2'] + "\n\n@ITDarslarPro1Bot — IT darslar platformasi!"
        if link1!='':
            await bot.send_video(chat_id=message.chat.id, video=link1, caption=caption1)
        if link2!='':
            await bot.send_video(chat_id=message.chat.id, video=link2, caption=caption2)

# ######################## Videos ###########################################


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)



