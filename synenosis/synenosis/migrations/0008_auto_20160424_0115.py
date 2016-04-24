# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synenosis', '0007_auto_20160424_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='completed_datetime',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='posted_datetime',
            new_name='posted',
        ),
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.TextField(blank=True, verbose_name=b'Comment'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='balance_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name=b'New balance amount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='balance_currency',
            field=models.CharField(blank=True, choices=[(b'EUR', b'Euro'), (b'GBP', b'GB Pound'), (b'USD', b'US Dollar'), (b'AFN', b'Afghani'), (b'DZD', b'Algerian Dinar'), (b'ARS', b'Argentine Peso'), (b'AMD', b'Armenian Dram'), (b'AWG', b'Aruban Florin'), (b'AUD', b'Australian Dollar'), (b'AZN', b'Azerbaijanian Manat'), (b'BSD', b'Bahamian Dollar'), (b'BHD', b'Bahraini Dinar'), (b'THB', b'Baht'), (b'PAB', b'Balboa'), (b'BBD', b'Barbados Dollar'), (b'BYR', b'Belarussian Ruble'), (b'BZD', b'Belize Dollar'), (b'BMD', b'Bermudian Dollar'), (b'VEF', b'Bolivar Fuerte'), (b'BOB', b'Boliviano'), (b'BRL', b'Brazilian Real'), (b'BND', b'Brunei Dollar'), (b'BGN', b'Bulgarian Lev'), (b'BIF', b'Burundi Franc'), (b'CAD', b'Canadian Dollar'), (b'CVE', b'Cape Verde Escudo'), (b'KYD', b'Cayman Islands Dollar'), (b'GHS', b'Cedi'), (b'XOF', b'CFA Franc BCEAO'), (b'XAF', b'CFA Franc BEAC'), (b'XPF', b'CFP Franc'), (b'CLP', b'Chilean Peso'), (b'COP', b'Colombian Peso'), (b'KMF', b'Comoro Franc'), (b'BAM', b'Convertible Marks'), (b'NIO', b'Cordoba Oro'), (b'CRC', b'Costa Rican Colon'), (b'HRK', b'Croatian Kuna'), (b'CUC', b'Cuba Convertible Peso'), (b'CUP', b'Cuban Peso'), (b'CZK', b'Czech Koruna'), (b'GMD', b'Dalasi'), (b'DKK', b'Danish Krone'), (b'MKD', b'Denar'), (b'DJF', b'Djibouti Franc'), (b'STD', b'Dobra'), (b'DOP', b'Dominican Peso'), (b'VND', b'Dong'), (b'XCD', b'East Caribbean Dollar'), (b'EGP', b'Egyptian Pound'), (b'ETB', b'Ethiopian Birr'), (b'FKP', b'Falkland Islands Pound'), (b'FJD', b'Fiji Dollar'), (b'HUF', b'Forint'), (b'CDF', b'Franc Congolais'), (b'GIP', b'Gibraltar Pound'), (b'HTG', b'Gourde'), (b'PYG', b'Guarani'), (b'GNF', b'Guinea Franc'), (b'GYD', b'Guyana Dollar'), (b'HKD', b'Hong Kong Dollar'), (b'UAH', b'Hryvnia'), (b'ISK', b'Iceland Krona'), (b'INR', b'Indian Rupee'), (b'IRR', b'Iranian Rial'), (b'IQD', b'Iraqi Dinar'), (b'JMD', b'Jamaican Dollar'), (b'JOD', b'Jordanian Dinar'), (b'KES', b'Kenyan Shilling'), (b'PGK', b'Kina'), (b'LAK', b'Kip'), (b'KWD', b'Kuwaiti Dinar'), (b'MWK', b'Kwacha'), (b'AOA', b'Kwanza'), (b'MMK', b'Kyat'), (b'GEL', b'Lari'), (b'LBP', b'Lebanese Pound'), (b'ALL', b'Lek'), (b'HNL', b'Lempira'), (b'SLL', b'Leone'), (b'LRD', b'Liberian Dollar'), (b'LYD', b'Libyan Dinar'), (b'SZL', b'Lilangeni'), (b'LSL', b'Loti'), (b'MGA', b'Malagascy Ariary'), (b'MYR', b'Malaysian Ringgit'), (b'MUR', b'Mauritius Rupee'), (b'MXN', b'Mexican Peso'), (b'MXV', b'Mexican Unidad de Inversion'), (b'MDL', b'Moldovan Leu'), (b'MAD', b'Moroccan Dirham'), (b'MZN', b'Mozambique Metical'), (b'BOV', b'Mvdol'), (b'NGN', b'Naira'), (b'ERN', b'Nakfa'), (b'NAD', b'Namibian Dollar'), (b'NPR', b'Nepalese Rupee'), (b'ANG', b'Netherlands Antillian Guilder'), (b'ILS', b'New Israeli Sheqel'), (b'RON', b'Romanian Leu'), (b'TWD', b'New Taiwan Dollar'), (b'TRY', b'Turkish Lira'), (b'NZD', b'New Zealand Dollar'), (b'BTN', b'Ngultrum'), (b'KPW', b'North Korean Won'), (b'NOK', b'Norwegian Krone'), (b'PEN', b'Nuevo Sol'), (b'MRO', b'Ouguiya'), (b'TOP', b'Paanga'), (b'PKR', b'Pakistan Rupee'), (b'MOP', b'Pataca'), (b'UYU', b'Peso Uruguayo'), (b'PHP', b'Philippine Peso'), (b'BWP', b'Pula'), (b'QAR', b'Qatari Rial'), (b'GTQ', b'Quetzal'), (b'ZAR', b'Rand'), (b'OMR', b'Rial Omani'), (b'KHR', b'Riel'), (b'MVR', b'Rufiyaa'), (b'IDR', b'Rupiah'), (b'RUB', b'Russian Ruble'), (b'RWF', b'Rwanda Franc'), (b'XDR', b'SDR'), (b'SHP', b'Saint Helena Pound'), (b'SAR', b'Saudi Riyal'), (b'RSD', b'Serbian Dinar'), (b'SCR', b'Seychelles Rupee'), (b'SGD', b'Singapore Dollar'), (b'SBD', b'Solomon Islands Dollar'), (b'KGS', b'Som'), (b'SOS', b'Somali Shilling'), (b'TJS', b'Somoni'), (b'LKR', b'Sri Lanka Rupee'), (b'SDG', b'Sudanese Pound'), (b'SRD', b'Surinam Dollar'), (b'SEK', b'Swedish Krona'), (b'CHF', b'Swiss Franc'), (b'SYP', b'Syrian Pound'), (b'BDT', b'Taka'), (b'WST', b'Tala'), (b'TZS', b'Tanzanian Shilling'), (b'KZT', b'Tenge'), (b'TTD', b'Trinidad and Tobago Dollar'), (b'MNT', b'Tugrik'), (b'TND', b'Tunisian Dinar'), (b'TMT', b'Turkmenistan New Manat'), (b'AED', b'UAE Dirham'), (b'UGX', b'Uganda Shilling'), (b'COU', b'Unidad de Valor Real'), (b'CLF', b'Unidades de formento'), (b'UYI', b'Uruguay Peso en Unidades Indexadas'), (b'UZS', b'Uzbekistan Sum'), (b'VUV', b'Vatu'), (b'CHE', b'WIR Euro'), (b'CHW', b'WIR Franc'), (b'KRW', b'Won'), (b'YER', b'Yemeni Rial'), (b'JPY', b'Yen'), (b'CNY', b'Yuan Renminbi'), (b'ZMW', b'Zambian Kwacha'), (b'ZWL', b'Zimbabwe Dollar'), (b'PLN', b'Zloty'), (b'BTC', b'Bitcoin')], max_length=3, verbose_name=b'New balance currency'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[(b'DRAFT', b'DRAFT'), (b'APPROVED', b'APPROVED'), (b'PAUSED', b'PAUSED'), (b'CANCELLED', b'CANCELLED'), (b'COMPLETED', b'COMPLETED')], default=b'completed', max_length=9, verbose_name=b'Status'),
        ),
    ]