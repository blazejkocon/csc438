# -*- coding: utf-8 -*-
db.define_table('ip2nationCountries',
                Field('code',requires=IS_NOT_EMPTY()),
                Field('iso_code_2',requires= IS_NOT_EMPTY()),
               Field('iso_code_3',requires= IS_NOT_EMPTY()),
               Field('iso_country',requires=IS_NOT_EMPTY()),
                Field('country',requires=IS_NOT_EMPTY()),
                Field('lat',requires=IS_NOT_EMPTY()),
                 Field('lon',requires=IS_NOT_EMPTY()))
