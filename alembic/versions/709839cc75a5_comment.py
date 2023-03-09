"""comment

Revision ID: 709839cc75a5
Revises: 
Create Date: 2023-03-09 14:16:15.954775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '709839cc75a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fuser')
    # ### end Alembic commands ###
