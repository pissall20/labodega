from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comments"]
        widgets = {"comments": Textarea(attrs={"cols": 40, "rows": 15})}
