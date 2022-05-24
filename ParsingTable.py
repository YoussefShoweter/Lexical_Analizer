parsing_table = [
    # State 0
    {
        'actions': {
            'repeat': ('s', 5),
            'ID': ('s', 6)
        },
        'goto': {
            'stmt-seq': 1,
            'statement': 2,
            'repeat-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 1
    {
        'actions': {
            'ID': ('s', 6),
            'repeat': ('s', 5),
            '$': ('r', 1)       # acceptance
        },
        'goto': {
            'statement': 7,
            'repeat-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 2
    {
        'actions': {
            'ID': ('r', 3),
            'repeat': ('r', 3),
            'until': ('r', 3),
            '$': ('r', 3)
        },
        'goto': {}
    },

    # State 3
    {
        'actions': {
            'ID': ('r', 4),
            'repeat': ('r', 4),
            'until': ('r', 4),
            '$': ('r', 4)
        },
        'goto': {}
    },

    # State 4
    {
        'actions': {
            'ID': ('r', 5),
            'repeat': ('r', 5),
            'until': ('r', 5),
            '$': ('r', 5)
        },
        'goto': {}
    },

    # State 5
    {
        'actions': {
            'repeat': ('s', 5),
            'ID' : ('s',6)
        },
        'goto': {
            'stmt-seq': 8,
            'statement': 2,
            'repeat-stmt': 3,
            'assign-stmt': 4
        }
    },

    # State 6
    {
        'actions': {
            ':=': ('s', 9)
        },
        'goto': {}
    },

    # State 7
    {
        'actions': {
            'ID': ('r', 2),
            'repeat': ('r', 2),
            'until': ('r', 2),
            '$': ('r', 2)
        },
        'goto': {}
    },

    # State 8
    {
        'actions': {
            'repeat': ('s', 5),
            'until' : ('s', 10),
            'ID' :('s',6)
        },
        'goto': {
            'statement': 7,
            'repeat-stmt': 3,
            'assign-stmt': 4

        }
    },

    # State 9
    {
        'actions': {
            'NUM': ('s', 13),
            'ID': ('s', 12)
        },
        'goto': {
            'factor': 11
        }
    },

    # State 10
    {
        'actions': {
            'ID': ('s', 14)
        },
        'goto': {}
    },

    # State 11
    {
        'actions': {
            ';': ('s', 15)
        },
        'goto': {}
    },

    # State 12
    {
        'actions': {
            ';': ('r', 8)
        },
        'goto': {}
    },

    # State 13
    {
        'actions': {
            ';': ('r', 9)
        },
        'goto': {}
    },

    # State 14
    {
        'actions': {
            'ID': ('r', 6),
            'repeat': ('r', 6),
            'until': ('r', 6),
            '$': ('r', 6)
        },
        'goto': {}
    },

  # State 15
    {
        'actions': {
            'ID': ('r', 7),
            'repeat': ('r', 7),
            'until': ('r', 7),
            '$': ('r', 7)
        },
        'goto': {}
    }
]


production_rules = [
    (),
    # Rule 1
    ("s'", ['stmt-seq']),
    # Rule 2
    ('stmt-seq', ['stmt-seq', 'statement']),
    # Rule 3
    ('stmt-seq', ['statement']),
    # Rule 4
    ('statement', ['repeat-stmt']),
    # Rule 5
    ('statement', ['assign-stmt']),
    # Rule 6
    ('repeat-stmt', ['repeat', 'stmt-seq', 'until', 'ID']),
    # Rule 7
    ('assign-stmt', ['ID', ':=', 'factor', ';']),
    # Rule 8
    ('factor', ['ID']),
    # Rule 9
    ('factor', ['NUM'])
]