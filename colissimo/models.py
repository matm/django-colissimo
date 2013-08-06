# -*- coding: utf-8 -*-

from django.db import models
import types

class Region(models.Model):
	name = models.CharField(max_length = 255)
	# France
	FMA = (u'France', u'Monaco', u'Andorra')
	# Outre-mer OM1
	OM1 = (u'Guadeloupe', u'Martinique', u'French Guiana', u'Réunion', u'Mayotte',
		   u'Saint Pierre and Miquelon', u'Saint Martin', u'Saint Barthélémy')
	# Outre-mer OM2
	OM2 = (u'New Caledonia', u'French Polynesia', u'Wallis and Futuna Islands',
		   u'French Southern Territories')
	# International Zone A
	IZA = (u'Switzerland', u'Norway', u'Austria', u'Belgium', u'Bulgaria', u'Cyprus',
		   u'Czech Republic', u'Denmark', u'Estonia', u'Finland', u'Germany',
		   u'Greece', u'Hungary', u'Italy', u'Latvia', u'Lithuania', u'Luxembourg',
		   u'Malta', u'Netherlands', u'Poland', u'Portugal', u'Ireland', u'Romania',
		   u'Slovakia', u'Slovenia', u'Spain', u'Sweden',
		   u'United Kingdom of Great Britain and Northern Ireland', u'Gibraltar',
		   u'Guernsey', u'Jersey', u'Liechtenstein', u'Norway', u'San Marino')
	# International Zone B
	IZB = (u'Morocco', u'Algeria', u'Tunisia', u'Libyan Arab Jamahiriya',
		   u'Mauritania', u'Western Sahara', u'Albania', u'Armenia', u'Azerbaijan',
		   u'Ukraine', u'Belarus', u'Bosnia and Herzegovina', u'Croatia', u'Georgia',
		   u'Iceland', u'The former Yugoslav Republic of Macedonia',
		   u'Republic of Moldova', u'Russian Federation', u'Serbia', u'Turkey')
	# International Zone C
	IZC = (u'Afghanistan', u'Angola', u'Argentina', u'Zimbabwe', u'Zambia', u'Yemen',
		   u'Uganda', u'Bahrain', u'Chad', u'Benin', u'Botswana', u'Burkina Faso',
		   u'Burundi', u'Cameroon', u'Canada', u'Cape Verde',
		   u'Central African Republic', u'Comoros', u'Congo',
		   u'Democratic Republic of the Congo', u'Djibouti', u'Egypt',
		   u'Equatorial Guinea', u'Ethiopia', u'Gabon', u'Gambia', u'Ghana',
		   u'Guinea', u'Iran, Islamic Republic of', u'Iraq', u'Israel', u'Jordan',
		   u'Kenya', u'Kuwait', u'Lebanon', u'Lesotho', u'Liberia', u"Côte d'Ivoire",
		   u'Madagascar', u'Mali', u'Marshall Islands', u'Mozambique', u'Namibia',
		   u'Niger', u'Nigeria', u'Oman', u'Pakistan', u'Qatar', u'Rwanda',
		   u'Saudi Arabia', u'Senegal', u'South Africa', u'Sudan', u'Swaziland',
		   u'Syrian Arab Republic', u'United Republic of Tanzani', u'Timor-Leste',
		   u'Togo', u'United Arab Emirates', u'United States of America')
	# International Zone D
	IZD = (u'American Samoa', u'Anguilla', u'Antarctica', u'Antigua and Barbuda',
		   u'Aruba', u'Australia', u'Bahamas', u'United States Virgin Islands',
		   u'British Virgin Islands', u'Viet Nam',
		   u'Venezuela (Bolivarian Republic of)', u'Vanuatu', u'Uzbekistan',
		   u'Uruguay', u'Tuvalu', u'Bangladesh', u'Barbados', u'China', u'Chile',
		   u'Belize', u'Bermuda', u'Bhutan', u'Bolivia', u'Bouvet Island', u'Brazil',
		   u'British Indian Ocean Territory', u'Brunei Darussalam', u'Cambodia',
		   u'Cayman Islands', u'Christmas Island', u'Cocos (Keeling) Islands',
		   u'Colombia', u'Cook Islands', u'Costa Rica', u'Cuba', u'Dominica',
		   u'Dominican Republic', u'Ecuador', u'El Salvador', u'Eritrea',
		   u'Falkland Islands (Malvinas)', u'Faeroe Islands', u'Fiji', u'Guyana',
		   u'Greenland', u'Grenada', u'Guam', u'Guatemala', u'Guinea-Bissau',
		   u'Haiti', u'Heard Island and Mcdonald Islands', u'Holy See', u'Honduras',
		   u'Hong Kong Special Administrative Region of China', u'India',
		   u'Indonesia', u'Isle of Man', u'Jamaica', u'Japan', u'Kazakhstan',
		   u'Kiribati', u'French Southern Territories', u'Republic of Korea',
		   u'Kyrgyzstan', u"Democratic People's Republic of Korea",
		   u"Lao People's Democratic Republic",
		   u'Macao Special Administrative Region of China', u'Malawi', u'Malaysia',
		   u'Maldives', u'Mauritius', u'Mexico', u'Micronesia, Federated States of',
		   u'Mongolia', u'Montenegro', u'Montserrat', u'Myanmar', u'Nauru', u'Nepal',
		   u'Netherlands Antilles', u'New Zealand', u'Nicaragua', u'Niue',
		   u'Norfolk Island', u'Northern Mariana Islands', u'Palau',
		   u'Occupied Palestinian Territory', u'Panama', u'Papua New Guinea',
		   u'Paraguay', u'Peru', u'Philippines', u'Pitcairn', u'Puerto Rico',
		   u'Saint Helena', u'Saint Kitts and Nevis', u'Saint Lucia',
		   u'Saint Vincent and the Grenadines', u'Samoa', u'Sao Tome and Principe',
		   u'Seychelles', u'Sierra Leone', u'Singapore', u'Solomon Islands',
		   u'Somalia', u'South Georgia and the South Sandwich Islands',
		   u'Sri Lanka', u'Suriname', u'Svalbard and Jan Mayen Islands',
		   u'Taiwan, Province of China', u'Tajikistan', u'Thailand', u'Tokelau',
		   u'Tonga', u'Trinidad and Tobago', u'Turkmenistan',
		   u'Turks and Caicos Islands', u'United States Minor Outlying Islands',
		   u'Åland Islands')

	_lookup = (u'France', u'OM1', u'OM2', u'Zone A', u'Zone B', u'Zone C', u'Zone D')

	@staticmethod
	def get_region_from_country(country):
		if type(country) != types.StringType and type(country) != types.UnicodeType:
			raise TypeError, u"Country must be a string, not %s" % type(country)
		cty = country.strip().lower()
		# France
		zones = (Region.FMA, Region.OM1, Region.OM2, Region.IZA, Region.IZB, Region.IZC, Region.IZD)
		for k in range(len(zones)):
			for z in zones[k]:
				if cty == z.strip().lower():
					return Region.objects.get(name__contains=Region._lookup[k])
		return None

	def __repr__(self):
		return u"<Region: %s>" % self.name

