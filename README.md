تكوين الفيروس:

يتكون من كودين برمجيين :

كود السيرفر يتكون من fanction 2

الاولى (recvf) مسئولة عن فحص الاتصال بين المهاجم و الضحية

التانية (server) مسئولة عن انشاء اتصال بين المهاجم و الضحية و ارسال الاوامر الى جهاز الضحية للتشفير او فك التشفير

كود الفيروس (final/Ransomeware) يتكون من fanction 6

1- encryption تستقبل argumant 2 و مسؤولة عن تشفير الملفات

2-decryption تستقبل argumant 2 مسئولة عن فك تشفير الملفات

3- partition_windows تقوم يالعودة ب list تحتوي اسماء جميع اقراص التخزين عدا قرص "C" لانه يحتوي ملفات النظام و لايجب تشفيرها

4-dir_f_list_en يتم استدعاء encryption fanction و يتم البحث داخلهاعن جميع الملفات التي تنتهي بامتداد("doc" or "docx") و تقوم بتشفيرها و اضافة امتداد (".R") لها

5-dir_f_list_de يتم استدعاء decryptipn fanction ويتم البحث داخلهاعن جميع الملفات التي تنتهي بامتداد (".R") وتقوم بازالته و فك تشفير الملفات

6-client مسئولة عن انشاء اتصال بينها و بين السيرفر يتم استدعاء جميع fanctions داخلها و هي الوحيدة التي يتم استدعائها بشكل اساسي للتنفيذ الكود
*********************************
آليه العمل :

عندما يضغط الضحية على الصورة الملغمة يبدأ عمل الفيروس في خلفية جهازة ويتم انشاء اتصال بالسيرفر الخاص بالمهاجم حيث يتم الاتصال بينهم عن طريق عنوان ip عند نجاح عملية الاتصال يمكن للمهاجم تشفير ملفات الوورد الخاصة بالضحية كما يمكنه من فك تشفير هذه الملفات اذا تم الاتفاق بينهم على المبلغ المالي الذي سيرسل للمهاجم

**********************************
ملاحظات

تم بناء سيرفر وهمي لتنفيذ المشروع لأن استخدام سيرفر حقيقي يتطلب منا شراءه ورفعه على شبكة الانترنت
************************************
(server.exe)قمنا برفع السيرفر كملف تنفيذي حتى يتمكن أي شخص من تجريب المشروع ولكن يجب على من يريد تنزيل الملف   
       كملف مضغوط وذلك بالضغط على زر   (test1) أن يقوم بتحميل المشروع البرمجي
 
Clone or download

ثم خيار  Download ZIP 
***********************************
