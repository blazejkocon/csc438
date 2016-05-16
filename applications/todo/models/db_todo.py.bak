# -*- coding: utf-8 -*-

db.define_table('todo_items',
                Field('description',type="string", requires=IS_NOT_EMPTY()),
                Field('deadline',type ='datetime', requires= IS_NOT_EMPTY()),auth.signature)

rows = SQLTABLE(db(db.todo_items.created_by==auth.user).select(),columns=["todo.description", 
                              "todo.deadline"
                              ],
                     headers={"todo.description": "Description",
                              "todo.deadline": "Deadline",
                             })
