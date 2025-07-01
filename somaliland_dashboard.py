# --- 主頁腳本：somaliland_dashboard.py ---
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Somaliland Climate Homepage", page_icon="🌍", layout="wide")

st.sidebar.title("關於此專題")
st.sidebar.info(
    """
    本儀表板旨在提供索馬利蘭地區近期 (2015-2025) 氣候變遷的動態分析。
    
    **數據來源:**
    - **降水:** NASA GPM IMERG
    - **氣溫及其他:** ECMWF ERA5-Land
    
    *役男：林軒毅*
    """
)
st.sidebar.markdown("---")
st.sidebar.header("報告圖表列表")
st.sidebar.markdown("""
- **圖1:** 時間序列總覽圖
- **圖2:** SPI乾旱指數圖
- **圖3:** 區域氣候比較圖
- **圖4:** 年平均降水地圖
- **圖5:** 年平均氣溫地圖
- **圖6:** 乾旱/濕潤年距平圖
- **圖7:** 季節降水比較圖
- **圖8:** 區域SPI比較圖
- **圖10:** 月均溫箱型圖
- **圖11:** 溫雨關係散佈圖
- **圖12:** 主要農業區氣候圖
- **圖13:** 降雨變異性地圖
- **圖14:** 生長季長度比較圖
- **圖15:** 複合災害分析圖
- **圖16:** 區域降雨關聯圖
""")

st.title("🌍 索馬利蘭氣候分析儀表板總覽")
st.markdown("歡迎來到本專題的成果儀表板。此處提供最重要的摘要圖表。請使用左側導覽列切換至不同分析主題。")
st.markdown("---")

# 定義圖片路徑
figures_path = "figures"

st.header("核心發現摘要")
col1, col2 = st.columns(2)
with col1:
    st.subheader("乾旱事件監測 (SPI)")
    st.image(os.path.join(figures_path, "fig2_spi12_drought_analysis.png"), use_container_width=True)
with col2:
    st.subheader("農業潛力評估")
    st.image(os.path.join(figures_path, "fig14_growing_season_length.png"), use_container_width=True)

st.markdown("---")
st.header("氣候時間序列總覽")
st.image(os.path.join(figures_path, "fig1_timeseries_overview.jpg"), use_container_width=True)