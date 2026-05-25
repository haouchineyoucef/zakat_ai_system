# 🕌 Intelligent Zakat Decision Support System (Zakat-AI)
### منظومة دعم القرار الذكية لتحديد جدارة استحقاق الزكاة باستخدام تعلم الآلة

---

## 📌 نبذة عن المشروع (About the Project)
هذا المشروع يمثل نظاماً خبيراً متكاملاً (Expert Decision Support System) مصمماً لحوكمة وتأصيل عمليات توزيع أموال الزكاة وضمان توجيهها لمستحقيها الفعليين بأعلى درجات النزاهة والعدالة التوزيعية. تعتمد المنظومة على دمج فقه الكفاية المقاصدي مع خوارزميات التعلم الآلي المتقدمة لتقييم الحالات الإنسانية المتقدمة بناءً على توازنات معقدة بين الأبعاد المالية، الديموغرافية، والصحية.

This repository features an AI-driven, expert decision-support web application tailored for determining Zakat eligibility. By integrating the jurisprudential framework of Islamic economics with state-of-the-art Machine Learning, the system assesses multi-dimensional socioeconomic, demographic, and health attributes to compute reliable financial vulnerability and priority indices.

---

## 🔬 المعمارية والنمذجة الإحصائية (Model Architecture)
تم تطوير واختبار المنظومة المقترحة عبر مقارنة أدائية صارمة بين ثلاثة من نماذج التعلم الإحصائي والعميق:
1. **الانحدار اللوجستي (Logistic Regression)**
2. **الغابات العشوائية (Random Forest)** - *النموذج المعتمد تشغيلياً لكفاءته الفائقة وثباته.*
3. **الشبكات العصبية الاصطناعية (Artificial Neural Networks - ANN)**

### 📊 الميزات التفسيرية والضبط (XAI & Robustness)
- **منهجية SHAP (SHapley Additive exPlanations):** تم دمج تقنيات الذكاء الاصطناعي القابل للتفسير (XAI) لتفكيك آليات اتخاذ القرار داخل النموذج (Black-Box Transformation)، حيث أظهرت النتائج أن متغير **الدخل الشهري (Income)** يمثل الوزن النسبي الأكبر تأثيرًا على مخرجات النموذج، تليه مؤشرات عبء الدين والنفقات المعيشية المعيارية.
- **منحنيات المعايرة (Calibration Curves):** أظهر نموذج الغابات العشوائية أفضل مؤشر اتساق احتمالي بمعدل خطأ ضئيل جداً (Brier Score = 0.0073).

---

## 🖥️ واجهة النظام التشغيلية (System Dashboard)
تم بناء واجهة مستخدم ديناميكية تفاعلية باستخدام إطار العمل **Streamlit** لتسهيل عمل اللجان المؤسسية ومحاكاة الحالات المرجعية (Benchmark Scenarios) بدقة وفورية.

---

## 🛠️ متطلبات التشغيل المحلي (Local Installation & Setup)

إذا كنت ترغب في تشغيل المنظومة محلياً على جهازك، يرجى تتبع الخطوات التالية:

### 1. استنساخ المستودع (Clone the Repository)
```bash
git clone [https://github.com/haouchineyoucef/zakat_ai_system.git](https://github.com/haouchineyoucef/zakat_ai_system.git)
cd zakat_ai_system
