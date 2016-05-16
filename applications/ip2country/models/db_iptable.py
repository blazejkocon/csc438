# -*- coding: utf-8 -*-
db.define_table('ip2nation',
                Field('code',type='integer', requires=IS_NOT_EMPTY()),
                Field('country', requires= IS_NOT_EMPTY()))
