"""empty message

Revision ID: afdec6e57a94
Revises: b52e7d9d6dd5
Create Date: 2023-04-28 17:15:08.483927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afdec6e57a94'
down_revision = 'b52e7d9d6dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Favorites', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['Favorites'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Favorites', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['Favorites'], ['id'])

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Favorites', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['Favorites'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('Favorites')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('Favorites')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('Favorites')

    op.drop_table('favorites')
    # ### end Alembic commands ###