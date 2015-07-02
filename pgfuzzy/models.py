from django.db.models import (
    Transform, Lookup, CharField, PositiveIntegerField
)

class SoundsLike(Lookup):
    lookup_name = 'sounds_like'

    def as_sql(self, qn, connection):
        lhs, lhs_params = self.process_lhs(qn, connection)
        rhs, rhs_params = self.process_rhs(qn, connection)
        params = lhs_params + rhs_params
        return 'dmetaphone(%s) = dmetaphone(%s)' % (lhs, rhs), params

class Soundex(Transform):

    lookup_name = 'soundex'

    def as_sql(self, qn, connection):
        lhs, params = qn.compile(self.lhs)
        return 'soundex(%s)' % (lhs), params

    @property
    def output_field(self):
        return CharField()

class Difference(Transform):

    lookup_name = 'difference'

    def as_sql(self, qn, connection):
        lhs, lhs_params = qn.compile(self.lhs)
        rhs, rhs_params = self.process_rhs(qn, connection)
        params = lhs_params + rhs_params
        return 'difference(%s, %s)' % (lhs), params

    @property
    def output_field(self):
        return PositiveIntegerField()

class Levenshtein(Transform):

    lookup_name = 'levenshtein'

    def as_sql(self, qn, connection):
        lhs, lhs_params = qn.compile(self.lhs)
        rhs, rhs_params = self.process_rhs(qn, connection)
        params = lhs_params + rhs_params
        return 'levenshtein(%s, %s)' % (lhs), params

    @property
    def output_field(self):
        return PositiveIntegerField()

class DoubleMetaphone(Transform):

    lookup_name = 'dmetaphone'

    def as_sql(self, qn, connection):
        lhs, params = qn.compile(self.lhs)
        return 'dmetaphone(%s)' % (lhs), params

    @property
    def output_field(self):
        return CharField()

CharField.register_lookup(SoundsLike)
CharField.register_lookup(Soundex)
CharField.register_lookup(Difference)
CharField.register_lookup(DoubleMetaphone)
