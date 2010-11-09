# coding: iso-8859-1

from django.db import models
import types

class Region(models.Model):
	name = models.CharField(max_length = 255)
	# France
	FMA = ('France', 'Monaco', 'Andorra')
	# Outre-mer OM1
	OM1 = ('Guadeloupe', 'Martinique', 'French Guiana', 'Réunion', 'Mayotte', 'Saint Pierre and Miquelon', 'Saint Martin', 'Saint Barthélémy')
	# Outre-mer OM2
	OM2 = ('New Caledonia', 'French Polynesia', 'Wallis and Futuna Islands', 'French Southern Territories')
	# International Zone A
	IZA = ('Switzerland', 'Norway', 'Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'Germany', 
			'Greece', 'Hungary', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Ireland', 'Romania', 'Slovakia', 
			'Slovenia', 'Spain', 'Sweden', 'United Kingdom of Great Britain and Northern Ireland', 'Gibraltar', 'Guernsey', 'Jersey', 'Liechtenstein', 'Norway',
			'San Marino')
	# International Zone B
	IZB = ('Morocco', 'Algeria', 'Tunisia', 'Libyan Arab Jamahiriya', 'Mauritania', 'Western Sahara', 'Albania', 'Armenia',
			'Azerbaijan', 'Ukraine', 'Belarus', 'Bosnia and Herzegovina', 'Croatia', 'Georgia', 'Iceland', 'The former Yugoslav Republic of Macedonia',
			'Republic of Moldova', 'Russian Federation', 'Serbia', 'Turkey')
	# International Zone C
	IZC = ('Afghanistan', 'Angola', 'Argentina', 'Zimbabwe', 'Zambia', 'Yemen', 'Uganda', 'Bahrain', 'Chad', 'Benin', 'Botswana', 'Burkina Faso',
			'Burundi', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Comoros', 'Congo', 'Democratic Republic of the Congo', 'Djibouti',
			'Egypt', 'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Iran, Islamic Republic of', 'Iraq', 'Israel', 'Jordan', 'Kenya',
			'Kuwait', 'Lebanon', 'Lesotho', 'Liberia', "Côte d'Ivoire", 'Madagascar', 'Mali', 'Marshall Islands', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
			'Oman', 'Pakistan', 'Qatar', 'Rwanda', 'Saudi Arabia', 'Senegal', 'South Africa', 'Sudan', 'Swaziland', 'Syrian Arab Republic', 'United Republic of Tanzani',
			'Timor-Leste', 'Togo', 'United Arab Emirates', 'United States of America')
	# International Zone D
	IZD = ('American Samoa', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Aruba', 'Australia', 'Bahamas', 'United States Virgin Islands',
			'British Virgin Islands', 'Viet Nam', 'Venezuela (Bolivarian Republic of)', 'Vanuatu', 'Uzbekistan', 'Uruguay', 'Tuvalu', 'Bangladesh',
			'Barbados', 'China', 'Chile', 'Belize', 'Bermuda', 'Bhutan', 'Bolivia', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
			'Brunei Darussalam', 'Cambodia', 'Cayman Islands', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Cook Islands', 'Costa Rica',
			'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Eritrea', 'Falkland Islands (Malvinas)', 'Faeroe Islands', 'Fiji', 'Guyana',
			'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea-Bissau', 'Haiti', 'Heard Island and Mcdonald Islands', 'Holy See', 'Honduras', 
			'Hong Kong Special Administrative Region of China', 'India', 'Indonesia', 'Isle of Man', 'Jamaica', 'Japan', 'Kazakhstan', 'Kiribati',
			'French Southern Territories', 'Republic of Korea', 'Kyrgyzstan', "Democratic People's Republic of Korea", "Lao People's Democratic Republic",
			'Macao Special Administrative Region of China', 'Malawi', 'Malaysia', 'Maldives', 'Mauritius', 'Mexico', 'Micronesia, Federated States of',
			'Mongolia', 'Montenegro', 'Montserrat', 'Myanmar', 'Nauru', 'Nepal', 'Netherlands Antilles', 'New Zealand', 'Nicaragua', 'Niue', 'Norfolk Island',
			'Northern Mariana Islands', 'Palau', 'Occupied Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn',
			'Puerto Rico', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 
			'Seychelles', 'Sierra Leone', 'Singapore', 'Solomon Islands', 'Somalia', 'South Georgia and the South Sandwich Islands', 'Sri Lanka', 'Suriname',
			'Svalbard and Jan Mayen Islands', 'Taiwan, Province of China', 'Tajikistan', 'Thailand', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Turkmenistan',
			'Turks and Caicos Islands', 'United States Minor Outlying Islands', 'Åland Islands')

	_lookup = ('France', 'OM1', 'OM2', 'Zone A', 'Zone B', 'Zone C', 'Zone D')

	@staticmethod
	def get_region_from_country(country):
		if type(country) != types.StringType and type(country) != types.UnicodeType:
			raise TypeError, "Country must be a string, not %s" % type(country)
		cty = country.strip().lower()
		# France
		zones = (Region.FMA, Region.OM1, Region.OM2, Region.IZA, Region.IZB, Region.IZC, Region.IZD)
		for k in range(len(zones)):
			for z in zones[k]:
				if cty == z.strip().lower():
					return Region.objects.get(name__contains=Region._lookup[k])
		return None

	def __repr__(self):
		return "<Region: %s>" % self.name

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
		         Rate.get_rates('France', 4.2).get(recommanded__level='R0')
		"""
		if type(country) != types.StringType and type(country) != types.UnicodeType:
			raise TypeError, "Country must be a string, not %s" % type(country)
		if type(weight) != types.FloatType and type(weight) != types.IntType:
			raise TypeError, "Weight must be a float"
		if weight < 0 or weight > 30:
			raise ValueError, "Colissimo only supports 0<weight<=30 kg"
		from decimal import Decimal
		r = Region.get_region_from_country(country)
		if r is None:
			raise ValueError, "Bad country value '%s': could not determine region" % country
		w = Rate.objects.filter(weight__gte=Decimal(str(weight)), region=r)[0].weight
		rs = Rate.objects.filter(weight=w, region=r).order_by('price')
		return rs

	def __repr__(self):
		return "<Rate: max %.2fkg@%s, %.2f EUR>" % (self.weight, self.recommanded, self.price)

	class Meta:
		unique_together = (('weight', 'region', 'recommanded'))

