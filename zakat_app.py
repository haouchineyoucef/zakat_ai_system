import streamlit as st
import numpy as np
import pandas as pd
import joblib
# streamlit run zakat_app.py


# 1. تحميل النموذج وقائمة الأعمدة الأصلية التي تدرب عليها
@st.cache_resource
def load_model_artifacts():
    model = joblib.load("rf_model.pkl")
    # تحميل قائمة الأعمدة التي حفظناها أثناء التدريب لضمان التطابق
    model_columns = joblib.load("model_columns.pkl")
    return model, model_columns
try:
    model, model_columns = load_model_artifacts()
except FileNotFoundError:
    st.error("لم يتم العثور على ملفات النموذج. يرجى تشغيل كود التدريب أولاً.")
    st.stop()
st.set_page_config(page_title="منصة التقديم على الزكاة الذكية", layout="wide")

#===================================================================
# تحسينات جمالية احترافية للواجهة
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
/* الخلفية العامة */
.stApp {
    background-color: #f5f7fa;
}
/*===================================================================
دعم اللغة العربية RTL
===================================================================*/
html, body, [class*="css"]  {
    direction: rtl;
    text-align: right;
    font-family: 'Cairo', 'Tahoma', sans-serif;
}
/* الحقول */
input, textarea {
    direction: rtl;
    text-align: right;
}
/* Selectbox */
div[data-baseweb="select"] > div {
    direction: rtl;
    text-align: right;
}
/* الأرقام تبقى يسارياً لسهولة القراءة */
input[type="number"] {
    direction: ltr;
    text-align: left;
}
/* العناوين */
h1, h2, h3, h4, h5, h6 {
    text-align: right;
}
/* الأزرار */
.stButton>button {
    width: 100%;
    background-color: #198754;
    color: white;
    border-radius: 10px;
    height: 3.5em;
    font-size: 22px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background-color: #157347;
    color: white;
}
/* الرسائل والتنبيهات */
.stAlert {
    direction: rtl;
    text-align: right;
}
/* Sidebar */
section[data-testid="stSidebar"] {
    direction: rtl;
    text-align: right;
}
/* العنوان الرئيسي */
.main-title {
    font-size: 48px;
    font-weight: bold;
    color: #0f5132;
    text-align: center;
    margin-bottom: 10px;
}
/* الوصف */
.subtitle {
    font-size: 22px;
    color: #555;
    text-align: center;
    margin-bottom: 30px;
}
/* البطاقات */
.custom-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
/* أزرار */
.stButton>button {
    width: 100%;
    background-color: #198754;
    color: white;
    border-radius: 10px;
    height: 3.5em;
    font-size: 22px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background-color: #157347;
    color: white;
}
/* الحقول */
.stNumberInput, .stTextInput, .stSelectbox {
    border-radius: 10px;
}
/* النتائج */
.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff;
    border-left: 6px solid #198754;
    margin-top: 20px;
}

/* ==========================================================
تكبير الخط العام في المنصة
========================================================== */
/* الخط الأساسي */
html, body, [class*="css"] {
    font-size: 18px !important;
}
/* النصوص العادية */
p, label, div, span {
    font-size: 18px !important;
}
/* حقول الإدخال */
input {
    font-size: 18px !important;
}
/* القوائم المنسدلة */
div[data-baseweb="select"] * {
    font-size: 18px !important;
}
/* Number Input */
.stNumberInput input {
    font-size: 18px !important;
    font-weight: 600;
}
/* Text Input */
.stTextInput input {
    font-size: 18px !important;
}
/* File Uploader */
[data-testid="stFileUploader"] {
    font-size: 18px !important;
}
/* الرسائل */
.stAlert {
    font-size: 18px !important;
}
/* النصوص التوضيحية */
[data-testid="stCaptionContainer"] {
    font-size: 16px !important;
}
/* عناصر Metric */
[data-testid="stMetricLabel"] {
    font-size: 22px !important;
    font-weight: bold;
}
[data-testid="stMetricValue"] {
    font-size: 38px !important;
    font-weight: bold;
}
/* عناوين الأقسام */
h1 {
    font-size: 42px !important;
}
h2 {
    font-size: 34px !important;
}
h3 {
    font-size: 28px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🕌 منظومة الزكاة الرقمية الذكية</div>',
    unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'منصة ذكية لدعم قرارات استحقاق الزكاة باستخدام تقنيات تعلم الآلة والحوكمة الرقمية'
    '</div>',
    unsafe_allow_html=True)
