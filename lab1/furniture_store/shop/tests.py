from django.test import TestCase
import django
from .models import Product, Category, Color, Feature, FeatureVariant, FeatureSet
from .data_builders import ColorBuilder


class ProductTestCase(TestCase):
	def setUp(self):
		builder = ColorBuilder()
		builder.with_name('TestColor')
		record = builder.build()
		record.save()

	def test_create_none_name(self):
		builder =  ColorBuilder()

		with self.assertRaises(django.db.utils.IntegrityError):
			record = builder.build()
			record.save()

	def test_get_from_db(self):
		name = 'TestColor'
		test_record = Color.objects.get(name=name)
		self.assertEqual(test_record.name, name)

	def test_str(self):
		name = 'TestColor'
		builder = ColorBuilder()
		builder.with_name(name)
		record = builder.build()

		check_str = str(record)

		self.assertEqual(name, check_str)
