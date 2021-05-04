from flask_table import Table, Col, LinkCol


class ThingResults(Table):
    id = Col('Id', show=False)
    thing = Col('Thing')
    rating = Col('Rating')
