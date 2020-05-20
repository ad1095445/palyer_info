from django.db import models

class Rank(models.Model):
    class Meta:
        verbose_name = "排行榜"
        verbose_name_plural = "排行榜"

    client = models.CharField(verbose_name="客户端", max_length=50, null=False, blank=False)
    score = models.IntegerField(verbose_name="分数", null=False, blank=False)
    upload_time =  models.DateTimeField(auto_now_add=True,verbose_name="上传时间")

    def __str__(self):
        return self.client