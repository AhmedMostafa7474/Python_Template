from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.title
    
class Survey(models.Model):
    username = models.CharField(max_length=300,null=True,blank=True)
    email = models.CharField(max_length=300,null=True,blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    question1 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم جودة المحتوى التعليمي المتاح على الموقع؟ (1-5)"
    )
    question2 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم تنظيم وهيكلة دورات البث المباشر؟ (1-5)"
    )
    question3 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل تشعر أن المحتوى مقسم بشكل جيد وسهل الفهم؟ (1-5)"
    )
    question4 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل تجد أن التمارين والاختبارات مفيدة في تعزيز فهمك للمحتوى؟ (1-5)"
    )
    question5 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل تمكنت من تطبيق ما تعلمته من الدورات في مشاريعك أو عملك؟ (1-5)"
    )
    question6 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل تشعر أن المحتوى محدث ويتماشى مع التطورات الحديثة؟ (1-5)"
    )
    question7 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم سرعة تحميل الصفحات والفيديوهات على الموقع؟ (1-5)"
    )
    question8 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل تشعر أن النظام التعليمي على الموقع تفاعلي وجذاب؟ (1-5)"
    )
    question9 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="هل توفر المنصة أدوات كافية للتفاعل مع المعلمين والزملاء؟ (1-5)"
    )
    question10 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم جودة الدعم الفني المقدم من المنصة؟ (1-5)"
    )
    question11 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم تجربة مشاهدة الفيديوهات التعليمية من حيث الجودة والأداء؟ (1-5)"
    )
    question12 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="كيف تقيم توافق المنصة مع الأجهزة المختلفة (مثل الهواتف الذكية والأجهزة اللوحية)؟ (1-5)"
    )
    comments = models.TextField(null=True,blank=True ,verbose_name="ملاحظات واقتراحات")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.username + " Survey"