# إضافة عبارة إخلاء المسؤولية والطور التجريبي
st.info("""
**⚠️ نسخة تجريبية أولية (Beta Version) - لأغراض البحث العلمي والتدقيق الإستراتيجي.**
هذه المنصة تمثل نموذجاً محاكياً مدعوماً بالذكاء الاصطناعي لفحص كفاءة كفاية الاستحقاق، 
ولا تعتبر محركاً نهائياً لإصدار فتاوى الصرف أو التوزيع المالي دون المراجعة البشرية المعتمدة.
""")
#===================================================================
# Sidebar
#===================================================================
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )
    st.markdown("## ℹ️ معلومات النظام")
    st.info(
        """
        تعتمد هذه المنصة على نموذج ذكاء اصطناعي
        مدرب لتقييم مؤشرات الاستحقاق الزكوي
        وفق معايير مالية واجتماعية وصحية.
        """
    )

    st.sidebar.markdown("### 🛠️ حالة النظام")
    st.sidebar.caption("📌 **الإصدار:** 1.0.0 (نموذج أولي تجريبي)")
    st.sidebar.caption("🚨 خاضع للتدقيق والمحاكاة البحثية")
    st.sidebar.write("---")

    st.markdown("---")
    st.success("✔️ نظام ذكي")
    st.success("✔️ حوكمة رقمية")
    st.success("✔️ تفسير قابل للمراجعة")
    st.markdown("---")
    st.caption("الإصدار التجريبي 1.0")
    # الخط الفاصل ومعلومات الباحث في أسفل السايدبار بتنسيق محاذ لليد اليمنى
    st.sidebar.markdown("<br><hr>", unsafe_allow_html=True)
    st.sidebar.markdown(
        """
        <div style='text-align: right; direction: rtl; color: #555555; font-size: 14px; padding-right: 10px;'>
            <b style='color: #000000;'>إعداد وتطوير الباحث:</b><br>
            أ. د. حوشين يوسف<br>
            <span style='font-size: 12px; color: #777777;'>جامعة البليدة 2 - الجزائر</span>
        </div>
        """,
        unsafe_allow_html=True)

st.markdown('<div class="custom-card">', unsafe_allow_html=True)

# 📝 إدخال البيانات من المستخدم
الاسم = st.text_input("📝 الاسم الكامل")
الدخل = st.number_input("💰 الدخل الشهري (بالدينار)", min_value=0, value=0)
عدد_المعالين = st.number_input("👨‍👩‍👧‍👦 عدد المعالين", min_value=1, value=1)

# ===================================================================
# حساب نفقات المعيشة معيارياً (منعاً للتحايل وضماناً للحوكمة)
# ===================================================================
# احتساب النفقات مباشرة بالمعادلة الأساسية المستنبطة من بيئة المحاكاة
نفقات_المعيشة_الأساسية = 20000 + عدد_المعالين * 5000
# الحدود الأمنية لضمان التوافق الإحصائي مع نموذج التدريب
min_expenses = 15000 + عدد_المعالين * 3000
max_expenses = 60000 + عدد_المعالين * 10000
# تطبيق معادلة القص الذاتية للتأكد المطلق من عدم خروج القيمة عن النطاق
نفقات_المعيشة = int(max(min_expenses, min(نفقات_المعيشة_الأساسية, max_expenses)))
# عرض القيمة للمتقدم كمعلومة "للقراءة فقط" لحفظ الشفافية
st.info(
    f"🏠 **نفقات المعيشة المعيارية المحتسبة:** {نفقات_المعيشة:,} دينار جزائري.")
st.caption(
    "💡 يحدد النظام نفقات المعيشة تلقائياً بناءً على معايير الكفاية الفقهية وحجم الأسرة (عدد المعالين) لضمان العدالة ومنع التلاعب.")

# إدخال بيانات المديونية
مدين = st.selectbox("📄 هل لديك ديون؟", ["لا", "نعم"])
st.caption("يتم احتساب القسط الشهري تلقائيًا بناءً على إجمالي الدين ومدة السداد")
if مدين == "نعم":
    إجمالي_الدين = st.number_input(
        "💳 إجمالي الدين",
        min_value=1,
        value=50000)
    مدة_السداد = st.number_input(
        "⏳ عدد الأشهر المتبقية للسداد",
        min_value=1,
        value=12)
    # حساب القسط الشهري بشكل مباشر وآمن
    قيمة_القسط = إجمالي_الدين / مدة_السداد
else:
    إجمالي_الدين = 0
    مدة_السداد = 1
    قيمة_القسط = 0.0
نوع_العمل = st.selectbox("⚒️ نوع العمل", ["لا يعمل", "عمل يومي", "عمل دائم"])
الحالة_الصحية = st.selectbox("🏥 الحالة الصحية", ["سليم", "مرض مزمن", "معاق"])

