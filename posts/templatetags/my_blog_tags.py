from django import template
from ..models import Article
from datetime import datetime

register = template.Library()

@register.simple_tag
def total_articles():
    return Article.publish.count()


@register.filter(name="isnew")
def time_calculate(value):    
    created_date = value.strftime("%d %m %Y")
    now_date = datetime.now().strftime("%d %m %Y")
    created_date_prime = datetime.strptime(created_date, "%d %m %Y")
    now_date_prime = datetime.strptime(now_date, "%d %m %Y")
    return (now_date_prime - created_date_prime).days < 7

# from datetime import datetime

# from datetime import datetime, timedelta

# @register.filter(name="isnew")
# def time_calculate(article_date):
#     try:
#         current_date = datetime.now()
#         difference = current_date - article_date
#         return difference.days < 7
#     except ValueError:
#         return False


# from datetime import datetime, timedelta

# @register.filter(name="isnew")
# def is_new(article):
#     try:
#         article_date = datetime.strptime(str(Article.created), "%d %m %Y")
#         current_date = datetime.now()
#         difference = current_date - article_date
#         return difference.days < 7
#     except ValueError:
#         return False
