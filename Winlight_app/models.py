from django.db import models

class RecentWork(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recent_work/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # ADDED: Boolean switch for layout routing
    is_featured = models.BooleanField(default=True, help_text="Check to display in the homepage carousel slider. Uncheck to move to the dedicated portfolio grid page.")

    class Meta:
        ordering = ['-uploaded_at']
        db_table = 'winlight_app_recentwork'  # Forces lowercase mapping to match SQLite table

    def __str__(self):
        return self.title


class UpcomingProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='upcoming_projects/')
    release_expected = models.CharField(max_length=100, blank=True)
    # Boolean filter to toggle main landing page spotlight
    is_featured = models.BooleanField(default=True, verbose_name="Feature on Homepage")

    class Meta:
        db_table = 'winlight_app_upcomingproject'  # Forces lowercase mapping

    def __str__(self):
        return self.title


class CrewMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='crew/')
    display_order = models.PositiveIntegerField(default=0)
    # ADDED: Layout switch flag
    is_featured = models.BooleanField(default=True, help_text="Check to feature inside the homepage loop slider. Uncheck to move to the standalone roster page.")

    class Meta:
        ordering = ['display_order', 'name']
        db_table = 'winlight_app_crewmember'  # Forces lowercase mapping

    def __str__(self):
        return f"{self.name} - {self.role}"


class Article(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/')
    published_date = models.DateTimeField(auto_now_add=True)
    # Boolean filter to toggle main landing page spotlight
    is_featured = models.BooleanField(default=True, verbose_name="Feature on Homepage")

    class Meta:
        ordering = ['-published_date']
        db_table = 'winlight_app_article'  # Forces lowercase mapping

    def __str__(self):
        return self.title