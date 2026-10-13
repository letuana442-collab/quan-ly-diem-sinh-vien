import streamlit as st
import pandas as pd

st.title("QUAN LY DIEM SINH VIEN")

data = {
    "Ho_ten": [
        "Nguyen An", "Tran Binh", "Le Cuong",
        "Pham Dung", "Hoang Giang", "Vu Hanh",
        "Do Khoa", "Bui Lan", "Ngo Minh", "Dang Nam"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 7, 6, 4, 9],
    "Cuoi_ky": [9, 8, 7, 9, 5, 7, 8, 6, 4, 10]
}

df = pd.DataFrame(data)

df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

st.subheader("1. Bang diem sinh vien")
st.dataframe(df)

st.subheader("2. Thong ke")

st.write("Diem trung binh:", round(df["Tong_ket"].mean(), 2))

cao = df.loc[df["Tong_ket"].idxmax()]
thap = df.loc[df["Tong_ket"].idxmin()]

st.write("Diem cao nhat:", cao["Ho_ten"], cao["Tong_ket"])
st.write("Diem thap nhat:", thap["Ho_ten"], thap["Tong_ket"])

st.write("So sinh vien dat:", int((df["Tong_ket"] >= 5).sum()))

st.subheader("3. Chon sinh vien")

ten = st.selectbox("Chon ho ten:", df["Ho_ten"])

sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Chuyen can:", sv["Chuyen_can"])
st.write("Giua ky:", sv["Giua_ky"])
st.write("Cuoi ky:", sv["Cuoi_ky"])
st.write("Tong ket:", round(sv["Tong_ket"], 2))
st.write("Xep loai:", sv["Xep_loai"])

st.subheader("4. Bieu do diem tong ket")

st.bar_chart(df.set_index("Ho_ten")["Tong_ket"])

st.caption("Nguoi tao: [LÊ ANH TUẤN] - MSSV: [054208008451]")