class Recommanded(models.Model):
	"""
	Recommanded
	"""
	level = models.CharField(max_length = 3, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.level

class Rate(models.Model):
	# Up to this weight (in kg)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	# Signature on delivery?
	signature = models.BooleanField(default=False)
	# Deposit proof?
	deposit = models.BooleanField(default=False)
	# Tracking number?
	tracking = models.BooleanField(default=False)
	# Rate in Euro
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# FKs
	region = models.ForeignKey(Region)
	recommanded = models.ForeignKey(Recommanded)

	@staticmethod
	def get_rates(country, weight):
		"""
		Example: lowest rate for a 4.2 kg box to France:
		         Rate.get_rates(u'France', 4.2).get(recommanded__level='R0')
		"""
		if type(country) != types.StringType and type(country) != types.UnicodeType:
			raise TypeError, u"Country must be a string, not %s" % type(country)
		if type(weight) != types.FloatType and type(weight) != types.IntType:
			raise TypeError, u"Weight must be a float"
		if weight < 0 or weight > 30:
			raise ValueError, u"Colissimo only supports 0<weight<=30 kg"
		from decimal import Decimal
		r = Region.get_region_from_country(country)
		if r is None:
			raise ValueError, u"Bad country value '%s': could not determine region" % country
		w = Rate.objects.filter(weight__gte=Decimal(str(weight)), region=r)[0].weight
		rs = Rate.objects.filter(weight=w, region=r).order_by(u'price')
		return rs

	def __repr__(self):
		return u"<Rate: max %.2fkg@%s, %.2f EUR>" % (self.weight, self.recommanded, self.price)

	class Meta:
		unique_together = ((u'weight', 'region', 'recommanded'))

