"""empty message

Revision ID: 40cf9d90b61a
Revises: 
Create Date: 2023-09-14 06:43:56.872094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40cf9d90b61a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mercado',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=20), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mercado')
    # ### end Alembic commands ###
