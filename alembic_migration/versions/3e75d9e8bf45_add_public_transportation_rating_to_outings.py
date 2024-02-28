"""Add public_transportation_rating to outings

Revision ID: 3e75d9e8bf45
Revises: 305b064bdf66
Create Date: 2024-02-28 18:28:40.411945

"""
from alembic import op
import sqlalchemy as sa
from c2corg_api.models import enums


# revision identifiers, used by Alembic.
revision = '3e75d9e8bf45'
down_revision = '305b064bdf66'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        'outings',
        sa.Column('public_transportation_rating', enums.public_transportation_rating),
        schema='guidebook')


def downgrade():
    op.drop_column('outings', 'public_transportation_rating', schema='guidebook')
