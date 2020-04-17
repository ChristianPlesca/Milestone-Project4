from django.db import models
from products.models import Product

class Order(models.Model):
    COUNTRIES = (
        ('albania', 'Albania'),
        ('algeria', 'Algeria'),
        ('andorra', 'Andorra'),
        ('argentina', 'Argentina'),
        ('armenia', 'Armenia'),
        ('australia', 'Australia'),
        ('austria', 'Austria'),
        ('azerbaijan', 'Azerbaijan'),
        ('belarus', 'Belarus'),
        ('belgium', 'Belgium'),
        ('bermuda', 'Bermuda'),
        ('bosnia', 'Bosnia'),
        ('brazil', 'Brazil'),
        ('bulgaria', 'Bulgaria'),
        ('canada', 'Canada'),
        ('chile', 'Chile'),
        ('china', 'China'),
        ('colombia', 'Colombia'),
        ('costa_rica', 'Costa Rica'),
        ('croatia', 'Croatia'),
        ('cyprus', 'Cyprus'),
        ('czech_republic', 'Czech Republic'),
        ('denmark', 'Denmark'),
        ('ecuador', 'Ecuador'),
        ('egypt', 'Egypt'),
        ('estonia', 'Estonia'),
        ('finland', 'Finland'),
        ('france', 'France'),
        ('georgia', 'Georgia'),
        ('germany', 'Germany'),
        ('greece', 'Greece'),
        ('guatemala', 'Guatemala'),
        ('honduras', 'Honduras'),
        ('hungary', 'Hungary'),
        ('iceland', 'Iceland'),
        ('india', 'India'),
        ('indonesia', 'Indonesia'),
        ('israel', 'Israel'),
        ('italy', 'Italy'),
        ('jamaica', 'Jamaica'),
        ('japan', 'Japan'),
        ('latvia', 'Latvia'),
        ('liechtenstein', 'Liechtenstein'),
        ('lithuania', 'Lithuania'),
        ('luxembourg', 'Luxembourg'),
        ('macedonia', 'Macedonia'),
        ('malaysia', 'Malaysia'),
        ('maldives', 'Maldives'),
        ('malta', 'Malta'),
        ('mexico', 'Mexico'),
        ('moldova', 'Moldova'),
        ('monaco', 'Monaco'),
        ('montenegro', 'Montenegro'),
        ('morocco', 'Morocco'),
        ('netherlands', 'Netherlands'),
        ('new_zealand', 'New Zealand'),
        ('norway', 'Norway'),
        ('peru', 'Peru'),
        ('philippines', 'Philippines'),
        ('poland', 'Poland'),
        ('portugal', 'Portugal'),
        ('south_korea', 'Republic of Korea'),
        ('romania', 'Romania'),
        ('russia', 'Russia'),
        ('serbia', 'Serbia'),
        ('singapore', 'Singapore'),
        ('slovakia', 'Slovakia'),
        ('slovenia', 'Slovenia'),
        ('south_africa', 'South Africa'),
        ('spain', 'Spain'),
        ('sweden', 'Sweden'),
        ('switzerland', 'Switzerland'),
        ('thailand', 'Thailand'),
        ('tunisia', 'Tunisia'),
        ('turkey', 'Turkey'),
        ('ukraine', 'Ukraine'),
        ('uae', 'United Arab Emirates'),
        ('uk', 'United Kingdom'),
        ('usa', 'United States'),
    )
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False,choices=COUNTRIES)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)

