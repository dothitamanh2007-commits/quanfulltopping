import streamlit as st

import pandas as pd

from datetime import datetime

st.image("TRASUA.jpg")

# ---------------------------------------------------------

# CẤU HÌNH TRANG & CƠ SỞ DỮ LIỆU SẢN PHẨM

# ---------------------------------------------------------

st.set_page_config(

page_title="Hệ Thống Tính Tiền Trà Sữa",

page_icon="🧋",

layout="wide"

)


# Danh sách menu & giá (VND)

MENU_TEA = {

"Trà Sữa Truyền Thống": 30000,

"Trà Sữa Trân Châu Đường Đen": 35000,
