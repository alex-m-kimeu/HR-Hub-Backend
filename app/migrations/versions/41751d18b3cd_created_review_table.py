"""created review table

Revision ID: 41751d18b3cd
Revises: 
Create Date: 2024-04-17 12:13:08.659017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41751d18b3cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
