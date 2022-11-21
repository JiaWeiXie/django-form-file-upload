from django.db import models


def cover_directory_path(instance, filename):
    return "covers/{0}_{1}".format(instance.id, filename)


class Book(models.Model):
    title = models.CharField("標題", max_length=128)
    description = models.TextField("描述", null=True, blank=True)
    cover_image = models.ImageField("封面", upload_to=cover_directory_path, null=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "書本"
        verbose_name_plural = verbose_name
