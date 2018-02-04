riskTypes = [
    {
        'id': 1,
        'name': u'Risk type 1',
        'description': u'This is the risk type 1'
    },
    {
        'id': 2,
        'name': u'Risk type 2',
        'description': u'This is the risk type 2'
    }
]


class RiskType(object):

    @staticmethod
    def get_all():
        return riskTypes
