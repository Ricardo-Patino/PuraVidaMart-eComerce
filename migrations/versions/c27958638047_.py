"""empty message

Revision ID: c27958638047
Revises: 
Create Date: 2023-07-10 20:31:37.443876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c27958638047'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('category', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('lastname', sa.String(length=250), nullable=True),
    sa.Column('seller', sa.Boolean(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_products', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_products'], ['products.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=250), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_products', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_products'], ['products.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_products', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_products'], ['products.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_shopping', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_shopping'], ['shopping.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_history')
    op.drop_table('shopping')
    op.drop_table('review')
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('products')
    # ### end Alembic commands ###
