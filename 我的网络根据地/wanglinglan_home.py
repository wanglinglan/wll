"'wanglinglan 的网站'"
import  streamlit as st
from PIL import Image
from PIL import Image,ImageOps,ImageFilter
import matplotlib as plt

page = st.sidebar.radio("我的首页",['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区',"解密区"])


if st.button('音乐'):
    audio_file = open('霞光.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
else:
    st.write("祝您阅读愉快！")
def page_1():
    "'我的兴趣推荐'"
    st.write(":blue[这是我的兴趣推荐]")
    st.write("以下分为三个板块")
    tab1,tab2,tab3,tab4 = st.tabs(["兴趣分享","课外奖状","本人作文","音乐视频"])
    with tab1:
        st.write("一、兴趣分享")
        st.image("鹦鹉.jpg")
        st.image("斑猫.jpg")
        st.image("非遗.jpg")

    with tab2:
        st.write("二、课外奖状")
        st.image("奖状.jpg")
        st.image("奖状2.jpg")

    with tab3:
        st.write("三、本人作文")
        st.image("作文1.jpg")
        st.image("作文2.jpg")
        st.image("作文3.jpg")
        st.image("作文4.jpg")
        st.image("作文5.jpg")
        st.image("作文6.jpg")
        st.image("作文7.jpg")
        st.image("作文8.jpg")
    with tab4:
        with open("解密.mp4","rb") as f:
            mymp4 = f.read()
        st.write("周深——解密")
        st.video(mymp4)
        with open("轻音乐.mp4","rb") as f:
            mymp4_2 = f.read()
        st.write("一首轻音乐送你，放松一下疲劳的双耳吧")
        st.video(mymp4_2)
        
    st.write(":red[未完待续！！！]")
    
def page_2():
    "'我的图片处理工具'"
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpg","jpeg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        
        tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(["原图","改图1","改图2","改图3","灰度图","反色","高斯模糊","颜色减淡"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            img_gray = img.convert('L')
            st.image(img_gray)
        with tab6:
            img_invert = ImageOps.invert(img_gray)
            st.image(img_invert)
        with tab7:
            img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
            st.image(img_gaussian)
        with tab8:
            width,height = img.size
            img_gray = img.convert('L')
            img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))
            for x in range(width):
                for y in range(height):
                    pos = (x,y)

                    A = img_gray.getpixel(pos)
                    B = img_gaussian.getpixel(pos)
                    img_gray.putpixel(pos,min(int(A+A*B/(255-B)),255))
            st.image(img_gray)
        
def page_3():
    "'我的智慧词典'"
    st.write("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(7988):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in  times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
            with open("check_out_times.txt","w",encoding="utf-8")as f:
                message = ""
                for k,v in times_dict.items():
                    message += str(k) + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)
        st.write("查询次数：",times_dict[n])
        if word == "wang":
            st.code('''
                    #恭喜你触发彩蛋，这是一行Python代码
                    print("祝你万事顺利，福寿永年")''')
            st.balloons()
        if word =="π":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="qing":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="tan":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="yin":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="ming":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="fangpi":
            st.write("恭喜你触发彩蛋!")
            st.snow()
        if word =="agirl":
            st.write("恭喜你触发彩蛋!")
            st.snow()
def page_4():
    "'我的留言区'"
    st.write('我的留言区')
    with open("leave_messages.txt","r",encoding="utf-8")as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🍭"):
                st.write(i[1]+i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🎇"):
                st.write(i[1]+i[2])
        elif i[1] == "学霸":
            with st.chat_message("🏆"):
                st.write(i[1]+i[2])
        elif i[1] == "神秘人":
            with st.chat_message("❔"):
                st.write(i[1]+i[2])
        elif i[1] == "富翁":
            with st.chat_message("💸"):
                st.write(i[1]+i[2])
        elif i[1] == "花季少女":
            with st.chat_message("💮"):
                st.write(i[1]+i[2])
        elif i[1] == "美女":
            with st.chat_message("😜"):
                st.write(i[1]+i[2])
        elif i[1] == "帅哥":
            with st.chat_message("😎"):
                st.write(i[1]+i[2])
        elif i[1] == "现代版福尔摩斯":
            with st.chat_message("🕵️‍♀️"):
                st.write(i[1]+i[2])
                
    name = st.selectbox("我是.......",["阿短","现代版福尔摩斯","编程猫","学霸","神秘人","美女","帅哥","富翁","花季少女"])
    new_message = st.text_input("想要说的话.....")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8")as f:
                message = ""
                for i in messages_list:
                    message += i[0] + "#" + i[1] + "#" + i[2] +"\n"
                message = message[:-1]
                f.write(message)

def page_5():
    '"解密区"'
    st.write("暂未开放")

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (b,g,r)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == "解密区":
    page_5()
