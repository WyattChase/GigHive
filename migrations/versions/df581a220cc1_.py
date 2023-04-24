"""empty message

Revision ID: df581a220cc1
Revises: d9bdad07c17e
Create Date: 2023-04-21 01:37:27.171490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df581a220cc1'
down_revision = 'd9bdad07c17e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.TEXT(),
               existing_nullable=True)

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=250),
               existing_nullable=True)

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###