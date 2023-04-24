"""empty message

Revision ID: 274ac8ede1e2
Revises: e9dd99a28a2e
Create Date: 2023-04-19 00:20:06.276424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '274ac8ede1e2'
down_revision = 'e9dd99a28a2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('hiring',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('hiring',
               existing_type=sa.String(length=120),
               type_=sa.BOOLEAN(),
               existing_nullable=False)

    # ### end Alembic commands ###