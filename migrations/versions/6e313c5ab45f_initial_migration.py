"""initial migration

Revision ID: 6e313c5ab45f
Revises: 4347b93e4f62
Create Date: 2016-09-05 11:01:04.604142

"""

# revision identifiers, used by Alembic.
revision = '6e313c5ab45f'
down_revision = '4347b93e4f62'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
