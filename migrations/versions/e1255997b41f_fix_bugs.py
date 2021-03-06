"""fix bugs

Revision ID: e1255997b41f
Revises: 90089f7961b9
Create Date: 2022-05-16 12:45:06.636668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1255997b41f'
down_revision = '90089f7961b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('pename', sa.String(length=255), nullable=True))
    op.drop_column('blog', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('blog', 'pename')
    # ### end Alembic commands ###
