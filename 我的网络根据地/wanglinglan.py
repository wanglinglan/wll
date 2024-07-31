"'wanglinglan 的网站'"
import  streamlit as st
from PIL import Image
from PIL import Image,ImageOps,ImageFilter
import matplotlib as plt

col1 = st.columns(1)
with col1:
    if st.button('音乐'):
        audio_file = open('霞光.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
    else:
        st.write("祝您阅读愉快！")

col2,col3 = st.columns(4,7)
with col2:
    col4 = st.columns(2)
    with col4:
        st.write(":blue[网页介绍]")
        st.write("........")
    col5 = st.columns(2)
    with col5:
        st.write("本人介绍")
        st.write(".......")
with col3:
    col6 = st.columns(1)
    with col6:
        st.write("喜欢的网站")
        st.write("........")
    col7 = st.columns(1)
    with col7:
        st.write("喜欢的游戏")
        st.write(".......")
    col8 = st.columns(1)
    with col8:
        st.write("喜欢的电影")
        st.write(".......")
col9 = st.columns(5)
with col9:
    st.write("改图专区")
    st.write("......")
col10,col11 = st.columns(3,3)
with col10:
    st.write("我的小作文")
with col11:
    st.write("专业英语查词")
col12,col13 = st.columns(5,4)
with col12:
    st.write("我的旅游照片")
with col13:
    st.write("音乐视频")
col14,col15 = st.columns(6,5)
with col14:
    st.write ("你知道如何解摩斯电码吗？")
with col15:
    st.write("解秘方法")
col16 = st.columns(3)
with col16:
    st.write("评论区")

    