"""Initial migration

Revision ID: d11d7127a5af
Revises: 
Create Date: 2024-04-27 04:50:08.810926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd11d7127a5af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('department', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('leaves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('leaveType', sa.String(), nullable=False),
    sa.Column('startDate', sa.Date(), nullable=False),
    sa.Column('endDate', sa.Date(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('leaves')
    op.drop_table('employees')
    # ### end Alembic commands ###
