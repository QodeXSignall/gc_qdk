from gc_qdk.tests.round_tests import functions

scenaries = {'normal_round':
    {'BEFORE_WEIGHING':
        {'WAIT_PHOTOCELL_BLOCK_EXTERNAL_PHOTOCELL':
            {'photocell':
                {
                    'operation': functions.block_external_photocell,
                    'timer': 55}},
            'PHOTOCELL_WAS_BLOCKED_EXTERNAL_PHOTOCELL':
                {'weight': {'operation': functions.set_weight_value,
                            'value': 500,
                            'used': False}},
            'WAIT_PHOTOCELL_RELIEVE_EXTERNAL_PHOTOCELL':
                {'photocell':
                    {
                        'operation': functions.unblock_external_photocell,
                        'timer': 54},
                    'weight': {
                        'operation': functions.set_weight_value,
                        'timer': 44,
                        'value': 1000,
                        'used': False}},
            'PHOTOCELL_AFTER_RELIEVE_WAIT_EXTERNAL_PHOTOCELL':
                {'weight': {'operation': functions.set_weight_value,
                            'timer': 3,
                            'value': 5000,
                            'used': False}},

            'WAIT_PHOTOCELL_BLOCK_INTERNAL_PHOTOCELL':
                {'photocell':
                    {
                        'operation': functions.block_external_photocell,
                        'timer': 1794}},
            'WAIT_PHOTOCELL_RELIEVE_INTERNAL_PHOTOCELL':
                {'photocell':
                    {
                        'operation': functions.unblock_internal_photocell,
                        'timer': 54},
                    'weight': {
                        'operation': functions.set_weight_value,
                        'timer': 44,
                        'value': 13000,
                        'used': False}},
        },

        'AFTER_WEIGHING':
            {'WAIT_PHOTOCELL_BLOCK_INTERNAL_PHOTOCELL':
                {'photocell': {
                    'operation': functions.block_internal_photocell,
                    'timer': 1795}},
                'WAIT_PHOTOCELL_RELIEVE_INTERNAL_PHOTOCELL':
                    {'photocell': {
                        'operation': functions.unblock_internal_photocell,
                        'timer': 55},
                        'weight': {'operation': functions.set_weight_value,
                                   'timer': 54,
                                   'value': 500,
                                   'used': False}},

                'WAIT_PHOTOCELL_BLOCK_EXTERNAL_PHOTOCELL':
                    {'photocell': {
                        'operation': functions.block_external_photocell,
                        'timer': 58}},
                'WAIT_PHOTOCELL_RELIEVE_EXTERNAL_PHOTOCELL':
                    {'photocell': {
                        'operation': functions.unblock_external_photocell,
                        'timer': 55},
                        'weight': {'operation': functions.set_weight_value,
                                   'timer': 54,
                                   'value': 500,
                                   'used': False}},

                'WAITING_ESCAPING': {
                    'weight': {
                        'operation': functions.set_weight_value,
                        'value': 10,
                        'used': False
                    },
                    'photocell':
                        {'operation': functions.block_internal_photocell,
                         'timer': 55},
                }
            }}}