# تحميل الوثائق لدعم الحوكمة والشفافية
st.markdown("---")
st.write("📎 تحميل الوثائق المطلوبة للتحقق")
بطاقة_تعريف = st.file_uploader("🔐 بطاقة الهوية الوطنية", type=["pdf", "jpg", "png"])
وثيقة_دين = None
if مدين == "نعم":
    وثيقة_دين = st.file_uploader("📄 شهادة تثبت المديونية وصحة الغرم", type=["pdf", "jpg", "png"])

st.markdown('</div>', unsafe_allow_html=True)
# 🔍 عند الضغط على الزر لطلب تحليل القرار
st.markdown("### 📌 اكتمال البيانات")
progress_value = 0
if الاسم:
    progress_value += 20
if الدخل > 0:
    progress_value += 20
if عدد_المعالين >= 1:
    progress_value += 20
if بطاقة_تعريف:
    progress_value += 20
if مدين == "لا" or وثيقة_دين:
    progress_value += 20
st.progress(progress_value)

if st.button("تحقق من الاستحقاق"):
    if not الاسم or not بطاقة_تعريف:
        st.warning("🚫 الرجاء إدخال الاسم وتحميل بطاقة الهوية.")
    elif مدين == "نعم" and not وثيقة_دين:
        st.warning("🚫 الرجاء تحميل شهادة المديونية.")
    else:
        # 🔄 خطوة المعالجة الذكية والمطابقة الحرفية (Alignment):
        # ===================================================================
        # تحويل القيم العربية إلى نفس القيم المستخدمة أثناء التدريب
        # ===================================================================
        work_map = {
            "لا يعمل": "unemployed",
            "عمل يومي": "daily_wage",
            "عمل دائم": "permanent"
        }
        health_map = {
            "سليم": "healthy",
            "مرض مزمن": "chronic_disease",
            "معاق": "disabled"
        }
        # تحويل الاختيارات العربية إلى الإنجليزية
        نوع_العمل_انجليزي = work_map[نوع_العمل]
        الحالة_الصحية_انجليزية = health_map[الحالة_الصحية]
        # ===================================================================
        # إنشاء DataFrame مطابق تمامًا لبيانات التدريب
        # ===================================================================
        single_request = pd.DataFrame({
            "income": [الدخل],
            "dependents": [عدد_المعالين],
            "living_expenses": [نفقات_المعيشة],
            "debt": [1 if مدين == "نعم" else 0],
            "total_debt": [إجمالي_الدين],
            "repayment_months": [مدة_السداد],
            "monthly_debt_payment": [قيمة_القسط],
            # استخدام القيم الإنجليزية المطابقة للتدريب
            "work_type": [نوع_العمل_انجليزي],
            "health": [الحالة_الصحية_انجليزية]
        })
        # ===================================================================
        # تطبيق One-Hot Encoding
        # ===================================================================
        single_encoded = pd.get_dummies(single_request,columns=["work_type", "health"])
        single_encoded = single_encoded.reindex(columns=model_columns, fill_value=0).astype(float)
        # ===================================================================
        # مواءمة الأعمدة مع بيانات التدريب الأصلية
        # ===================================================================
        for col in model_columns:
            if col not in single_encoded.columns:
                single_encoded[col] = 0
        # حذف أي أعمدة إضافية غير موجودة أثناء التدريب
        single_encoded = single_encoded[model_columns]
        # تحويل جميع القيم إلى float
        input_data = single_encoded.astype(float)
        # 🔍 التنبؤ الآمن باستخدام النموذج المدرب
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        # 📊 عرض النتائج التفصيلية ومؤشرات الأولوية
        st.markdown("### 📊 تقرير فحص أهلية الاستحقاق")
        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True)
        if prediction == 1:
            if probability >= 0.90:
                priority_level = "مستحق واضح – احتمال مرتفع للاستحقاق"
                color = "green"
            elif probability >= 0.70:
                priority_level = "مستحق مرجّح – احتمال متوسط للاستحقاق"
                color = "orange"
            else:
                priority_level = "مستحق محتمل – احتمال ضعيف للاستحقاق"
                color = "gray"
            st.success(f"✅ النتيجة الأولية: {الاسم} ضمن الفئات المرشحة للاستحقاق.")
            st.metric(label="مؤشر أولوية الاستحقاق",value=f"{probability * 100:.1f}%")
            st.subheader(f"درجة الحالة: :{color}[{priority_level}]")
            st.info("⚖️ القرار النهائي يُعتمد بعد المراجعة الشرعية والإدارية للوثائق.")
        else:
            st.error(f"❌ النتيجة الأولية: {الاسم} غير مستحق حالياً.")
            st.metric(label="مؤشر أولوية الاستحقاق",value=f"{probability * 100:.1f}%")


        st.markdown('</div>',unsafe_allow_html=True)



# streamlit run zakat_app.py
